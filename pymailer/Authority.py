""" Created by Jieyi on 2/5/16. """
import os
import smtplib

from IoOperation import FileOperator
from Mail import MailBuilder

_debug_log = False
# For decorator's parameter.
user = FileOperator().open_json_file(os.path.abspath(os.pardir) + '/user.json')


# Decorator.
class Authority:
	"""
	Authority decorator. Including login and logout's fixed actions.
	"""

	def __init__(self, uid, pwd, mail_service_ip):
		self.__id = uid
		self.__pwd = pwd
		self.__mail_service_ip = mail_service_ip

	def __call__(self, f):
		def wrapper(*args, **kwargs):
			# '*args' parameters are gotten by caller.
			res = None

			# If login is successful, get the service object.
			print('Try to login to your mail server...')
			self.__s = self._login()
			print('Login is successful!!\n')

			if self.__s is not None:
				# Here parameters will send to the decoratee.
				res = f(args[0], args[1], self.__s)

			# After operation action, auto logout.
			print('Logout your mail server...')
			self._logout()
			print('Logout!!\n')
			return res

		return wrapper

	# Login to server.
	def _login(self):
		try:
			self.__service = smtplib.SMTP(self.__mail_service_ip, 587)
			self.__service.ehlo()
			self.__service.starttls()
			self.__service.ehlo()
			self.__service.login(self.__id, self.__pwd)
		except Exception as e:
			print(str(e))
			return None

		return self.__service

	# Logout from server.
	def _logout(self):
		self.__service.quit()


class Mailer:
	"""
	We collate all of mail operations here.
	As like 'send', delete, ...
	"""

	# Send a mail to someone through which mail service.
	@Authority(user['uid'], user['pwd'], user['server'])
	def send_mail(self, mail, mail_server):
		print('Combining all of the information to a mail...')
		mail_info = mail.create_mail()
		print('Finish combining!!\n')

		if _debug_log:
			print(mail_info)

		print('Start to send the mail...')
		mail_server.sendmail(mail_info['From'], mail_info['To'], mail_info.as_string())
		print('Finished sending!!\n')


# Testing code
def main():
	mail = MailBuilder().uid(user['uid']).to('sample@google.com').subject('Hello world').content('Oh, just testing!!').build()
	# 'mail' parameter will send to Authority decorator's __call__.
	Mailer().send_mail(mail)


if __name__ == '__main__':
	main()
