import time
from pages.cart_page import CartPage
from pages.homepage import HomePage
from pages.product_listing_page import ProductListingPage
from pages.checkout_shipping_page import ShippingPage
from pages.checkout_personal_data_page import PersonalDataPage
from pages.checkout_order_page import OrderPage
import allure


def navigate_to_product_and_add_to_cart(driver):
    home = HomePage(driver)
    home.opening_homepage()
    home.get_screenshot()
    home.navigation_to_plp_level_1()
    home.get_screenshot()
    home.navigation_to_plp_level_2()
    home.get_screenshot()

    plp = ProductListingPage(driver)
    plp.apply_filter_plp_level_3()
    plp.apply_sort()
    plp.apply_filter_delivery()
    plp.apply_filter_brand()
    plp.apply_filter_price()

    plp_product_1_name = plp.get_product_1_name_plp()
    print("Product_1 name on PLP:", plp_product_1_name)
    plp_product_1_price = plp.get_product_1_price_plp()
    print("Product_1 price on PLP:", plp_product_1_price)

    plp.get_screenshot()
    plp.click_add_to_cart_product_1()
    return plp_product_1_name, plp_product_1_price


def verify_cart_and_proceed_to_checkout(driver, plp_product_1_name, plp_product_1_price):
    cart = CartPage(driver)
    cart_product_1_name = cart.get_product_1_name_cart()
    print("Product_1 name on Cart page:", cart_product_1_name)
    cart.assert_product_1_name_cart(plp_product_1_name)

    cart_product_1_price = cart.get_product_1_price_cart()
    print("Product_1 price on Cart page:", cart_product_1_price)
    cart.assert_product_1_price_cart(plp_product_1_price)

    cart_sum_price = cart.get_sum_products_cart()
    print("Sum of products on Cart page:", cart_sum_price)
    cart.assert_sum_products_cart(cart_product_1_price)

    cart.get_screenshot()
    cart.navigation_to_checkout()
    return cart_product_1_name, cart_sum_price


def fill_shipping_data(driver):
    shipping = ShippingPage(driver)
    shipping.get_screenshot()
    shipping.change_delivery_method()
    shipping.get_screenshot()
    shipping.input_delivery_address()

    address = shipping.get_address_field().get_attribute("value").strip()
    apartment = shipping.get_apartment_field().get_attribute("value").strip()
    floor = shipping.get_floor_field().get_attribute("value").strip()
    entrance = shipping.get_entrance_field().get_attribute("value").strip()
    print("Sum of entered delivery address:", f"{address}, кв. {apartment}, {floor} этаж, {entrance} подъезд")

    shipping.apply_express_delivery()
    shipping.get_screenshot()
    shipping.click_delivery_here()
    shipping.get_screenshot()
    shipping.select_additional_services()
    shipping.get_screenshot()
    shipping.apply_additional_services()

    shipping.assert_full_delivery_address(address, apartment,floor, entrance)

    shipping_full_address = shipping.get_full_delivery_address()
    print("Full delivery address on Shipping page:", shipping_full_address)

    shipping_full_details = shipping.get_full_delivery_details()
    print("Full shipping details on Shipping page:", shipping_full_details)

    shipping_delivery_time = shipping.get_details_delivery_time()
    print("Delivery time:", shipping_delivery_time)

    shipping.get_screenshot()
    shipping.click_save_and_continue_1()
    return shipping_full_address, shipping_full_details, shipping_delivery_time


def fill_personal_data(driver):
    personal = PersonalDataPage(driver)
    personal.get_screenshot()
    personal.input_personal_data()

    first_name = personal.get_first_name_field().get_attribute("value").strip()
    last_name = personal.get_last_name_field().get_attribute("value").strip()
    email = personal.get_email_field().get_attribute("value").strip()
    phone_number = personal.get_phone_number_field().get_attribute("value").strip()
    notes = personal.get_notes_field().get_attribute("value").strip()
    print("Sum of entered personal data:", f"{first_name}, {last_name}, {email}, {phone_number}, {notes}")

    full_personal_data = personal.get_full_personal_data()
    print("Full personal data on Personal data page:", full_personal_data)

    personal.get_screenshot()
    personal.click_terms_of_service_cb()
    personal.click_subscription_cb()

    personal.get_screenshot()
    personal.click_save_and_continue_2()
    return full_personal_data


def verify_order(driver, cart_sum_price, cart_product_1_name, shipping_full_address, full_personal_data, shipping_full_details, shipping_delivery_time):
    order = OrderPage(driver)
    order.get_screenshot()

    order_sum_price = order.get_sum_products_order()
    print("Sum of products on Order page:", order_sum_price)
    order.assert_sum_products_order(cart_sum_price)

    order_product_1_name = order.get_product_1_name_order()
    print("Product_1 name on Order page:", order_product_1_name)
    order.assert_product_1_name_order(cart_product_1_name)

    order_address = order.get_full_delivery_address_order()
    print("Full delivery address on Order page:", order_address)
    order.assert_full_delivery_address_order(shipping_full_address)

    order_personal_data = order.get_full_personal_data_order()
    print("Full personal data on Order page:", order_personal_data)
    order.assert_full_personal_data_order(full_personal_data)

    order_delivery_details = order.get_full_delivery_details_order()
    print("Full delivery details on Order page:", order_delivery_details)
    order.assert_full_delivery_details_order(shipping_full_details)

    order_delivery_time = order.get_order_delivery_time()
    print("Delivery time on Order page:", order_delivery_time)
    order.assert_delivery_time_order(shipping_delivery_time)


@allure.description("Test e2e")
def test_e2e(driver, set_up):
    plp_product_1_name, plp_product_1_price = navigate_to_product_and_add_to_cart(driver)
    cart_product_1_name, cart_product_sum = verify_cart_and_proceed_to_checkout(driver, plp_product_1_name, plp_product_1_price)
    shipping_full_address, shipping_full_details, shipping_delivery_time = fill_shipping_data(driver)
    full_personal_data = fill_personal_data(driver)
    verify_order(driver, cart_product_sum, cart_product_1_name, shipping_full_address, full_personal_data, shipping_full_details, shipping_delivery_time)
    time.sleep(2)
