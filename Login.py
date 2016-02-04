""" Created by Jieyi on 2/4/16. """
import os

from Authority import Mailer, uid
from Mail import MailBuilder

mailTo = 'sample@msn.com'
mailSubject = 'helOoooOo'
mailContent = 'warning testing'


def main():
	sameDir = os.path.dirname(os.path.abspath(__file__))
	attachment1 = os.path.join(sameDir, 'sample.png')

	mail = MailBuilder().uid(uid).to(mailTo).subject(mailSubject).content(mailContent) \
		.attach(attachment1) \
		.build()

	# print(mail.CreateMail())

	Mailer().sendMail(mail)


if __name__ == '__main__':
	main()
