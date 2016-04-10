""" Created by Jieyi on 2/4/16. """
import copy
import threading
import tkinter
import tkinter.messagebox as messagebox
from tkinter import Frame, Label, Entry, Button, END, StringVar
from tkinter.constants import FALSE
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar, Combobox

from __init__ import debug_log, attachment_list, lang_list, content_link_title, content_link, atta_lang_list
from mail_checker import CheckModifyContentTitle, CheckInternet, CheckInputReceiver, CheckSelectLanguage
from mailer import Mailer


class DecoratorThreadLockerApp:
    """
    Decorator to application for lock the thread.
    """

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            """
            For locking the thread processing.
            """

            decoratee = args[0]

            decoratee.lock = True  # Lock this process.
            decoratee.send_progressbar['value'] = 0
            decoratee.log_msg_text.delete('1.0', END)  # Clear the log text area.

            res = func(*args)

            decoratee.lock = False  # Unlock this process.
            return res

        return wrapper


class DecoratorErrorCheckAndInitApp:
    """
    Decorator to application for error checking.
    """

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            """
            Error checking.
            """

            decoratee = args[0]
            decoratee.log_msg_text.insert(END, 'We start to check your input format...\n\n')

            # Error checker.
            checker = CheckInternet(
                None, CheckSelectLanguage(
                    decoratee.url_lang_combobox.current(), CheckInputReceiver(
                        decoratee.receiver_name_field.get())))

            # Checking all of the error check.
            res, msg = checker.do_something()

            # Pass the 1st checking step.
            if res:
                # Create a Mailer object.
                decoratee._mailer = decoratee._make_mailer()
                # For English content. The 2nd step, checking English content's url title.
                if decoratee.url_lang_combobox.get() != lang_list[2] and decoratee.url_lang_combobox.get() != lang_list[3]:
                    res, msg = CheckModifyContentTitle([decoratee._mailer.content, decoratee.url_lang_link_title]).do_something()

                    # Pass the 2nd checking step.
                    if res:
                        # Change to the language we selected url link.
                        decoratee._modify_content_url_link()

            # The checking is fail.
            decoratee.log_msg_text.insert(END, msg)  # Show the error msg.
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
        self.url_lang_combobox_list = lang_list
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
        self.mail_attachment_list = attachment_list[:]
        self.url_lang_link_title = content_link_title[:]
        self.url_lang_link = copy.deepcopy(content_link)
        # Mailer
        self._mailer = None

        # Let Mailer can control components.
        Mailer.window_content = self

        self.__create_widgets()

    def _send_mail(self):
        if not self.lock:
            threading.Thread(target=self.__send_mail).start()
        else:
            messagebox.showinfo('Warning', "Now it's processing...")

    def _choose(self, event):
        # arr = self.url_lang_link.get(self.url_lang_combobox_str.get())  # Get the array by choosing language.
        pass

    def _modify_content_url_link(self):
        link_arr = self.url_lang_link.get(self.url_lang_combobox_str.get())
        content = self._mailer.content
        for index in range(len(link_arr)):
            content_index = content.index(self.url_lang_link_title[index]) + len(self.url_lang_link_title[index])
            content = content[:content_index] + '\n' + link_arr[index] + content[content_index:]

        self._mailer.content = content
        return False

    def _make_mailer(self):
        self.mail_attachment_list = attachment_list[:]  # Clone a list.
        if atta_lang_list[self.url_lang_combobox.current()]:
            for i in range(len(self.mail_attachment_list)):
                # Only from the third file to the end file can change language.
                if i > 2:
                    # Modify the file name.
                    att = self.mail_attachment_list[i].split('.')
                    self.mail_attachment_list[i] = ''.join([' ', atta_lang_list[self.url_lang_combobox.current()], '.']).join(att)

        path = 'content.docx'
        if self.url_lang_combobox.get() == lang_list[2] or self.url_lang_combobox.get() == lang_list[3]:
            path = 'content chinese.docx'
        if debug_log:
            print(self.mail_attachment_list)

        # ** IMPORTANT, we have to new an object here. Otherwise, we couldn't check the error checking.
        return Mailer(content_path=path, attachment_list=self.mail_attachment_list)

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
    @DecoratorErrorCheckAndInitApp()
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
