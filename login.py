from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

driver = webdriver.Firefox()
user_name = 'cadu.mrod@gmail.com'
user_password = '2650Duka2299!@'

def login():
    driver.get('https://www.instagram.com/')

    sleep(random.randint(1,2))

    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user_name)
    sleep(random.randint(1,2))
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(user_password)
    sleep(random.randint(1,2))
    driver.find_element(By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30']").click()

    sleep(5)




if __name__ == "__main__":
    login()