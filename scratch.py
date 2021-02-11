from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user_name = "email"
password = "password"
msg = "msg"
driver = webdriver.Firefox()
driver.get("https://www.facebook.com")
driver.maximize_window()

#login to facebook
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
time.sleep(7)

#Posting something on wall
post_box = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span")
post_box.click()
time.sleep(5)
txt = driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div/span/br")

#commenting on a random friend's recent post
driver.get("https://www.facebook.com/<username>/friends")
time.sleep(3)
friend = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]/div[1]/div[2]/div[1]/a/span")
friend.click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 1000)", "")
comment = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[5]/div[2]/div[1]/div/div/div/form/div/div/div[2]/div/div/div/div")
comment.click()

#sending friend request to a random person on facebook

#unable to complete because facebook blocked my one account and restricted my other account(so i am unable to comment add status or add friend