from selenium.webdriver.common.by import By


class RegLocators:

    REG_FIRSTNAME = (By.XPATH, "//input[@name='firstName']")
    REG_LASTNAME = (By.XPATH, "//input[@name='lastName']")
    REG_REGION = (By.XPATH, "//input[@autocomplete='new-password']"[0])
    REG_ADDRESS = (By.ID, 'address')
    REG_PASSWORD = (By.ID, 'password')
    REG_PASS_CONFIRM = (By.ID, 'password-confirm')
    REG_REGISTER = (By.XPATH, "//button[@name='register']")


class AuthLocators:

    AUTH_USERNAME = (By.ID, 'username')
    AUTH_PASS = (By.ID, 'password')
    AUTH_BTN = (By.ID, 'kc-login')
    AUTH_FORM_ERROR = (By.XPATH, "//span[@id='form-error-message']")
    AUTH_MESS_ERROR = (By.CSS_SELECTOR, '.rt-input-container__meta--error')
    AUTH_REG_IN = (By.ID, 'kc-register')
    AUTH_FORGOT_PASSWORD = (By.ID, 'forgot_password')


class PassRecoveryLocators:

    NEWPASS_ADDRESS = (By.ID, 'username')
    NEWPASS_CAPТCHA = (By.ID, 'captcha')
    NEWPASS_CONTINUE = (By.ID, 'reset')
    NEWPASS_ONETIME_CODE = (By.XPATH, '//input[@inputmode="numeric"]')
    NEWPASS_NEW_PASS = (By.ID, 'password-new')
    NEWPASS_NEW_PASS_CONFIRM = (By.ID, 'password-confirm')
    NEWPASS_BTN_SAVE = (By.ID, 't-btn-reset-pass')