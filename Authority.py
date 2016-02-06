""" Created by Jieyi on 2/5/16. """
import smtplib

from IoOperation import FileOperator

_debug_log = False
# For decorator's parameter.
user = FileOperator().open_json_file('user.json')


class Authority:
	"""
	Authority decorator.
	"""

	def __init__(self, uid, pwd):
		self.__id = uid
		self.__pwd = pwd

	def __call__(self, f):
		def wrapper(*args, **kwargs):
			res = None
			self.__s = self._login()
			if self.__s is not None:
				res = f(self, self.__s, args[-1])
			self._logout()
			return res

		return wrapper

	def _login(self):
		try:
			self.__service = smtplib.SMTP('smtp.live.com', 587)
			self.__service.ehlo()
			self.__service.starttls()
			self.__service.ehlo()
			self.__service.login(self.__id, self.__pwd)
		except Exception as e:
			print(str(e))
			return None

		return self.__service

	def _logout(self):
		self.__service.quit()


class Mailer:
	@Authority(user['uid'], user['pwd'])
	def send_mail(self, service, mail):
		mail_info = mail.create_mail()
		service.sendmail(mail_info['From'], mail_info['To'], mail_info.as_string())


# Testing code
def main():
	print()


if __name__ == '__main__':
	main()
