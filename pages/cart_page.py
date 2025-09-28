from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure


class CartPage(Base):

    # Locators

    product_1_name_cart = "(//a[@class='BAcw7'])[1]"
    product_1_price_cart = "(//span[@aria-label='Текущая цена продукта'])[1]"
    sum_products_cart = "//strong[@class='_2nMVY']"

    navigation_to_checkout_button = "//button[@class='_2eEQG _2xhLm _3sJhC _3aV4_ _3EhDt']"
    delivery_method_assert_title = "//p[contains(text(), 'Способ получения')]"

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
