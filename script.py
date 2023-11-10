import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys

import time

class AsosTests(unittest.TestCase):
    # 1. Script for adding a product to cart
    def add_product_to_cart(self):
        driver = webdriver.Firefox()
        driver.get("https://www.asos.com/women/")

        winter_button = driver.find_element(By.CSS_SELECTOR, "[data-id='5811d5c8-03b2-4bf3-bf0d-e4471f8e5a46']")
        winter_button.click()
        puffer_jackets = driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.asos.com/women/coats-jackets/puffer-jackets/cat/?cid=28643')]")
        puffer_jackets.click()
        product = driver.find_element(By.XPATH, "//a[contains(@href, '/the-north-face/the-north-face-nuptse-cropped-down-puffer-jacket-in-black/prd/204516879#colourWayId-204516904')]")
        product.click()
        variant_selector = driver.find_element(By.XPATH, "//select[contains(@id, 'variantSelector')]")
        variant_selector.click()
        m_size = driver.find_element(By.XPATH, "//option[contains(@value, '204516917')]")
        m_size.click()
        green_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='add-button']")
        green_button.click()

    # 2. Script for signup
    def signup(self):
        driver = webdriver.Firefox()
        actions = ActionChains(driver)
        driver.get("https://www.asos.com/women/")

        human_icon = driver.find_element(By.CSS_SELECTOR, "[data-testid='myAccountIcon']")
        actions.move_to_element(human_icon).perform()
        time.sleep(3)

        signup_link = driver.find_element(By.CSS_SELECTOR, "[data-testid='signup-link']")
        signup_link.click()

        email_input = driver.find_element(By.ID, "Email")
        first_name_input = driver.find_element(By.ID, "FirstName")
        last_name_input = driver.find_element(By.ID, "LastName")
        password_input = driver.find_element(By.ID, "Password")
        password_input = driver.find_element(By.ID, "Password")
        birthday = driver.find_element(By.ID, "BirthDay")
        birthmonth = driver.find_element(By.ID, "BirthMonth")
        birth_year = driver.find_element(By.ID, "BirthYear")
        input_for_male_clothes = driver.find_element(By.ID, "male")
        input_for_submit = driver.find_element(By.ID, "register")

        email_input.send_keys("random@gmail.com")
        first_name_input.send_keys("name")
        last_name_input.send_keys("laname")
        password_input.send_keys("passwordk123123")
        birthday.click()
        day_option = driver.find_element(By.XPATH, "//option[contains(@value, '1')]")
        day_option.click()

        birthmonth.click()
        month_option = driver.find_element(By.XPATH, "//option[contains(text(), 'January')]")
        month_option.click()

        birth_year.click()
        year_option = driver.find_element(By.XPATH, "//option[contains(@value, '1998')]")
        year_option.click()
        input_for_male_clothes.click()
        input_for_submit.click()

    # 3. Script for sign in
    def signin(self):
        driver = webdriver.Firefox()
        actions = ActionChains(driver)
        driver.get("https://www.asos.com/women/")

        human_icon = driver.find_element(By.CSS_SELECTOR, "[data-testid='myAccountIcon']")
        actions.move_to_element(human_icon).perform()
        time.sleep(3)

        signin_link = driver.find_element(By.CSS_SELECTOR, "[data-testid='signin-link']")
        signin_link.click()

        email_input = driver.find_element(By.ID, "EmailAddress")
        password_input = driver.find_element(By.ID, "Password")
        signin_button = driver.find_element(By.ID, "signin")

        email_input.send_keys("random@gmail.com")
        password_input.send_keys("pass")
        signin_button.click()


new_test = AsosTests()
new_test.add_product_to_cart()


if __name__ == '__main__':
	unittest.main()
