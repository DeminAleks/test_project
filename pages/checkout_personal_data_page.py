from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import allure


class PersonalDataPage(Base):

    # Locators

    first_name_field = "//*[@id='firstname']"
    last_name_field = "//*[@id='lastname']"
    email_field = "//*[@id='email']"
    phone_number_field = "//*[@id='telephone']"
    notes_field = "//*[@id='customer_notes']"

    terms_of_service_checkbox = "(//div[@class='_1AaQx'])[1]"
    subscription_checkbox = "(//div[@class='_1AaQx'])[2]"
    terms_of_service_checkbox_status = "(//div[@class='TX7r9'])[1]"
    subscription_checkbox_status = "(//div[@class='TX7r9'])[2]"

    save_and_continue_button_2 = "//button[@class='_2eEQG _2xhLm _3sJhC _3aV4_ _2kk3H']"
    order_page_assert_title = "//p[contains(text(), 'Оформление заказа')]"

    # Getters

    def get_first_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name_field)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_phone_number_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number_field)))

    def get_notes_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.notes_field)))

    # Notes не суммирую, т.к. добавленные комментарии не отображаются на Order page
    def get_full_personal_data(self):
        full_personal_data = f"{self.get_first_name_field().get_attribute("value").strip()} {self.get_last_name_field().get_attribute("value").strip()}, {self.get_email_field().get_attribute("value").strip()}, {self.get_phone_number_field().get_attribute("value").strip()}"
        return full_personal_data

    def get_terms_of_service_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.terms_of_service_checkbox)))

    def get_subscription_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subscription_checkbox)))

    def get_terms_of_service_checkbox_status(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.terms_of_service_checkbox_status)))

    def get_subscription_checkbox_status(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subscription_checkbox_status)))

    def get_save_and_continue_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.save_and_continue_button_2)))

    def get_order_page_assert_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_page_assert_title)))

    # Actions

    def input_first_name_field(self, first_name_field):
        element = self.get_first_name_field()
        print(f'Input "{element.get_attribute("placeholder").strip()}" field')
        element.send_keys(first_name_field)

    def input_last_name_field(self, last_name_field):
        element = self.get_last_name_field()
        print(f'Input "{element.get_attribute("placeholder").strip()}" field')
        element.send_keys(last_name_field)

    def input_email_field(self, email_field):
        element = self.get_email_field()
        print(f'Input "{element.get_attribute("placeholder").strip()}" field')
        element.send_keys(email_field)

    def input_phone_number_field(self, phone_number_field):
        element = self.get_phone_number_field()
        print(f'Input "{element.get_attribute("placeholder").strip()}" field')
        element.send_keys(phone_number_field)

    def input_notes_field(self, notes_field):
        element = self.get_notes_field()
        print(f'Input "{element.get_attribute("placeholder").strip()}" field')
        element.send_keys(notes_field)

    def click_terms_of_service_checkbox(self):
        self.get_terms_of_service_checkbox().click()
        print('Click "Terms of service" checkbox')

    def click_subscription_checkbox(self):
        self.get_subscription_checkbox().click()
        print('Click "Subscription" checkbox')

    def click_save_and_continue_2_button(self):
        element = self.get_save_and_continue_button_2()
        print(f'Click "{element.text.strip()}" button 2')
        element.click()

    # Methods
    def input_personal_data(self):
        with allure.step("Input Personal data"):
            Logger.add_start_step(method="input_personal_data")
            self.get_current_url()
            self.input_first_name_field(self.faker.first_name())
            self.input_last_name_field(self.faker.last_name())
            self.input_email_field(self.faker.email())
            self.input_phone_number_field(self.faker.phone_number())
            self.input_notes_field(self.faker.sentences(nb=2))
            Logger.add_end_step(url=self.driver.current_url, method="input_personal_data")

    def click_terms_of_service_cb(self):
        with allure.step("Click Terms of service checkbox"):
            Logger.add_start_step(method="click_terms_of_service_cb")
            self.click_terms_of_service_checkbox()
            self.checkbox_is_selected_status(self.get_terms_of_service_checkbox_status())
            Logger.add_end_step(url=self.driver.current_url, method="click_terms_of_service_cb")

    def click_subscription_cb(self):
        with allure.step("Click Subscription checkbox"):
            Logger.add_start_step(method="click_subscription_cb")
            self.click_subscription_checkbox()
            self.checkbox_is_selected_status(self.get_subscription_checkbox_status())
            Logger.add_end_step(url=self.driver.current_url, method="click_subscription_cb")

    def click_save_and_continue_2(self):
        with allure.step("Click Save and continue button 2"):
            Logger.add_start_step(method="click_save_and_continue_2")
            self.click_save_and_continue_2_button()
            self.assert_word(self.get_order_page_assert_title(), "Оформление заказа")
            Logger.add_end_step(url=self.driver.current_url, method="click_save_and_continue_2")
