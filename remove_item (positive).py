import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(2)

driver.get("https://www.saucedemo.com/")
time.sleep(1)

username = driver.find_element(By.NAME, "user-name")
password = driver.find_element(By.NAME, "password")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

time.sleep(1)

submit_button = driver.find_element(By.ID , "login-button").click()

time.sleep(3)

product_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

time.sleep(3)

cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

time.sleep(3)

remove_button = driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

time.sleep(2)

driver.quit()