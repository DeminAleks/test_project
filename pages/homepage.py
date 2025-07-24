from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure

class HomePage(Base):

    url = 'https://obi.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    close_cookies_button = "//*[@id='__next']/div[5]/div/button"
    plp_level_1_link = "//*[@id='__next']/header/div[4]/div/section/div/div/span[2]"
    plp_level_2_link = "//*[@id='__next']/main/div/div[1]/div/div/div[3]"

    # Getters

    def get_close_cookies_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_cookies_button)))

    def get_plp_level_1_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plp_level_1_link)))

    def get_plp_level_2_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plp_level_2_link)))

    # Actions

    def click_close_cookies_button(self):
        self.get_close_cookies_button().click()
        print('Click "Close Cookies banner" button')

    def click_plp_level_1_link(self):
        element = self.get_plp_level_1_link()
        print(f'Click "{element.text.strip()}" link')
        element.click()

    def click_plp_level_2_link(self):
        element = self.get_plp_level_2_link()
        print(f'Click "{element.text.strip()}" link')
        element.click()

    # Methods

    def opening_homepage(self):
        with allure.step("Opening Homepage"):
            Logger.add_start_step(method="opening_homepage")
            self.driver.get(self.url)
            self.get_current_url()
            self.click_close_cookies_button()
            self.assert_url("https://obi.ru/")
            Logger.add_end_step(url=self.driver.current_url, method="opening_homepage")

    def navigation_to_plp_level_1(self):
        with allure.step("Navigation to PLP level 1"):
            Logger.add_start_step(method="navigation_to_plp_level_1")
            self.get_current_url()
            self.click_plp_level_1_link()
            self.wait_for_url_to_be("https://obi.ru/sad-i-dosug")
            self.assert_url("https://obi.ru/sad-i-dosug")
            Logger.add_end_step(url=self.driver.current_url, method="navigation_to_plp_level_1")

    def navigation_to_plp_level_2(self):
        with allure.step("Navigation to PLP level 2"):
            Logger.add_start_step(method="navigation_to_plp_level_2")
            self.get_current_url()
            self.click_plp_level_2_link()
            self.wait_for_url_to_be("https://obi.ru/sad-i-dosug/sadovaja-tehnika")
            self.assert_url("https://obi.ru/sad-i-dosug/sadovaja-tehnika")
            Logger.add_end_step(url=self.driver.current_url, method="navigation_to_plp_level_2")
