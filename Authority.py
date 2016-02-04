""" Created by Jieyi on 2/5/16. """
import smtplib

uid = 'sample@msn.com'
pwd = 'sample'


class Authority:
	"""
	Authority decorator.
	"""

	def __init__(self, id, pwd):
		self.__id = id
		self.__pwd = pwd

	def __call__(self, f):
		def wrapper(*args, **kwargs):
			res = None
			self.__s = self.login()
			if self.__s is not None:
				res = f(self, self.__s, args[-1])
			self.logout()
			return res

		return wrapper

	def login(self):
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

	def logout(self):
		self.__service.quit()


class Mailer:
	@Authority(uid, pwd)
	def sendMail(self, service, mail):
		self.__content = mail.CreateMail()
		service.sendmail(self.__content['From'], self.__content['To'], self.__content.as_string())


def main():
	print()


if __name__ == '__main__':
	main()
