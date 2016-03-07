""" Created by Jieyi on 2/5/16. """
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail:
    """
    Mail format. All of the mail information in this class.
    """

    def __init__(self, uid, to, subject, content, attach):
        self.__msg = MIMEMultipart()
        self.__id = uid
        self.__mailTo = to
        self.__mailSub = subject
        self.__content = content
        self.__attachment = attach

    # Create a mail.
    def create_mail(self):
        # Mail header
        self.__msg['From'] = self.__id
        self.__msg['To'] = self.__mailTo
        self.__msg['Subject'] = self.__mailSub

        # Mail content
        self.__msg.attach(MIMEText(self.__content))

        # Mail attachment
        self._create_attachment()

        return self.__msg

    # Create attachments.
    # Users don't have too call this method. Create a mail has already included this.
    def _create_attachment(self):
        for path in self.__attachment:
            # Get the file name from file path.
            self.__filename = path.split('/')[-1]

            # Attach the file to mail information.
            self.att = MIMEText(open(path, 'rb').read(), 'base64', 'gb2312')
            self.att['Content-Type'] = 'application/octet-stream'
            self.att['Content-Disposition'] = 'attachment; filename="%s"' % self.__filename

            self.__msg.attach(self.att)


class MailBuilder:
    """
    Mail builder.
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


# Testing code
def main():
    print()


if __name__ == '__main__':
    main()
