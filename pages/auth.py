from base import WebPage
from locators import RegLocators, AuthLocators, PassRecoveryLocators
import time, os


class Registration(WebPage):
    def __init__(self, webdriver, timeout=10):
        super().__init__(webdriver, timeout)
        self.first_name = webdriver.find_element(RegLocators.REG_FIRSTNAME)
        self.last_name = webdriver.find_element(RegLocators.REG_LASTNAME)
        self.email = webdriver.find_element(RegLocators.REG_ADDRESS)
        self.password = webdriver.find_element(RegLocators.REG_PASSWORD)
        self.confirm = webdriver.find_element(RegLocators.REG_PASS_CONFIRM)
        self.reg_button = webdriver.find_element(RegLocators.REG_REGISTER)

    def firstname(self, value):
        self.first_name.send_keys(value)

    def lastname(self, value):
        self.last_name.send_keys(value)

    def email(self, value):
        self.email.send_keys(value)

    def password(self, value):
        self.password.send_keys(value)

    def confirm(self, value):
        self.confirm.send_keys(value)

    def reg_button(self):
        self.reg_button.click()


class Authorization(WebPage):
    def __init__(self, webdriver, timeout=10):
        super().__init__(webdriver, timeout)
        url = os.getenv('MAIN_URL') or 'https://b2c.passport.rt.ru'
        webdriver.get(url)
        self.username = webdriver.find_element(AuthLocators.AUTH_USERNAME)
        self.password = webdriver.find_element(AuthLocators.AUTH_PASS)
        self.auth_button = webdriver.find_element(AuthLocators.AUTH_BTN)
        self.reg_in = webdriver.find_element(AuthLocators.AUTH_REG_IN)

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def button_click_enter(self):
        self.auth_button.click()
        time.sleep(10)

    def enter_reg_page(self):
        self.reg_in.click()
        time.sleep(10)


class PassRecoveryPage(WebPage):
    def __init__(self, webdriver, timeout=10):
        super().__init__(webdriver, timeout)
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials'
        webdriver.get(url)
        self.username = webdriver.find_element(PassRecoveryLocators.NEWPASS_ADDRESS)
        self.button_cont = webdriver.find_element(PassRecoveryLocators.NEWPASS_CONTINUE)

    def new_username(self, value):
        self.username.send_keys(value)

    def button_continue(self):
        self.button_cont.click()
        time.sleep(10)