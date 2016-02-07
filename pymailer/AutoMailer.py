""" Created by Jieyi on 2/4/16. """
import os

from Authority import Mailer, user
from Internet import InternetStatus
from IoOperation import FileOperator
from Mail import MailBuilder

"""
* If you use pyCharm to execute this project, the file path shouldn't
  add os.path.abspath(os.pardir). Because of the shell script, we need
  to add correct file path.
"""

_debug_log = False
# Get receiver's information from local json file.
# ** The path we should use 'receiver.json' & 'content.txt'. **
receiver = FileOperator().open_json_file(os.path.abspath(os.pardir) + '/receiver.json')
content = FileOperator().open_txt_file(os.path.abspath(os.pardir) + '/content.txt')


# Main function for all library.
def main():
	# Change the name for difference people.
	modified_content = content.replace('**name**', receiver['receiver_name'])

	print('Checking the internet...')
	# Check the internet is available or not.
	if not InternetStatus().is_internet_connect():
		# If the internet is not connected, we will quit the process.
		print('no internet connect!!')
		return
	print('Internet is ok!\n')

	# Get the folder path which is the same as where this file is.
	same_dir = os.path.dirname(os.path.abspath(__file__))
	# Go to parent's folder path.
	same_dir = same_dir[0:same_dir.rfind('/')]
	# Change path to mail folder.
	same_dir = '/'.join((same_dir, 'For mail'))

	# Get attachment's file from the same folder.
	attachment1 = os.path.join(same_dir, 'Detail Map.png')
	attachment2 = os.path.join(same_dir, 'Map.png')
	attachment3 = os.path.join(same_dir, 'Kansai Int Access.pdf')
	attachment4 = os.path.join(same_dir, 'GARBAGE.pdf')
	attachment5 = os.path.join(same_dir, 'Home Utensils.pdf')
	attachment6 = os.path.join(same_dir, 'Rule for email.pdf')
	attachment7 = os.path.join(same_dir, 'Self Check.pdf')

	print('Creating the mail format...')
	# Build a mail data.
	mail = MailBuilder().uid(user['uid']).to(receiver['to']).subject(receiver['subject']).content(modified_content) \
		.attach(attachment1) \
		.attach(attachment2) \
		.attach(attachment3) \
		.attach(attachment4) \
		.attach(attachment5) \
		.attach(attachment6) \
		.attach(attachment7) \
		.build()
	print('Finish the creating a mail!!\n')

	if _debug_log:
		print(mail.CreateMail())

	Mailer().send_mail(mail)
	print('Welcome to use my application :)')


if __name__ == '__main__':
	main()
