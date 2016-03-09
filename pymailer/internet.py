""" Created by Jieyi on 2/5/16. """
import socket


class InternetStatus:
    def __init__(self):
        pass

    @staticmethod
    def is_internet_connect():
        try:
            # see if we can resolve the host name -- tells us if there is
            # a DNS listening
            host = socket.gethostbyname('www.google.com')
            # connect to the host -- tells us if the host is actually
            # reachable
            soc = socket.create_connection((host, 80), 2)
        except Exception as e:
            print('ERROR: %s' % e)
            return False
        return True


def main():
    print(InternetStatus().is_internet_connect())


if __name__ == '__main__':
    main()
