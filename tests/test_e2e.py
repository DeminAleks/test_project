import time
from pages.cart_page import CartPage
from pages.homepage import HomePage
from pages.product_listing_page import ProductListingPage
from pages.checkout_shipping_page import ShippingPage
from pages.checkout_personal_data_page import PersonalDataPage
from pages.checkout_order_page import OrderPage
import allure


# Навигация на страницу товара и добавление его в корзину
def navigate_to_product_and_add_to_cart(driver):
    home = HomePage(driver)
    home.opening_homepage()                # Открываем главную страницу
    home.navigation_to_plp_level_1()       # Переходим на первый уровень PLP
    home.navigation_to_plp_level_2()       # Переходим на второй уровень PLP

    plp = ProductListingPage(driver)
    plp.apply_filter_plp_level_3()         # Применяем фильтр по категории
    plp.apply_sort()                       # Применяем сортировку
    plp.apply_filter_delivery()            # Применяем фильтр по доставке
    plp.apply_filter_brand()               # Применяем фильтр по бренду
    plp.apply_filter_price()               # Применяем фильтр по цене

    plp_product_1_name = plp.get_product_1_name_plp()  # Получаем название первого товара на PLP
    print("Product_1 name on PLP:", plp_product_1_name)
    plp_product_1_price = plp.get_product_1_price_plp() # Получаем цену первого товара на PLP
    print("Product_1 price on PLP:", plp_product_1_price)

    plp.click_add_to_cart_product_1()      # Добавляем первый товар в корзину
    return plp_product_1_name, plp_product_1_price


# Проверка корзины и переход к оформлению заказа
def verify_cart_and_proceed_to_checkout(driver, plp_product_1_name, plp_product_1_price):
    cart = CartPage(driver)
    cart_product_1_name = cart.get_product_1_name_cart()         # Читаем название товара в корзине
    print("Product_1 name on Cart page:", cart_product_1_name)
    cart.assert_product_1_name_cart(plp_product_1_name)          # Проверяем соответствие названия товара

    cart_product_1_price = cart.get_product_1_price_cart()       # Читаем цену товара в корзине
    print("Product_1 price on Cart page:", cart_product_1_price)
    cart.assert_product_1_price_cart(plp_product_1_price)        # Проверяем соответствие цены товара

    cart_sum_price = cart.get_sum_products_cart()                # Получаем итоговую сумму корзины
    print("Sum of products on Cart page:", cart_sum_price)
    cart.assert_sum_products_cart(cart_product_1_price)          # Проверяем сумму корзины

    cart.navigation_to_checkout()                               # Переходим к оформлению заказа
    return cart_product_1_name, cart_sum_price


# Заполнение данных о доставке
def fill_shipping_data(driver):
    shipping = ShippingPage(driver)
    shipping.change_delivery_method()                           # Выбираем способ доставки
    shipping.input_delivery_address()                           # Вводим адрес доставки

    # Читаем введённые данные из формы
    address = shipping.get_address_field().get_attribute("value").strip()
    apartment = shipping.get_apartment_field().get_attribute("value").strip()
    floor = shipping.get_floor_field().get_attribute("value").strip()
    entrance = shipping.get_entrance_field().get_attribute("value").strip()
    print("Sum of entered delivery address:", f"{address}, кв. {apartment}, {floor} этаж, {entrance} подъезд")

    shipping.apply_express_delivery()                           # Применяем экспресс-доставку
    shipping.click_delivery_here()                              # Подтверждаем доставку по адресу
    shipping.select_additional_services()                       # Выбираем доп. услуги
    shipping.apply_additional_services()                        # Применяем выбранные доп. услуги

    shipping.assert_full_delivery_address(address, apartment, floor, entrance)  # Проверяем введённый адрес

    shipping_full_address = shipping.get_full_delivery_address()    # Получаем итоговый адрес на странице доставки
    print("Full delivery address on Shipping page:", shipping_full_address)

    shipping_full_details = shipping.get_full_delivery_details()    # Получаем все детали доставки
    print("Full shipping details on Shipping page:", shipping_full_details)

    shipping_delivery_time = shipping.get_details_delivery_time()   # Получаем время доставки
    print("Delivery time:", shipping_delivery_time)

    shipping.click_save_and_continue_1()                         # Сохраняем данные и продолжаем
    return shipping_full_address, shipping_full_details, shipping_delivery_time


