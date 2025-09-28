from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure


class OrderPage(Base):

    # Locators

    sum_products_order = "//strong[@class='_2nMVY']"
    product_1_name_order = "//span[@class='QvxB4']"
    full_delivery_address_order = "(//p[@class='kfrjR'])[1]"
    full_personal_data_order = "(//p[@class='kfrjR'])[2]"
    full_delivery_details_order = "(//p[@class='kfrjR'])[3]"
    order_delivery_time = "//p[@class='_31ew1']"

    # Getters

    def get_sum_products_order(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sum_products_order)))
        return element.text.replace("₽", "").replace(" ", "").strip()

    def get_product_1_name_order(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_name_order)))
        return element.get_attribute("title").strip()

    def get_full_delivery_address_order(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_delivery_address_order)))
        return element.text.strip()

    def get_full_personal_data_order(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_personal_data_order)))
        return element.text.strip()

    def get_full_delivery_details_order(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_delivery_details_order)))
        return element.text.strip()

    def get_order_delivery_time(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_delivery_time)))
        return element.text.replace("Экспресс-доставка, ", "").strip()

    # Actions

    # Methods

    def assert_sum_products_order(self, expected_sum):
        with allure.step("Assert Sum products order"):
            Logger.add_start_step(method="assert_sum_products_order")
            self.get_current_url()
            actual_sum_checkout = self.get_sum_products_order()
            self.assert_product_details(expected_sum, actual_sum_checkout, label="Sum of products on Order page")
            Logger.add_end_step(url=self.driver.current_url, method="assert_sum_products_order")

    def assert_product_1_name_order(self, expected_name):
        with allure.step("Assertion of Product 1 name in Order"):
            Logger.add_start_step(method="assert_product_1_name_order")
            actual_product_1_name_checkout = self.get_product_1_name_order()
            self.assert_product_details(expected_name, actual_product_1_name_checkout, label="Product_1 name on Order page")
            Logger.add_end_step(url=self.driver.current_url, method="assert_product_1_name_order")

    def assert_full_delivery_address_order(self, expected_full_address):
        with allure.step("Assertion of Full Delivery address in Order"):
            Logger.add_start_step(method="assert_full_delivery_address_order")
            actual_full_address = self.get_full_delivery_address_order()
            self.assert_product_details(expected_full_address, actual_full_address, label="Full delivery address on Order page")
            Logger.add_end_step(url=self.driver.current_url, method="assert_full_delivery_address_order")

    def assert_full_personal_data_order(self, expected_full_personal_data):
        with allure.step("Assertion of Full Personal data in Order"):
            Logger.add_start_step(method="assert_full_personal_data_order")
            actual_full_personal_data = self.get_full_personal_data_order()
            self.assert_product_details(expected_full_personal_data, actual_full_personal_data, label="Full personal data on Order page")
            Logger.add_end_step(url=self.driver.current_url, method="assert_full_personal_data_order")

    def assert_full_delivery_details_order(self, expected_full_delivery_details):
        with allure.step("Assertion of Full Delivery details in Order"):
            Logger.add_start_step(method="assert_full_delivery_details_order")
            actual_full_delivery_details = self.get_full_delivery_details_order()
            self.assert_product_details(expected_full_delivery_details, actual_full_delivery_details, label="Full delivery details on Order page")
            Logger.add_end_step(url=self.driver.current_url, method="assert_full_delivery_details_order")

    def assert_delivery_time_order(self, expected_delivery_time):
        with allure.step("Assertion of Delivery time in Order"):
            Logger.add_start_step(method="assert_delivery_time_order")
            actual_delivery_time = self.get_order_delivery_time()
            self.assert_product_details(expected_delivery_time, actual_delivery_time, label="Delivery time on Order page")
            Logger.add_end_step(url=self.driver.current_url, method="assert_delivery_time_order")
