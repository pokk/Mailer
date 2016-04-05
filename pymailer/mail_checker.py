""" Created by Jieyi on 4/4/16. """
from abc import ABCMeta, abstractmethod
from tkinter import END

from __init__ import attachment_list, atta_lang_list, debug_log
from internet import InternetStatus
from mailer import Mailer


class Checker(metaclass=ABCMeta):
    def __init__(self, gui, checker=None):
        self._gui = gui
        self.__next_checker = checker

    def do_something(self):
        if self._is_my_responsibility():
            self._my_action()
            return False
        else:
            return self.__next_checker.do_something() if self.__next_checker else True

    @abstractmethod
    def _my_action(self):
        pass

    @abstractmethod
    def _is_my_responsibility(self):
        pass


class CheckChangeAttachmentLanguage(Checker):
    """
    Change the attachment language.
    """

    def _my_action(self):
        self._gui.log_msg_text.insert(END, '\n** Please check your attachments is correct...\n\n')

    def _is_my_responsibility(self):
        self._gui.mail_attachment_list = attachment_list[:]  # Clone a list.
        if atta_lang_list[self._gui.url_lang_combobox.current()]:  # Choose the index from atta_lang_list.
            for i in range(len(self._gui.mail_attachment_list)):
                # Only after the third file can change language.
                if i > 2:
                    # Modify the file name.
                    att = self._gui.mail_attachment_list[i].split('.')
                    self._gui.mail_attachment_list[i] = ''.join([' ', atta_lang_list[self._gui.url_lang_combobox.current()], '.']).join(att)

        # ** IMPORTANT, we have to new an object here. Otherwise, we couldn't check the error checking.
        self._gui._mailer = Mailer(self._gui.mail_attachment_list)
        if debug_log:
            print(self._gui.mail_attachment_list)

        return False


class CheckSelectLanguage(Checker):
    """
    Checking selection is selected.
    """

    def _my_action(self):
        self._gui.log_msg_text.insert(END, '\n** Please select a language, thanks! ;)\n\n')

    def _is_my_responsibility(self):
        return self._gui.url_lang_combobox.current() is 0


class CheckInputReceiver(Checker):
    """
    Didn't input the receiver name.
    """

    def _my_action(self):
        self._gui.log_msg_text.insert(END, "\n** Please don't forget to input receiver name. ^_^\n\n")

    def _is_my_responsibility(self):
        return not self._gui.receiver_name_field.get()


class CheckInternet(Checker):
    """
    The internet is not available.
    """

    def _my_action(self):
        self._gui.log_msg_text.insert(END, '\n** Please check your internet state.\n\n')

    def _is_my_responsibility(self):
        self._gui.log_msg_text.insert(END, 'Checking the internet...\n')
        # Check the internet is available or not.
        if not InternetStatus().is_internet_connect():
            # If the internet is not connected, we will quit the process.
            self._gui.log_msg_text.insert(END, 'No internet connect!!\n')
            return True
        self._gui.log_msg_text.insert(END, 'Internet is ok!\n\n')
        return False


class CheckModifyContent(Checker):
    """
    Modify the content link depends on the language you selected. 
    """

    def _my_action(self):
        self._gui.log_msg_text.insert(END, '\n** Please check your content key word.\n\n')

    def _is_my_responsibility(self):
        link_arr = self._gui.url_lang_link.get(self._gui.url_lang_combobox_str.get())
        content = self._gui._mailer.content
        for index in range(len(link_arr)):
            try:
                content_index = content.index(self._gui.url_lang_link_title[index]) + len(self._gui.url_lang_link_title[index])
                content = content[:content_index] + '\n' + link_arr[index] + content[content_index:]
            except ValueError as ve:
                self._gui.log_msg_text.insert(END, self._gui.url_lang_link_title[index] + ' ' + str(ve) + '\n')
                return True

        self._gui._mailer.content = content
        return False


def main():
    print("hello world")


if __name__ == '__main__':
    main()
