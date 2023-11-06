from config import URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebPage:
    def __init__(self, webdriver, timeout=10):
        self.driver = webdriver
        self.base_url = URL
        self.driver.implicitly_wait(timeout)

    def get(self):
        """ Данный метод осуществляет переход на начальную страницу. """

        return self.driver.get(self.base_url)

    def go_back(self):
        """ Данный метод осуществляет возврат на начальную страницу. """

        return self.driver.back(self.base_url)

    def refresh(self):
        """ Данный метод обновляет страницу. """

        return self.driver.refresh(self.base_url)

    def screenshot(self, file_name='screenshot.png'):
        """ Данный метод делает скриншот страницы. """

        return self.driver.save_screenshot(file_name)

    def scroll_down(self, offset=0):
        """ Данный метод прокручивает страницу вниз. """

        if offset:
            self.driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset=0):
        """ Данный метод прокручивает страницу вверх. """

        if offset:
            self.driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self.driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def find_element(self, locator, time=10):
        """ Данный метод производит поиск одного элемента на странице. """

        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Не найден {locator}')

    def find_many_elements(self, locator, time=10):
        """ Данный метод производит поиск нескольких элементов на странице. """

        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Не найден {locator}')

    def find_element_until_to_be_clickable(self, locator, time=10):
        """ Данный метод производит поиск элемента пока он остается кликабельным. """

        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Элемент страницы не кликабелен!')