""" Created by Jieyi on 2/5/16. """
import json
from pprint import pprint

_debug_log = False


class FileManager:
	"""
	File decorator.
	"""

	def __init__(self, f):
		self.__file = None
		self.__f = f

	def __call__(self, filename=''):
		self._open_file(filename)
		res = self.__f(self, self.__file)
		self._close_file()
		return res

	def _open_file(self, filename):
		self.__file = open(filename)

	def _close_file(self):
		self.__file.close()


class FileOperator:
	@FileManager
	def open_json_file(self, file_name):
		data = json.load(file_name)
		if _debug_log:
			pprint(data)

		return data


# Testing code.
def main():
	FileOperator().open_json_file('user.json')
	print("hello world")


if __name__ == '__main__':
	main()
