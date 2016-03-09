""" Created by Jieyi on 2/4/16. """
import threading
import tkinter
import tkinter.messagebox as messagebox
from tkinter import Frame, Label, Entry, Button, END, StringVar
from tkinter.constants import FALSE
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar, Combobox

from internet import InternetStatus
from mailer import Mailer


class DecoratorThreadLockerApp:
    """
    Decorator to application for lock the thread.
    """

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            decoratee = args[0]

            decoratee.lock = True  # Lock this process.
            decoratee.send_progressbar['value'] = 0
            decoratee.log_msg_text.delete('1.0', END)  # Clear the log text area.

            res = func(*args)

            decoratee.lock = False  # Unlock this process.
            return res

        return wrapper


class DecoratorErrorCheckApp:
    """
    Decorator to application for error checking.
    """

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            """
            Error checking.
            """

            decoratee = args[0]
            res = True

            # Check combobox.
            if res and decoratee.url_lang_combobox.current() is 0:
                decoratee.log_msg_text.insert(END, '\n** Please select a language, thanks! ;)\n\n')
                res &= False
            # Check receiver name.
            if res and not decoratee.is_input_receiver():
                decoratee.log_msg_text.insert(END, "\n** Please don't forget to input receiver name. ^_^\n\n")
                res &= False
            # Check internet.
            if res and not decoratee.is_internet():
                decoratee.log_msg_text.insert(END, '\n** Please check your internet state.\n\n')
                res &= False
            # Check content key word.
            if res and not decoratee.modify_content_link(decoratee.url_lang_link.get(decoratee.url_lang_combobox_str.get())):
                decoratee.log_msg_text.insert(END, '\n** Please check your content key word.\n\n')
                res &= False

            decoratee.lock = res  # Unlock the thread locker.
            return func(*args) if res else res

        return wrapper


