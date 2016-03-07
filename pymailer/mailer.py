""" Created by wu.jieyi on 2016/03/07. """
import os
import smtplib
from tkinter import END

from pymailer import debug_log
from pymailer.authority import Authority
from pymailer.io_operation import FileOperator
from pymailer.mail import Mail

# For decorator's parameter.
user = FileOperator().open_json_file(os.path.abspath(os.pardir) + '/user.json')


class Mailer:
    """
    We collate all of mail operations here.
    As like 'send', delete, ...
    """

    window_context = None

    # Send a mail to someone through which mail service.
    @Authority(user['uid'], user['pwd'], user['server'])
    def send_mail(self, mail, mail_server):
        Mailer.window_context.log_msg_text.insert(END, 'Combining all of the information to a mail...\n')
        try:
            mail_info = mail.create_mail()
        except FileNotFoundError as fnfe:
            Mailer.window_context.log_msg_text.insert(END, 'You lack some file.\n\n')
            Mailer.window_context.log_msg_text.insert(END, '** ' + str(fnfe) + '\n')
            return False
        Mailer.window_context.log_msg_text.insert(END, 'Finish combining!!\n\n')

        if debug_log:
            print(mail_info)

        Mailer.window_context.log_msg_text.insert(END, 'Start to send the mail...\n')
        try:
            mail_server.sendmail(mail_info['From'], mail_info['To'], mail_info.as_string())
        except smtplib.SMTPRecipientsRefused as stmp_refused:
            Mailer.window_context.log_msg_text.insert(END, '\n** ' + str(stmp_refused) + '\n\n')
            return False
        Mailer.window_context.log_msg_text.insert(END, 'Finished sending!!\n\n')


def main():
    mail = Mail.MailBuilder().uid(user['uid']).to('sample@google.com').subject('Hello world').content('Oh, just testing!!').build()
    # 'mail' parameter will send to Authority decorator's __call__.
    Mailer().send_mail(mail)


if __name__ == '__main__':
    main()
