""" Created by Jieyi on 2/5/16. """
import json
from pprint import pprint

_debug_log = False


class FileOperator:
	"""
	All of the operations for file will be here.
	"""

	@FileManager
	def open_json_file(self, opened_file):
		if _debug_log:
			print(opened_file)

		data = json.load(opened_file)

		if _debug_log:
			pprint(data)

		return data


# Decorator.
class FileManager:
	"""
	File decorator. Including open and close file's fixed actions.
	"""

	def __init__(self, fun):
		self.__opened_file = None
		self.__fun = fun

	def __call__(self, file_name):
		self._open_file(file_name)
		# Here is executing the decoratee's action.
		res = self.__fun(self.__fun, self.__opened_file)
		self._close_file()
		return res

	def _open_file(self, file_name):
		self.__opened_file = open(file_name)

	def _close_file(self):
		self.__opened_file.close()


# Testing code.
def main():
	d = FileOperator().open_json_file('user.json')
	print('%s\n%s' % (d['uid'], d['pwd']))


if __name__ == '__main__':
	main()
