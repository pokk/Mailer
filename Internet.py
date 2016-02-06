""" Created by Jieyi on 2/5/16. """
import socket


class InternetStatus:
	def __init__(self):
		...

	@staticmethod
	def is_internet_connect():
		try:
			# see if we can resolve the host name -- tells us if there is
			# a DNS listening
			host = socket.gethostbyname('www.google.com')
			# connect to the host -- tells us if the host is actually
			# reachable
			s = socket.create_connection((host, 80), 2)
			return True
		except Exception as e:
			print('ERROR : %s' % e)
			return False


def main():
	print(InternetStatus().is_internet_connect())


if __name__ == '__main__':
	main()
