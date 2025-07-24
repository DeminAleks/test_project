from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product_1_name_cart = "//*[@id='__next']/main/section/div/div[2]/div[1]/div/div/span/div/div/div[1]/div[1]/a"
    product_1_price_cart = "//*[@id='__next']/main/section/div/div[2]/div[1]/div/div/span/div/div/div[1]/p/span"
    sum_products_cart = "//*[@id='__next']/main/section/div/div[2]/div[2]/div/div[2]/div[2]/strong"

    navigation_to_checkout_button = "//*[@id='__next']/main/section/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/button"
    delivery_method_assert_title = "//*[@id='__next']/main/div/div[2]/div/div[1]/p"

    # Getters

    def get_product_1_name_cart(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_name_cart)))
        return element.text.strip()

    def get_product_1_price_cart(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price_cart)))
        return element.text.replace("₽", "").replace(" ", "").strip()

    def get_sum_products_cart(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sum_products_cart)))
        return element.text.replace("₽", "").replace(" ", "").strip()

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.navigation_to_checkout_button)))

    def get_delivery_method_assert_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_method_assert_title)))

    # Actions

    def click_navigation_to_checkout_button(self):
        element = self.get_checkout_button()
        print(f'Click "{element.text.strip()}" button')
        element.click()

    # Methods

    def assert_product_1_name_cart(self, expected_name):
        with allure.step("Assertion of Product 1 name in Cart"):
            Logger.add_start_step(method="assert_product_1_name_cart")
            actual_name_cart = self.get_product_1_name_cart()
            self.assert_product_details(expected_name, actual_name_cart, label="Product name")
            Logger.add_end_step(url=self.driver.current_url, method="assert_product_1_name_cart")

    def assert_product_1_price_cart(self, expected_price):
        with allure.step("Assertion of Product 1 price in Cart"):
            Logger.add_start_step(method="assert_product_1_price_cart")
            actual_price_cart = self.get_product_1_price_cart()
            self.assert_product_details(expected_price, actual_price_cart, label="Product price")
            Logger.add_end_step(url=self.driver.current_url, method="assert_product_1_price_cart")

    def assert_sum_products_cart(self, expected_sum):
        with allure.step("Assertion of Sum of products in Cart"):
            Logger.add_start_step(method="assert_sum_products_cart")
            actual_sum_cart = self.get_sum_products_cart()
            self.assert_product_details(expected_sum, actual_sum_cart, label="Sum of products in Cart")
            Logger.add_end_step(url=self.driver.current_url, method="assert_sum_products_cart")

    def navigation_to_checkout(self):
        with allure.step("Navigation to Checkout"):
            Logger.add_start_step(method="navigation_to_checkout")
            self.get_current_url()
            self.click_navigation_to_checkout_button()
            self.assert_word(self.get_delivery_method_assert_title(), "Способ получения")
            Logger.add_end_step(url=self.driver.current_url, method="navigation_to_checkout")
