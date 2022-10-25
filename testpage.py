from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

str1 = '123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()
str4 = str1+str2+str3
ls = list(str4)
random.shuffle(ls)
psw = ''.join([random.choice(ls) for x in range(12)])

def main():
    driver=webdriver.Chrome()
    driver.get("Instagramhttps://www.instagram.com")
    time.sleep(5)
    el = driver.find_element(By.XPATH, "#")
    el.click()
    time.sleep(5)
    eml = driver.find_element(By.XPATH,'#')
    eml.send_keys('mail')
    time.sleep(2)
    btn_go = driver.find_element(By.XPATH,'#')
    btn_go.click()
    time.sleep(2)
    pas_page = driver.find_element(By.XPATH,'#')
    pas_page.send_keys('pass')
    time.sleep(4)
    
    btn_send = driver.find_element(By.XPATH,'#')
    btn_send.click()
    time.sleep(2)
    categ = driver.find_element(By.XPATH,'#')
    categ.click()
    time.sleep(1)
    prof = driver.find_element(By.XPATH,'#')
    prof.click()
    time.sleep(1)
    usermane = driver.find_element(By.XPATH,'#')
    usermane.clear()
    time.sleep(1)
    usermane.send_keys(psw)
    time.sleep(1)
    sohr = driver.find_element(By.XPATH,'#')
    sohr.click()
    time.sleep(5)
    driver.quit()
if __name__ == "__main__":
    main()
