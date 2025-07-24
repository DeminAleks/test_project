import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()  # Отрабатывает для каждого модуля в тесте
def set_up():
    print("\nStart test")
    yield
    print("\nFinish test")


@pytest.fixture(scope="module")  # Отрабатывает для всего теста
def set_group():
    print("\nEnter system")
    yield
    print("\nExit system")
