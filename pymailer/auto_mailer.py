""" Created by Jieyi on 2/4/16. """
import threading
import tkinter.messagebox as messagebox
from tkinter import Frame, Label, Entry, Button, END
from tkinter.scrolledtext import ScrolledText

from internet import InternetStatus
from mailer import Mailer


class Application(Frame):
    def __init__(self, master=None):
        # Avoiding to send it continuously.
        self.lock = False

        Frame.__init__(self, master)
        self.grid()
        # UI components.
        self.receiver_email_text = Label(self, text="Receiver:")
        self.receiver_email_field = Entry(self, width=50)
        self.subject_text = Label(self, text='Subject:')
        self.subject_field = Entry(self, width=50)
        self.receiver_name_text = Label(self, text='Name:')
        self.receiver_name_field = Entry(self, width=50)
        self.send_button = Button(self, text='Send', command=self.__send_mail)
        self.log_msg_text = ScrolledText(self)
        self.__create_widgets()

        # Let Mailer can control components.
        Mailer.window_context = self

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
        self.send_button.grid(row=3, column=3)
        self.log_msg_text.grid(row=4, column=0, columnspan=7)

    def __send_mail(self):
        def inner_send_mail():
            self.lock = True  # Lock this process.
            # Clear the log text area.
            self.log_msg_text.delete('1.0', END)
            # Error checking.
            if not self.__check_internet():
                self.log_msg_text.insert(END, '\n** Please check your internet state.\n\n')
                self.lock = False  # Unlock this process.
                return

            ending = 'Welcome to use my application :)' if Mailer().send_mail() else '** Your sending was failed :( please send it again!'
            self.log_msg_text.insert(END, ending)
            self.lock = False  # Unlock this process.

        if not self.lock:
            threading.Thread(target=inner_send_mail).start()
        else:
            messagebox.showinfo('Warning', "Now it's processing...")

    def __check_internet(self):
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


# Main function for all library.
def main():
    """
    * If you use pyCharm to execute this project, the file path shouldn't
      add os.path.abspath(os.pardir). Because of the shell script, we need
      to add correct file path.
    """
    app = Application()
    app.master.title('Auto Mailer')
    app.mainloop()


if __name__ == '__main__':
    main()
