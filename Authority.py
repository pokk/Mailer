""" Created by Jieyi on 2/5/16. """
import smtplib

from IoOperation import FileOperator
from Mail import MailBuilder

_debug_log = False
# For decorator's parameter.
user = FileOperator().open_json_file('user.json')
mail_server_address = 'smtp.live.com'


class Mailer:
	"""
	We collate all of mail operations here.
	As like 'send', delete, ...
	"""

	# Send a mail to someone through which mail service.
	@Authority(user['uid'], user['pwd'], mail_server_address)
	def send_mail(self, mail, mail_server):
		mail_info = mail.create_mail()

		if _debug_log:
			print(mail_info)

		mail_server.sendmail(mail_info['From'], mail_info['To'], mail_info.as_string())


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
			self.__s = self._login()
			if self.__s is not None:
				# Here parameters will send to the decoratee.
				res = f(*args, self.__s, **kwargs)
			# After operation action, auto logout.
			self._logout()
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


# Testing code
def main():
	mail = MailBuilder().uid(user['uid']).to('sample@google.com').subject('Hello world').content('Oh, just testing!!').build()
	# 'mail' parameter will send to Authority decorator's __call__.
	Mailer().send_mail(mail)


if __name__ == '__main__':
	main()