# Заполнение персональных данных
def fill_personal_data(driver):
    personal = PersonalDataPage(driver)
    personal.input_personal_data()                               # Вводим персональные данные пользователя

    # Читаем введённые данные из формы
    first_name = personal.get_first_name_field().get_attribute("value").strip()
    last_name = personal.get_last_name_field().get_attribute("value").strip()
    email = personal.get_email_field().get_attribute("value").strip()
    phone_number = personal.get_phone_number_field().get_attribute("value").strip()
    notes = personal.get_notes_field().get_attribute("value").strip()
    print("Sum of entered personal data:", f"{first_name}, {last_name}, {email}, {phone_number}, {notes}")

    full_personal_data = personal.get_full_personal_data()       # Получаем итоговый блок с персональными данными
    print("Full personal data on Personal data page:", full_personal_data)

    personal.click_terms_of_service_cb()                        # Соглашаемся с условиями
    personal.click_subscription_cb()                            # Подписываемся на рассылку

    personal.click_save_and_continue_2()                        # Сохраняем данные и продолжаем
    return full_personal_data


# Проверка итоговой страницы заказа
def verify_order(driver, cart_sum_price, cart_product_1_name, shipping_full_address, full_personal_data, shipping_full_details, shipping_delivery_time):
    order = OrderPage(driver)

    order_sum_price = order.get_sum_products_order()            # Проверяем сумму товаров
    print("Sum of products on Order page:", order_sum_price)
    order.assert_sum_products_order(cart_sum_price)

    order_product_1_name = order.get_product_1_name_order()     # Проверяем название товара
    print("Product_1 name on Order page:", order_product_1_name)
    order.assert_product_1_name_order(cart_product_1_name)

    order_address = order.get_full_delivery_address_order()     # Проверяем адрес доставки
    print("Full delivery address on Order page:", order_address)
    order.assert_full_delivery_address_order(shipping_full_address)

    order_personal_data = order.get_full_personal_data_order()  # Проверяем персональные данные
    print("Full personal data on Order page:", order_personal_data)
    order.assert_full_personal_data_order(full_personal_data)

    order_delivery_details = order.get_full_delivery_details_order()  # Проверяем детали доставки
    print("Full delivery details on Order page:", order_delivery_details)
    order.assert_full_delivery_details_order(shipping_full_details)

    order_delivery_time = order.get_order_delivery_time()       # Проверяем время доставки
    print("Delivery time on Order page:", order_delivery_time)
    order.assert_delivery_time_order(shipping_delivery_time)


# Финальный тест end-to-end сценария покупки товара
@allure.description("Test e2e")
def test_e2e(driver, set_up):
    plp_product_1_name, plp_product_1_price = navigate_to_product_and_add_to_cart(driver)   # Навигация + добавление товара в корзину
    cart_product_1_name, cart_product_sum = verify_cart_and_proceed_to_checkout(driver, plp_product_1_name, plp_product_1_price)  # Проверка корзины
    shipping_full_address, shipping_full_details, shipping_delivery_time = fill_shipping_data(driver)  # Заполнение данных о доставке
    full_personal_data = fill_personal_data(driver)     # Заполнение личных данных
    verify_order(driver, cart_product_sum, cart_product_1_name, shipping_full_address, full_personal_data, shipping_full_details, shipping_delivery_time)   # Проверка итогового заказа
    time.sleep(2)   # Пауза перед завершением теста
