import pytest
from selenium.webdriver.common.by import By
from pages.auth import Registration
from config import valid_email, valid_password
import time


class TestRegistration:

    @pytest.mark.reg
    @pytest.mark.positive
    def test_get_registration_valid(self, browser):

        """ Валидный вариант регистрации при использовании email и получения кода для входа на почту. """

        page = Registration(browser)
        page.enter_reg_page()
        browser.implicitly_wait(2)
        assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

        page = Registration(browser)

        page.enter_firstname(self.first_name)
        browser.implicitly_wait(5)

        page.enter_lastname(self.last_name)
        browser.implicitly_wait(5)

        page.enter_email(valid_email)
        browser.implicitly_wait(3)

        page.enter_password(valid_password)
        browser.implicitly_wait(3)

        page.enter_pass_conf(valid_password)
        browser.implicitly_wait(3)

        page.btn_click()
        time.sleep(30)

        """Проверяем почтовый ящик на наличие писем и достаём ID последнего письма"""
        result_id, status_id = Registration().get_id_letter(valid_email)

        id_letter = result_id[0].get('id')

        assert status_id == 200
        assert id_letter > 0

        """Получаем код регистрации из письма от Ростелекома"""
        result_code, status_code = Registration().get_reg_code(valid_email, str(id_letter))

        text_body = result_code.get('body')

        reg_code = text_body[text_body.find('Ваш код : ') + len('Ваш код : '):
                             text_body.find('Ваш код : ') + len('Ваш код : ') + 6]

        assert status_code == 200
        assert reg_code != ''

        reg_digit = [int(char) for char in reg_code]
        browser.implicitly_wait(30)
        for i in range(0, 6):
            browser.find_elements(By.XPATH, '//input[@inputmode="numeric"]')[i].send_keys(reg_code[i])
            browser.implicitly_wait(5)
        browser.implicitly_wait(30)

        """Проверяем, что регистрация пройдена и пользователь перенаправлен в личный кабинет"""
        assert page.get_relative_link() == '/account_b2c/page'
        page.driver.save_screenshot('reg_done.png')

        """В случае успешной регистрации, перезаписываем созданные пару email/пароль в файл settings"""
        page.driver.save_screenshot('reg_done.png')
        print(valid_email, valid_password)
        with open(r"../pages/Settings.py", 'r', encoding='utf8') as file:
            lines = []
            print(lines)
            for line in file.readlines():
                if 'valid_email' in line:
                    lines.append(f"valid_email = '{str(valid_email)}'\n")
                elif 'valid_pass_reg' in line:
                    lines.append(f"valid_pass_reg = '{valid_password}'\n")
                else:
                    lines.append(line)
        with open(r"../pages/Settings.py", 'w', encoding='utf8') as file:
            file.writelines(lines)