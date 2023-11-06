import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Chrome(executable_path='ChromeDriver.exe')

    yield driver
    driver.quit()