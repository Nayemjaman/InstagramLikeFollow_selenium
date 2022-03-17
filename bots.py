import os
from tkinter import W, Button
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from up import *


# #create webdriver object
driver = webdriver.Chrome('C:/Users/USER/Desktop/insta/InstagramLikeFollow_selenium/chromedriver.exe')


# driver.close()



def login(driver,uname,passw):
    driver.get('https://www.instagram.com')
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.send_keys(uname)
    password.send_keys(passw)
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    try:
        alert = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
    except:
        pass
    try:
        alert2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]'))).click()
    except:
        pass

login(driver,uname,passw)










# # time.sleep(50)
# # driver.close()





