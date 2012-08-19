"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://projecteuler.net/login")
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")


password.send_keys(Keys.RETURN)
driver.get("http://projecteuler.net/problem=201")
elem = driver.find_element_by_name("guess")
dige = driver.find_element_by_name("confirm")
elem.send_keys("anan")
dige.send_keys("baban")
dige.send_keys(Keys.RETURN)
"""
from captacha import *
cap = captachaCek(123)
cap.captachaindir()
