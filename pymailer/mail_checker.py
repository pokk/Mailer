""" Created by Jieyi on 4/4/16. """
from abc import ABCMeta, abstractmethod

from internet import InternetStatus


class Checker(metaclass=ABCMeta):
    def __init__(self, condition=None, checker=None):
        self._gui = None
        self._condition = condition
        self.__next_checker = checker

    def do_something(self):
        if self._is_my_responsibility():
            msg = self._error_action()
            return False, msg
        else:
            return self.__next_checker.do_something() if self.__next_checker else (True, 'Perfect!! passing all of checking.\n\n')

    def set_checker(self, checker):
        self.__next_checker = checker

    @abstractmethod
    def _error_action(self):
        pass

    @abstractmethod
    def _is_my_responsibility(self):
        pass


class CheckChangeAttachmentLanguage(Checker):
    """
    Change the attachment language.
    """

    def _error_action(self):
        return '** Please check your attachments are correct...'

    def _is_my_responsibility(self):
        # TODO: .
        return False


class CheckSelectLanguage(Checker):
    """
    Checking selection is selected.
    """

    def _error_action(self):
        return '** Please select a language, thanks! ;)'

    def _is_my_responsibility(self):
        return self._condition is 0


class CheckInputReceiver(Checker):
    """
    Checking inputting the receiver name.
    """

    def _error_action(self):
        return "** Please don't forget to input receiver name. ^_^"

    def _is_my_responsibility(self):
        return not self._condition


class CheckInternet(Checker):
    """
    Checking Internet is available.
    """

    def _error_action(self):
        return '** Please check your internet state.'

    def _is_my_responsibility(self):
        # Because Internet is connected, this is not this responsibility.
        return not InternetStatus().is_internet_connect()


class CheckModifyContentTitle(Checker):
    """
    Checking the content is including modifiable title.
    """

    def _error_action(self):
        return '** Please check your content key word.'

    def _is_my_responsibility(self):
        content, content_title = self._condition
        for title in content_title:
            if title not in content:
                print('Please modify to this key word "%s".' % title)
                return True

        return False


def main():
    print("hello world")


if __name__ == '__main__':
    main()
