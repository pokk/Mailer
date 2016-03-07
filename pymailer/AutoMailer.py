""" Created by Jieyi on 2/4/16. """
import os
import threading
import tkinter.messagebox as messagebox
from tkinter import Frame, Label, Entry, Button, END
from tkinter.scrolledtext import ScrolledText

from pymailer.authority import Mailer, user
from pymailer.internet import InternetStatus
from pymailer.io_operation import FileOperator
from pymailer.mail import Mail

# Get receiver's information from local json file.
# ** The path we should use 'receiver.json' & 'content.txt'. **
content = FileOperator().open_txt_file(os.path.abspath(os.pardir) + '/content.txt')


class Application(Frame):
    def __init__(self, master=None):
        self._file_arr = ['Detail Map.png', 'Map.png', 'Kansai Int Access.pdf', 'GARBAGE.pdf',
                          'Home Utensils.pdf', 'Rule for email.pdf', 'Self Check.pdf']
        self.lock = False
        Frame.__init__(self, master)
        self.grid()

        self.receiver_email_text = Label(self, text="Receiver:")
        self.receiver_email_field = Entry(self, width=50)
        self.subject_text = Label(self, text='Subject:')
        self.subject_field = Entry(self, width=50)
        self.receiver_name_text = Label(self, text='Name:')
        self.receiver_name_field = Entry(self, width=50)
        self.send_button = Button(self, text='Send', command=self.__send_mail)
        self.log_msg_text = ScrolledText(self)

        self.__create_widgets()

        Mailer.window_context = self

    def __create_widgets(self):
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
            self.lock = True
            self.log_msg_text.delete('1.0', END)
            if not self.__check_internet():
                self.log_msg_text.insert(END, 'Please check your internet state.\n\n')
                return

            self.log_msg_text.insert(END, 'Creating the mail format...\n')
            mail = self.__making_email()
            self.log_msg_text.insert(END, 'Finish the creating a mail!!\n\n')

            ending = 'Welcome to use my application :)' if Mailer().send_mail(mail) else '** Your sending was failed :( please send it again!'
            self.log_msg_text.insert(END, ending)
            self.lock = False

        if not self.lock:
            threading.Thread(target=inner_send_mail).start()
        else:
            messagebox.showinfo('Warning', "Now it's processing...")

    def __check_internet(self):
        self.log_msg_text.insert(END, 'Checking the internet...\n')
        # Check the internet is available or not.
        if not InternetStatus().is_internet_connect():
            # If the internet is not connected, we will quit the process.
            self.log_msg_text.insert(END, 'No internet connect!!\n')
            return False
        self.log_msg_text.insert(END, 'Internet is ok!\n\n')
        return True

    def __making_email(self):
        modified_content = content.replace('**name**', self.receiver_name_field.get())

        # Get the folder path which is the same as where this file is.
        same_dir = os.path.dirname(os.path.abspath(__file__))
        # Go to parent's folder path.
        same_dir = same_dir[0:same_dir.rfind('/')]
        # Change path to mail folder.
        same_dir = '/'.join((same_dir, 'For mail'))

        # Build a mail data.
        mail = Mail.MailBuilder() \
            .uid(user['uid']) \
            .to(self.receiver_email_field.get()) \
            .subject(self.subject_field.get()) \
            .content(modified_content)

        for file in self._file_arr:
            attachment = os.path.join(same_dir, file)
            mail.attach(attachment)

        return mail.build()


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
