""" Created by Jieyi on 2/5/16. """
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail:
    """
    Mail format. All of the mail information in this class.
    """

    class MailBuilder:
        """
        Mail builder inner.
        """

        def __init__(self):
            self.__id = None
            self.__mailTo = None
            self.__mailSub = None
            self.__content = None
            self.__attach = []

        def uid(self, uid):
            self.__id = uid
            return self

        def to(self, to):
            self.__mailTo = to
            return self

        def subject(self, subject):
            self.__mailSub = subject
            return self

        def content(self, content):
            self.__content = content
            return self

        def attach(self, attachment):
            self.__attach.append(str(attachment))
            return self

        def build(self):
            return Mail(self.__id, self.__mailTo, self.__mailSub, self.__content, self.__attach)

    def __init__(self, uid, to, subject, content, attach):
        self.__msg = MIMEMultipart()
        self.__id = uid
        self.__mailTo = to
        self.__mailSub = subject
        self.__content = content
        self.__attachment = attach

    # Create a mail.
    def create_mail(self):
        """
        Create a mail content, including sender, receiver, subject, and attachment......

        :return: All of the mail content.
        """

        # Mail header
        self.__msg['From'] = self.__id
        self.__msg['To'] = self.__mailTo
        self.__msg['Subject'] = self.__mailSub

        # Mail content
        self.__msg.attach(MIMEText(self.__content))

        # Mail attachment
        res, error_msg = self._create_attachment()
        if not res:
            raise FileNotFoundError(error_msg)

        return self.__msg

    # Create attachments.
    # Users don't have too call this method. Create a mail has already included this.
    def _create_attachment(self):
        """
        Attach the necessary file to customer.

        :return: result, True: Success, False: Failed. lack_file_name, Which file you didn't attach.
        """

        res = True
        lack_file_name = ''
        for path in self.__attachment:
            try:
                # Get the file name from file path.
                self.__filename = path.split('\\')[-1]

                # Attach the file to mail information.
                att = MIMEText(open(path, 'rb').read(), 'base64', 'gb2312')
                att['Content-Type'] = 'application/octet-stream'
                att['Content-Disposition'] = 'attachment; filename="%s"' % self.__filename

                self.__msg.attach(att)
            except FileNotFoundError as fnfe:
                res = False
                lack_file_name += str(fnfe) + '\n'
        return res, lack_file_name


# Testing code
def main():
    print()


if __name__ == '__main__':
    main()