class AppGUI(Frame):
    def __init__(self, master=None):
        # Avoiding to send it continuously.
        self.lock = False

        Frame.__init__(self, master)
        self.grid()
        self.master = master
        # Setting for ComboBox.
        self.url_lang_combobox_str = StringVar()
        self.url_lang_combobox_list = ['Select a language', 'English', 'Tradition Chinese', 'Simple Chinese', 'Korea']
        # UI components.
        self.receiver_email_text = Label(self, text="Receiver:")
        self.receiver_email_field = Entry(self, width=50)
        self.subject_text = Label(self, text='Subject:')
        self.subject_field = Entry(self, width=50)
        self.receiver_name_text = Label(self, text='Name:')
        self.receiver_name_field = Entry(self, width=50)
        self.url_lang_text = Label(self, text='Link lang:')
        self.url_lang_combobox = Combobox(self, textvariable=self.url_lang_combobox_str, values=self.url_lang_combobox_list, state='readonly')
        self.send_progressbar = Progressbar(self, orient='horizontal', length=500, mode='determinate', maximum=300)
        self.send_button = Button(self, text='Send', command=self._send_mail)
        self.quit_button = Button(self, text='Exit', command=self.__exit)
        self.log_msg_text = ScrolledText(self)
        # Attachment.
        self._mail_attachment_list = ['Detail Map.png', 'Map.png', 'Kansai Int Access.pdf', 'GARBAGE.pdf',
                                      'Home Utensils.pdf', 'Rule for email.pdf', 'Self Check.pdf']
        self.url_lang_link_title = ['< Japan Guide >', '< Weather Forecast in Osaka >',
                                    '< Shuttle bus station at KIX to / from the Rinku Premium Outlet Shopping Mall >',
                                    '< Shuttle Bus Timetable Between KIX and the Rinku Premium Outlet Mall >',
                                    '< USJ >', '< KAIYUKAN AQUARIUM 海遊館 >']
        self.url_lang_link = {self.url_lang_combobox_list[1]: ['http://www.japan-guide.com/e/e2361.html',
                                                               'http://meteocast.net/forecast/jp/osaka/',
                                                               'http://www.kansai-airport.or.jp/en/index.asp',
                                                               'http://www.kate.co.jp/en/',
                                                               'http://www.usj.co.jp/e/',
                                                               'http://www.kaiyukan.com/language/eng/'],
                              self.url_lang_combobox_list[2]: ['http://tw.japan-guide.com/',
                                                               'http://cn.meteocast.net/forecast/jp/osaka/',
                                                               'http://www.kansai-airport.or.jp/tw/index.asp',
                                                               'http://www.kate.co.jp/tcn/',
                                                               'http://www.usj.co.jp/tw/',
                                                               'http://www.kaiyukan.com/language/chinese_traditional/'],
                              self.url_lang_combobox_list[3]: ['http://cn.japan-guide.com/',
                                                               'http://cn.meteocast.net/forecast/jp/osaka/',
                                                               'http://www.kansai-airport.or.jp/cn/index.asp',
                                                               'http://www.kate.co.jp/scn/',
                                                               'http://www.usj.co.jp/cn/',
                                                               'http://www.kaiyukan.com/language/chinese_simplified/'],
                              self.url_lang_combobox_list[4]: ['http://kr.japan-guide.com/',
                                                               'http://ko.meteocast.net/forecast/jp/osaka/',
                                                               'http://www.kansai-airport.or.jp/kr/index.asp',
                                                               'http://www.kate.co.jp/kr/',
                                                               'http://www.usj.co.jp/kr/',
                                                               'http://www.kaiyukan.com/language/korean/']}
        self._mailer = Mailer(self._mail_attachment_list)

        # Let Mailer can control components.
        Mailer.window_content = self

        self.__create_widgets()

    def is_internet(self):
        """
        Checking the internet state.

        :return: True: internet is available, False: internet is unavailable.
        """

        self.log_msg_text.insert(END, 'Checking the internet...\n')
        # Check the internet is available or not.
        if not InternetStatus().is_internet_connect():
            # If the internet is not connected, we will quit the process.
            self.log_msg_text.insert(END, 'No internet connect!!\n')
            return False
        self.log_msg_text.insert(END, 'Internet is ok!\n\n')
        return True

    def is_input_receiver(self):
        return not not self.receiver_name_field.get()

    def modify_content_link(self, link_arr):
        content = self._mailer.content
        for index in range(len(link_arr)):
            try:
                content_index = content.index(self.url_lang_link_title[index]) + len(self.url_lang_link_title[index])
                content = content[:content_index] + '\n' + link_arr[index] + content[content_index:]
            except ValueError as ve:
                self.log_msg_text.insert(END, self.url_lang_link_title[index] + ' ' + str(ve) + '\n')
                return False

        self._mailer.content = content
        return True

    def _send_mail(self):
        if not self.lock:
            threading.Thread(target=self.__send_mail).start()
        else:
            messagebox.showinfo('Warning', "Now it's processing...")

    def _choose(self, event):
        # arr = self.url_lang_link.get(self.url_lang_combobox_str.get())  # Get the array by choosing language.
        pass

    def __create_widgets(self):
        """
        Construct all of the UI components.
        """

        self.receiver_email_text.grid(row=0, column=0)
        self.receiver_email_field.grid(row=0, column=1, columnspan=6)
        self.subject_text.grid(row=1, column=0)
        self.subject_field.grid(row=1, column=1, columnspan=6)
        self.subject_field.insert(0, 'Osaka Mariko Apartment Location & Condition')
        self.receiver_name_text.grid(row=2, column=0)
        self.receiver_name_field.grid(row=2, column=1, columnspan=6)
        self.url_lang_text.grid(row=3, column=0)
        self.url_lang_combobox.grid(row=3, column=2, columnspan=2)
        self.send_progressbar.grid(row=4, column=0, columnspan=7)
        self.send_button.grid(row=5, column=2)
        self.quit_button.grid(row=5, column=3)
        self.log_msg_text.grid(row=6, column=0, columnspan=7)

        # Default setting.
        self.url_lang_combobox.current(0)
        self.url_lang_combobox.bind("<<ComboboxSelected>>", self._choose)

    def __exit(self):
        if not self.lock:
            self.log_msg_text.insert(END, '\n\n -- Bye Bye --\n')
            self.master.quit()
        else:
            messagebox.showinfo('Error', "Now it's processing...please wait it ;)")

    @DecoratorThreadLockerApp()
    @DecoratorErrorCheckApp()
    def __send_mail(self):
        self.send_progressbar.start()  # Start processing the progress.
        ending = 'Welcome to use my application :)' if self._mailer.send_mail() \
            else '** Your sending was failed :( please send it again!'
        self.log_msg_text.insert(END, ending)
        self.send_progressbar.stop()  # Stop processing the progress.


# Main function for all library.
def main():
    """
    * If you use pyCharm to execute this project, the file path shouldn't
      add os.path.abspath(os.pardir). Because of the shell script, we need
      to add correct file path.
    """

    tk = tkinter.Tk()
    tk.resizable(width=FALSE, height=FALSE)
    app = AppGUI(tk)
    app.master.title('Auto Mailer')
    app.mainloop()


if __name__ == '__main__':
    main()
