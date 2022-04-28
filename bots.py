import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from up import *


# #create webdriver object
driver = webdriver.Chrome(
    'C:/Users/USER/Desktop/insta/InstagramLikeFollow_selenium/chromedriver.exe')

name = 'nayemjaman'

# driver.close()


def login(driver, uname, passw):
    driver.get('https://www.instagram.com')
    username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.send_keys(uname)
    password.send_keys(passw)
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']"))).click()
    try:
        alert = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
    except:
        pass
    try:
        alert2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]'))).click()
    except:
        pass


# get followers list
def scrolling_down(driver, name):
    driver.get('https://www.instagram.com/'+name+'/')
    time.sleep(2)
    driver.find_element_by_partial_link_text("follower").click()

    pop_up_window = WebDriverWait(
        driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='isgrP']")))
    users = []
    
    # Scroll till Followers list is there
    while True:
        driver.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
            pop_up_window)
        time.sleep(3)
        # followers = driver.find_elements_by_class_name('d7ByH')
        followers = driver.find_elements_by_class_name('_7UhW9')
        followers = [i.text for i in followers]
        users.append(followers)
        print(users)
    # followers = [users.append(i.get_attribute('href')) for i in followers]
    users = set(users)
    




login(driver, uname, passw)
scrolling_down(driver, name)
# followers(driver)
driver.close()







