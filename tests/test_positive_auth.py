import pytest
from pages.auth import Authorization
from pages.locators import AuthLocators
from config import valid_phone, valid_login, valid_password, valid_email

@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.xfail
@pytest.mark.parametrize('username', [valid_phone, valid_email, valid_login],
                         ids=['phone', 'email', 'login'])
def test_active_tab(browser, username):
    """ Проверка автоматического переключения табов тел/почта/логин/лицевой счет """
    page = Authorization(browser)
    page.enter_username(username)
    page.enter_password(valid_password)
    if username == valid_phone:
        assert browser.find_element(AuthLocators.AUTH_ACTIVE_TAB).text == 'Телефон'
    elif username == valid_email:
        assert browser.find_element(AuthLocators.AUTH_ACTIVE_TAB).text == 'Почта'
    elif username == valid_login:
        assert browser.find_element(AuthLocators.AUTH_ACTIVE_TAB).text == 'Логин'
    else:
        assert browser.find_element(AuthLocators.AUTH_ACTIVE_TAB).text == 'Лицевой счет'


@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.parametrize('username', [valid_phone, valid_login],
                         ids=['valid phone', 'valid login'])
def test_auth_page_phone_login_valid(browser, username):
    """ Проверка авторизации по номеру телефона/логину и паролю + проверка
    автоматического переключения табов тел/логин """
    page = Authorization(browser)
    page.enter_username(username)
    page.enter_password(valid_password)
    page.btn_click_enter()

    assert page.get_relative_link() == '/account_b2c/page'


@pytest.mark.auth
@pytest.mark.positive
def test_auth_page_email_valid(browser):
    """ Проверка авторизации по почте и паролю """
    page = Authorization(browser)
    page.enter_username(valid_email)
    page.enter_password(valid_password)
    page.btn_click_enter()
    page.driver.save_screenshot('auth_by_email.png')

    assert page.get_relative_link() == '/account_b2c/page'


@pytest.mark.reg
@pytest.mark.positive
def test_reg_page_open(browser):
    """ Проверка страницы регистрации """
    page = Authorization(browser)
    page.enter_reg_page()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'