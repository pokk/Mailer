""" Created by Jieyi on 2/4/16. """
import os

from Authority import Mailer, user
from Internet import InternetStatus
from IoOperation import FileOperator
from Mail import MailBuilder

_debug_log = False
# Get receiver's information from local json file.
receiver = FileOperator().open_json_file('receiver.json')


# Main function for all library.
def main():
	# Check the internet is available or not.
	if not InternetStatus().is_internet_connect():
		# If the internet is not connected, we will quit the process.
		print('no internet connect!!')
		return

	# Get the folder path which is the same as where this file is.
	same_dir = os.path.dirname(os.path.abspath(__file__))
	same_dir = '/'.join((same_dir, 'For mail'))

	# Get attachment's file from the same folder.
	attachment1 = os.path.join(same_dir, 'Detail Map.png')
	attachment2 = os.path.join(same_dir, 'Map.png')
	attachment3 = os.path.join(same_dir, 'Kansai Int Access.pdf')
	attachment4 = os.path.join(same_dir, 'GARBAGE.pdf')
	attachment5 = os.path.join(same_dir, 'Home Utensils.pdf')
	attachment6 = os.path.join(same_dir, 'Rule for email.pdf')
	attachment7 = os.path.join(same_dir, 'Self Check.pdf')

	# Build a mail data.
	mail = MailBuilder().uid(user['uid']).to(receiver['To']).subject(receiver['Subject']).content(receiver['Content']) \
		.attach(attachment1) \
		.attach(attachment2) \
		.attach(attachment3) \
		.attach(attachment4) \
		.attach(attachment5) \
		.attach(attachment6) \
		.attach(attachment7) \
		.build()

	if _debug_log:
		print(mail.CreateMail())

	Mailer().send_mail(mail)


if __name__ == '__main__':
	main()
