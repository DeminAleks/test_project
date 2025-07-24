from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time
from utilities.logger import Logger
import allure


class ShippingPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    delivery_method_selector = "//*[@id='product-tabs']/ul/li[2]"
    delivery_method_selector_assert_title = "//*[@id='product-tabs']/div/div[1]/p[1]"

    address_field = "//*[@id='address-form-address-field-suggest']"
    select_address = "//*[@id='product-tabs']/div/div[1]/form/fieldset/div[1]/div[2]/div"

    apartment_field = "//*[@id='apartment']"
    floor_field = "//*[@id='floor']"
    entrance_field = "//*[@id='entrance']"
    express_delivery_toggle_1 = "//*[@id='product-tabs']/div/div[2]/div[2]/div/label"
    delivery_here_button = "//*[@id='product-tabs']/div/div[2]/div[1]/button[2]"
    delivery_details_assert_title = "//*[@id='__next']/main/div/div[2]/div/div[1]/div[1]/p"

    select_services_button = "//*[@id='__next']/main/div/div[2]/div/div[1]/div[2]/div[1]/button"
    services_assert_title = "//*[@id='html-body']/body/div[4]/div/div/div/p"
    by_lift_toggle = "//*[@id='product-tabs']/div[1]/div[1]/div[1]/label"
    apply_selected_services_button = "//*[@id='product-tabs']/button"

    details_delivery_time = "//*[@id='__next']/main/div/div[2]/div/div[1]/div[2]/div[1]/ul/li[1]/div/p/span[1]"
    details_pronos = "//*[@id='__next']/main/div/div[2]/div/div[1]/div[2]/div[1]/ul/li[2]/div/span"
    details_lifting = "//*[@id='__next']/main/div/div[2]/div/div[1]/div[2]/div[1]/ul/li[3]/div/span"

    express_delivery_toggle_2 = "//*[@id='__next']/main/div/div[2]/div/div[1]/div[2]/div[2]/div/label"
    save_and_continue_button_1 = "//*[@id='__next']/main/div/div[2]/div/div[1]/div[6]/div/button[2]"
    personal_data_assert_title = "//*[@id='__next']/main/div/div[2]/div/div/p"

    # Getters

    def get_delivery_method_selector(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_method_selector)))

    def get_delivery_method_selector_assert_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_method_selector_assert_title)))

    def get_address_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_field)))

    def get_select_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_address)))

    def get_apartment_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apartment_field)))

    def get_floor_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.floor_field)))

    def get_entrance_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.entrance_field)))

    def get_full_delivery_address(self):
        full_address = f"{self.get_address_field().get_attribute("value").strip()}, кв. {self.get_apartment_field().get_attribute("value").strip()}, {self.get_floor_field().get_attribute("value").strip()} этаж, {self.get_entrance_field().get_attribute("value").strip()} подъезд"
        return full_address

    def get_express_delivery_toggle_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.express_delivery_toggle_1)))

    def get_delivery_here_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_here_button)))

    def get_express_delivery_toggle_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.express_delivery_toggle_2)))

    def get_delivery_details_assert_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_details_assert_title)))

    def get_save_and_continue_button_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.save_and_continue_button_1)))

    def get_personal_data_assert_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_data_assert_title)))

    def get_select_services_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_services_button)))

    def get_services_assert_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.services_assert_title)))

    def get_by_lift_toggle(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.by_lift_toggle)))

    def get_apply_selected_services_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_selected_services_button)))

    def get_details_delivery_time(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.details_delivery_time)))
        return element.text.strip()

    def get_details_pronos(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.details_pronos)))
        return element.text.strip()

    def get_details_lifting(self):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.details_lifting)))
        return element.text.strip()

    def get_full_delivery_details(self):
        full_details = f"{self.get_details_pronos()}, {self.get_details_lifting()}"
        return full_details

    # Actions

    def click_delivery_method_selector(self):
        element = self.get_delivery_method_selector()
        print(f'Click Delivery method: "{element.text.strip()}"')
        element.click()

    def input_address_field(self, address_field):
        element = self.get_address_field()
        print(f'Input "{element.get_attribute("placeholder").strip()}" field')
        element.send_keys(address_field)

    def click_select_address(self):
        self.get_select_address().click()
        print('Apply entered "Адрес"')

    def input_apartment_field(self, apartment_field):
        element = self.get_apartment_field()
        print(f'Input "{element.get_attribute("placeholder").strip()}" field')
        element.send_keys(apartment_field)

    def input_floor_field(self, floor_field):
        element = self.get_floor_field()
        print(f'Input "{element.get_attribute("placeholder").strip()}" field')
        element.send_keys(floor_field)

    def input_entrance_field(self, entrance_field):
        element = self.get_entrance_field()
        print(f'Input "{element.get_attribute("placeholder").strip()}" field')
        element.send_keys(entrance_field)

    def click_express_delivery_toggle(self):
        element = self.get_express_delivery_toggle_1()
        print(f'Click "{element.text.strip()}" toggle')
        element.click()

    def click_delivery_here_button(self):
        element = self.get_delivery_here_button()
        print(f'Click "{element.text.strip()}" button')
        element.click()

    def click_save_and_continue_button_1(self):
        element = self.get_save_and_continue_button_1()
        print(f'Click "{element.text.strip()}" button 1')
        element.click()

    def click_select_services_button(self):
        element = self.get_select_services_button()
        print(f'Click "{element.text.strip()}" button')
        element.click()

    def click_by_lift_toggle(self):
        element = self.get_by_lift_toggle()
        print(f'Click "{element.text.strip()}" toggle')
        element.click()

    def click_apply_selected_services_button(self):
        element = self.get_apply_selected_services_button()
        print(f'Click "{element.text.strip()}" button')
        element.click()

    # Methods

    # Добавил time.sleep для более стабильного прохождения теста.
    # Стоит добавить ожидание конретного элемента, возможно загрузки карты.
    def change_delivery_method(self):
        with allure.step("Change Delivery method"):
            Logger.add_start_step(method="change_delivery_method")
            self.get_current_url()
            time.sleep(1)
            self.click_delivery_method_selector()
            self.assert_word(self.get_delivery_method_selector_assert_title(), "Куда доставить?")
            time.sleep(1)
            Logger.add_end_step(url=self.driver.current_url, method="change_delivery_method")

    # Добавил time.sleep для более стабильного прохождения теста.
    # Стоит добавить ожидание конретного элемента, возможно доступности delivery_here_button.
    def input_delivery_address(self):
        with allure.step("Input Delivery address"):
            Logger.add_start_step(method="input_delivery_address")
            self.input_address_field("Москва, улица Даниловский Вал, 1с6")
            time.sleep(2)
            self.click_select_address()
            time.sleep(2)
            self.input_apartment_field(self.faker.random_int(min=1, max=100))
            self.input_floor_field(self.faker.random_int(min=1, max=30))
            self.input_entrance_field(self.faker.random_int(min=1, max=10))
            Logger.add_end_step(url=self.driver.current_url, method="input_delivery_address")

    def apply_express_delivery(self):
        with allure.step("Apply Express delivery option"):
            Logger.add_start_step(method="apply_express_delivery")
            self.click_express_delivery_toggle()
            self.checkbox_is_selected_status(self.get_express_delivery_toggle_1())
            Logger.add_end_step(url=self.driver.current_url, method="apply_express_delivery")

    def click_delivery_here(self):
        with allure.step("Click Delivery here button"):
            Logger.add_start_step(method="click_delivery_here")
            self.click_delivery_here_button()
            self.assert_word(self.get_delivery_details_assert_title(), "Детали доставки")
            self.checkbox_is_selected_status(self.get_express_delivery_toggle_2())
            Logger.add_end_step(url=self.driver.current_url, method="click_delivery_here")

    def select_additional_services(self):
        with allure.step("Select Additional services"):
            Logger.add_start_step(method="select_additional_services")
            self.click_select_services_button()
            self.assert_word(self.get_services_assert_title(), "Дополнительные услуги")
            self.click_by_lift_toggle()
            self.checkbox_is_selected_status(self.get_by_lift_toggle())
            Logger.add_end_step(url=self.driver.current_url, method="select_additional_services")

    def apply_additional_services(self):
        with allure.step("Apply Additional services button"):
            Logger.add_start_step(method="apply_additional_services")
            self.click_apply_selected_services_button()
            self.assert_word(self.get_delivery_details_assert_title(), "Детали доставки")
            Logger.add_end_step(url=self.driver.current_url, method="apply_additional_services")

    def assert_full_delivery_address(self, expected_address, expected_apartment, expected_floor, expected_entrance):
        with allure.step("Assertion of Full Delivery address"):
            Logger.add_start_step(method="assert_full_delivery_address")
            expected_full_address = f"{expected_address}, кв. {expected_apartment}, {expected_floor} этаж, {expected_entrance} подъезд"
            actual_full_address = self.get_full_delivery_address()
            self.assert_product_details(expected_full_address, actual_full_address, label="Full entered Delivery address")
            Logger.add_end_step(url=self.driver.current_url, method="assert_full_delivery_address")

    def click_save_and_continue_1(self):
        with allure.step("Click Save and continue button 1"):
            Logger.add_start_step(method="click_save_and_continue_1")
            self.click_save_and_continue_button_1()
            self.assert_word(self.get_personal_data_assert_title(), "Данные получателя")
            Logger.add_end_step(url=self.driver.current_url, method="click_save_and_continue_1")
