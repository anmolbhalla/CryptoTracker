from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
print("**Welcome**")

driver=webdriver.Chrome()
url = 'https://coinmarketcap.com/'
driver.get(url)
timeout=200

try:
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[1]/div[2]'))
    WebDriverWait(driver, timeout).until(element_present)

except TimeoutException:
    print("May be you are not connected to internet")


table=driver.find_elements_by_xpath('//*[@id="currencies"]')
image_logo = driver.find_elements_by_class_name('currency-logo-sprite')
image_graph = driver.find_elements_by_class_name('sparkline')
for i in range(0,len(table)):
     tag = table[i].find_elements_by_tag_name('tr')
     for i in range(0,len(tag)):
         src_logo = image_logo[i].get_attribute('src')
         src_graph = image_graph[i].get_attribute('src')
         print(src_logo)
         print(src_graph)
         table_data=tag[i+1].find_elements_by_tag_name('td')
         for i in table_data:
             print(i.text)