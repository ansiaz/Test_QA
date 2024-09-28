from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Укажите путь к вашему драйверу
service = Service(executable_path='C:\\Program Files\\ChromeDriver\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # Открытие сайта
    driver.get('https://www.saucedemo.com')

    # Авторизация
    username_input = driver.find_element(By.ID, 'user-name')
    password_input = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    username_input.send_keys('standard_user')
    password_input.send_keys('secret_sauce')
    login_button.click()

    # Выбор товара и добавление в корзину
    time.sleep(2)  # Подождите, пока страница загрузится
    backpack_button = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button")
    backpack_button.click()

    # Переход в корзину
    cart_button = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_button.click()

    # Проверка, что товар добавлен в корзину
    time.sleep(2)
    assert "Sauce Labs Backpack" in driver.page_source

    # Оформление покупки
    checkout_button = driver.find_element(By.XPATH, "//button[text()='Checkout']")
    checkout_button.click()

    # Заполнение полей для оформления заказа
    first_name_input = driver.find_element(By.ID, 'first-name')
    last_name_input = driver.find_element(By.ID, 'last-name')
    zip_code_input = driver.find_element(By.ID, 'postal-code')
    continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")

    first_name_input.send_keys('John')
    last_name_input.send_keys('Doe')
    zip_code_input.send_keys('12345')
    continue_button.click()

    # Завершение покупки
    finish_button = driver.find_element(By.XPATH, "//button[text()='Finish']")
    finish_button.click()

    # Проверка успешного завершения покупки
    time.sleep(2)
    assert "Thank you for your order!" in driver.page_source

finally:
    # Закрытие браузера
    time.sleep(2)
    driver.quit()