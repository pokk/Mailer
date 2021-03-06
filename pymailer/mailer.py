""" Created by wu.jieyi on 2016/03/07. """
import os
import smtplib
from tkinter import END

from __init__ import debug_log
from authority import Authority
from io_operation import FileOperator
from mail import Mail

# For decorator's parameter.
user = FileOperator().open_json_file(os.path.abspath(os.pardir) + '/user.json')


class Mailer:
    """
    We collate all of mail operations here.
    As like 'send', delete, ...
    """

    window_content = None

    def __init__(self, content_path=None, attachment_list=None):
        self._file_arr = attachment_list
        self._mail = None
        self._file_path = ''
        # Get receiver's information from local json file.
        self._content = FileOperator().open_docx_file(os.path.abspath(os.pardir) + '/' + content_path)

    # Send a mail to someone through which mail service.
    @Authority(user['uid'], user['pwd'], user['server'])
    def send_mail(self, mail_server):
        self._mail = self._making_mail()

        Mailer.window_content.log_msg_text.insert(END, 'Combining all of the information to a mail...\n')

        try:
            mail_info = self._mail.create_mail()
        except FileNotFoundError as fnfe:
            Mailer.window_content.log_msg_text.insert(END, 'You lack some file.\n\n')
            Mailer.window_content.log_msg_text.insert(END, '** ' + str(fnfe) + '\n')
            return False

        Mailer.window_content.log_msg_text.insert(END, 'Finish combining!!\n\n')

        if debug_log:
            print(mail_info)

        Mailer.window_content.log_msg_text.insert(END, 'Start to send the mail...\n')

        try:
            mail_server.sendmail(mail_info['From'], mail_info['To'], mail_info.as_string())
        except smtplib.SMTPRecipientsRefused as stmp_refused:
            Mailer.window_content.log_msg_text.insert(END, '\n** ' + str(stmp_refused) + '\n\n')
            return False

        Mailer.window_content.log_msg_text.insert(END, 'Finished sending!!\n\n')
        return True

    def _making_mail(self):

        Mailer.window_content.log_msg_text.insert(END, 'Creating the mail format...\n')

        # Modify the content's receiver name.
        self._content = self._content.replace('**name**', Mailer.window_content.receiver_name_field.get())
        # Find the attachment dir path.
        self._file_path = '..' + self._file_dir_path()

        # Build a mail data.
        mail = Mail.MailBuilder() \
            .uid(user['uid']) \
            .to(Mailer.window_content.receiver_email_field.get()) \
            .subject(Mailer.window_content.subject_field.get()) \
            .content(self._content)

        for file in self._file_arr:
            attachment = os.path.join(self._file_path, file)
            mail.attach(attachment)

        Mailer.window_content.log_msg_text.insert(END, 'Finish the creating a mail!!\n\n')

        return mail.build()

    def _file_dir_path(self):
        # Get the folder path which is the same as where this file is.
        dir_path = os.path.dirname(os.path.abspath(__file__))
        # Go to parent's folder path.
        dir_path = self._file_path[0:dir_path.rfind('/')]
        # Change path to mail folder.
        dir_path = '/../'.join((dir_path, 'For mail'))

        return dir_path

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value


def main():
    mail = Mail.MailBuilder().uid(user['uid']).to('sample@google.com').subject('Hello world').content('Oh, just testing!!').build()
    # 'mail' parameter will send to Authority decorator's __call__.
    Mailer().send_mail()


if __name__ == '__main__':
    main()
