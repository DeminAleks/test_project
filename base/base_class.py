import os
import datetime
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver
        self.faker = Faker("ru_RU")

    """Method screenshot"""

    def get_screenshot(self):
        date_folder = datetime.now().strftime("%d.%m.%Y")
        time_stamp = datetime.now().strftime("%d.%m.%Y-%H.%M.%S")
        name_screenshot = f'Screenshot_{time_stamp}.png'
        base_dir = 'C:\\Users\\Alexander_Demin\\PycharmProjects\\pythonTestProject\\screenshots'
        folder_path = os.path.join(base_dir, date_folder)
        os.makedirs(folder_path, exist_ok=True)
        full_path = os.path.join(folder_path, name_screenshot)
        self.driver.save_screenshot(full_path)
        print(f"Screenshot saved")

    """Method scroll to element"""
    def scroll_to_element(self, element, offset=180):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script(f"window.scrollBy(0, -{offset});")

    """Method hold and move element"""
    def hold_and_move_element(self, element, offset_x, offset_y=0):
        actions = ActionChains(self.driver)
        actions.click_and_hold(element).move_by_offset(offset_x, offset_y).release().perform()

    """Method get current url"""
    def get_current_url(self):
        get_url = str(self.driver.current_url).strip()
        print(f'Current url: "{get_url}"')

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = str(word.text).strip()
        expected_result = str(result).strip()
        assert value_word == expected_result, f'Assertion failed:\nExpected: "{expected_result}"\nActual: "{value_word}"'
        print(f'Assert word is correct: "{value_word}"')

    """Method assert product details"""

    def assert_product_details(self, expected_value, actual_value, label):
        assert expected_value == actual_value, f"Assertion for {label} failed.\nExpected: '{expected_value}'\nActual: '{actual_value}'"
        print(f'Assert for "{label}" is correct')

    """Method assert url"""

    def assert_url(self, result):
        get_url = str(self.driver.current_url).strip()
        expected_url = str(result).strip()
        assert get_url == expected_url, f'Assertion failed:\nExpected URL: "{expected_url}"\nActual URL: "{get_url}"'
        print(f'Assert URL is correct: "{get_url}"')

    """Method wait url"""

    def wait_for_url_to_be(self, expected_url):
        expected_url = str(expected_url).strip()
        try:
            WebDriverWait(self.driver, 30).until(EC.url_to_be(expected_url))
            print(f'Assertion URL success: "{expected_url}"')
        except TimeoutException:
            current_url = self.driver.current_url
            raise AssertionError(
                f'Expected URL: "{expected_url}"\n'
                f'Current URL: "{current_url}"'
            )

    """Method contains url"""

    def wait_for_url_contains(self, partial_url):
        partial_url = str(partial_url).strip()
        try:
            WebDriverWait(self.driver, 30).until(EC.url_contains(partial_url))
            print(f'Assertion URL success: "{partial_url}"')
        except TimeoutException:
            current_url = self.driver.current_url
            raise AssertionError(
                f'Expected URL: "{partial_url}"\n'
                f'Current URL: "{current_url}"'
            )

    """Method verify checkbox is selected"""
    def checkbox_is_selected_status(self, wrapper):
        checkbox_status = wrapper.find_element(By.TAG_NAME, "input")
        checkbox_name = wrapper.text.strip().capitalize()
        if checkbox_status.is_selected():
            print(f'Сheckbox "{checkbox_name}" is selected')
        else:
            print(f'Сheckbox "{checkbox_name}" is not selected')
