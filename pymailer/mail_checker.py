""" Created by Jieyi on 4/4/16. """
from abc import ABCMeta, abstractmethod
from tkinter import END


class Checker(metaclass=ABCMeta):
    def __init__(self, gui, checker=None):
        self.__gui = gui
        self.__next_checker = checker

    def do_something(self):
        if self._is_my_responsibility():
            self._my_action()
            return False
        else:
            print(self)
            if self.__next_checker:
                self.__next_checker.do_something()
            else:
                return True

    @abstractmethod
    def _my_action(self):
        pass

    @abstractmethod
    def _is_my_responsibility(self):
        pass


class CheckChangeAttachmentLanguage(Checker):
    def _my_action(self):
        self.__gui.log_msg_text.insert(END, '\n** Please check your attachments is correct...\n\n')

    def _is_my_responsibility(self):
        return not self.__gui.change_attachment_lang()


class CheckSelectLanguage(Checker):
    def _my_action(self):
        self.__gui.log_msg_text.insert(END, '\n** Please select a language, thanks! ;)\n\n')

    def _is_my_responsibility(self):
        return self.__gui.url_lang_combobox.current() is 0


class CheckInputReceiver(Checker):
    def _my_action(self):
        self.__gui.log_msg_text.insert(END, "\n** Please don't forget to input receiver name. ^_^\n\n")

    def _is_my_responsibility(self):
        return self.__gui.is_input_receiver()


class CheckInternet(Checker):
    def _my_action(self):
        self.__gui.log_msg_text.insert(END, '\n** Please check your internet state.\n\n')

    def _is_my_responsibility(self):
        return not self.__gui.is_internet()


class CheckModifyContent(Checker):
    def _my_action(self):
        self.__gui.log_msg_text.insert(END, '\n** Please check your content key word.\n\n')

    def _is_my_responsibility(self):
        return not self.__gui.modify_content_link(self.__gui.url_lang_link.get(self.__gui.url_lang_combobox_str.get()))


def main():
    print("hello world")


if __name__ == '__main__':
    main()
