""" Created by Jieyi on 2/5/16. """
import smtplib


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
            print('Try to login to your mail server...')
            self.__s = self._login()
            if not self.__s:
                print('** Login was failed!!! :(\n')
                return res

            print('Login was successful!!\n')
            # Here parameters will send to the decoratee.
            # 'args[0]' must be decoratee itself(class object).
            res = f(*args, self.__s)

            # After operation action, auto logout.
            print('Logout your mail server...')
            self._logout()
            print('Logout!!\n')
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
        pass


# Testing code
def main():
    pass


if __name__ == '__main__':
    main()
