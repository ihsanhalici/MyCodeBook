from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import urllib2, string, random

class captachaCek:
    def __init__(self, soru):
        self.soru = soru
        self.driver = webdriver.Firefox()
        self.capid = ""

    def captachaindir(self):
        def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))

        self.capid = id_generator()
        self.driver.get("http://projecteuler.net/login")
        self.driver.switch_to_active_element()
        self.driver.switch_to_default_content()
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys("")
        password.send_keys("")
        password.send_keys(Keys.RETURN)
        self.driver.get("http://projecteuler.net/problem=%s" %self.soru)
        resim = self.driver.find_element_by_xpath("//img[@id='captcha']").get_attribute('src')
        dosya = open("capler/%s.png" %self.capid,"w")

        resimistek = urllib2.urlopen(resim)
        veri = resimistek.read()
        dosya.write(veri)
        dosya.close()

        def cevapyaz(self, capal, cevapal):
            cevap = self.driver.find_element_by_name("guess")
            cevap.send_keys(cevapal)
            capt = self.driver.find_element_by_name("confirm")
            capt.send_keys(capal)



