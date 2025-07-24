from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure


class ProductListingPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    sort_button = "//*[@id='category-sort_wrapper']"
    sort_ascending_button = "//*[@id='oASC price']"

    filter_plp_level_3_link = "//*[@id='__next']/main/div/div[3]/div[1]/div[1]/ul/li[1]/a"
    filter_delivery_checkbox = "//*[@id='__next']/main/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/span[1]/div/label"
    filter_brand_checkbox = "//*[@id='__next']/main/div/div[2]/div[1]/div[2]/div/div[2]/div[4]/div[2]/span[1]/div/label"
    filter_price_slider_min_value = "//*[@id='__next']/main/div/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div/div/div[1]"
    filter_price_slider_max_value = "//*[@id='__next']/main/div/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div/div/div[2]"
    filter_price_apply_button = "//*[@id='__next']/main/div/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[2]/button"

    product_1_name_plp = "//*[@id='__next']/main/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/p/a"
    product_1_price_plp = "//*[@id='__next']/main/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/span[1]"

    add_to_cart_product_1_button = "//*[@id='__next']/main/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/button"
    cart_icon = "//*[@id='__next']/header/div[3]/div/div[4]/ul/li[5]/a"
    cart_assert_title = "//*[@id='__next']/main/section/div/div[1]/div/div/h1"

    # Getters

    def get_sort_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_button)))

    def get_sort_ascending_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_ascending_button)))

    def get_filter_plp_level_3_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_plp_level_3_link)))

    def get_filter_delivery_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_delivery_checkbox)))

    def get_filter_brand_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_brand_checkbox)))

    def get_filter_price_slider_min_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_slider_min_value)))

    def get_filter_price_slider_max_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_slider_max_value)))

    def get_filter_price_apply_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_price_apply_button)))

    def get_add_to_cart_product_1_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_1_button)))

    def get_product_1_name_plp(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_name_plp)))
        return element.text.strip()

    def get_product_1_price_plp(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price_plp)))
        return element.text.replace("₽", "").replace(" ", "").strip()

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_icon)))

    def get_cart_assert_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_assert_title)))

    # Actions

    def click_sort_button(self):
        self.get_sort_button().click()
        print('Click "Sort" button')

    def click_sort_ascending_button(self):
        element = self.get_sort_ascending_button()
        print(f'Apply Sort: "{element.text.strip()}"')
        element.click()

    def click_filter_plp_level_3_link(self):
        element = self.get_filter_plp_level_3_link()
        print(f'Apply Filter: "{element.text.strip()}"')
        element.click()

    def click_filter_delivery_checkbox(self):
        element = self.get_filter_delivery_checkbox()
        print(f'Apply Filter: "{element.text.strip()}"')
        element.click()

    def click_filter_brand_checkbox(self):
        element = self.get_filter_brand_checkbox()
        print(f'Apply Filter: "{element.text.strip()}"')
        element.click()

    def set_filter_price_min_slider(self):
        min_slider = self.get_filter_price_slider_min_value()
        self.hold_and_move_element(min_slider, 40)
        print("Set Filter: Min price")

    def set_filter_price_max_slider(self):
        max_slider = self.get_filter_price_slider_max_value()
        self.hold_and_move_element(max_slider, -80)
        print("Set Filter: Max price")

    def click_filter_price_apply_button(self):
        self.get_filter_price_apply_button().click()
        print("Apply Filter: Price")

    def click_add_to_cart_product_1_button(self):
        self.scroll_to_element(self.get_sort_button())
        element = self.get_add_to_cart_product_1_button()
        print(f'Click "{element.text.strip()}" button for product 1')
        element.click()

    def click_cart_icon(self):
        self.get_cart_icon().click()
        print('Click "Cart" icon')

    # Methods

    def apply_sort(self):
        with allure.step("Apply Sort"):
            Logger.add_start_step(method="apply_sort")
            self.get_current_url()
            self.click_sort_button()
            self.click_sort_ascending_button()
            self.wait_for_url_contains("sortKey=price&sortDirection=ASC")
            Logger.add_end_step(url=self.driver.current_url, method="apply_sort")

    def apply_filter_plp_level_3(self):
        with allure.step("Apply Filter: PLP level 3"):
            Logger.add_start_step(method="apply_filter_plp_level_3")
            self.scroll_to_element(self.get_filter_plp_level_3_link())
            self.click_filter_plp_level_3_link()
            self.wait_for_url_contains("gazonokosilki")
            Logger.add_end_step(url=self.driver.current_url, method="apply_filter_plp_level_3")

    def apply_filter_delivery(self):
        with allure.step("Apply Filter: Delivery"):
            Logger.add_start_step(method="apply_filter_delivery")
            self.scroll_to_element(self.get_filter_delivery_checkbox())
            self.click_filter_delivery_checkbox()
            self.checkbox_is_selected_status(self.get_filter_delivery_checkbox())
            self.wait_for_url_contains("shipping_available_by:")
            Logger.add_end_step(url=self.driver.current_url, method="apply_filter_delivery")

    def apply_filter_brand(self):
        with allure.step("Apply Filter: Brand"):
            Logger.add_start_step(method="apply_filter_brand")
            self.scroll_to_element(self.get_filter_brand_checkbox())
            self.click_filter_brand_checkbox()
            self.checkbox_is_selected_status(self.get_filter_brand_checkbox())
            self.wait_for_url_contains("brand:")
            Logger.add_end_step(url=self.driver.current_url, method="apply_filter_brand")

    def apply_filter_price(self):
        with allure.step("Apply Filter: Price"):
            Logger.add_start_step(method="apply_filter_price")
            self.scroll_to_element(self.get_filter_price_slider_min_value())
            self.set_filter_price_min_slider()
            self.set_filter_price_max_slider()
            self.click_filter_price_apply_button()
            self.wait_for_url_contains("price:")
            Logger.add_end_step(url=self.driver.current_url, method="apply_filter_price")

    def click_add_to_cart_product_1(self):
        with allure.step("Click Add to cart Product 1 button"):
            Logger.add_start_step(method="click_add_to_cart_product_1")
            self.scroll_to_element(self.get_add_to_cart_product_1_button())
            self.click_add_to_cart_product_1_button()
            self.click_cart_icon()
            self.assert_word(self.get_cart_assert_title(), "Корзина")
            Logger.add_end_step(url=self.driver.current_url, method="click_add_to_cart_product_1")
