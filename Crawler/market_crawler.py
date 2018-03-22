from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()
url = 'https://coinmarketcap.com/currencies/ethereum/#markets'
driver.get(url)
timeout=200

try:
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[1]/div[2]'))
    WebDriverWait(driver, timeout).until(element_present)

except TimeoutException:
    print("May be you are not connected to internet")


table=driver.find_elements_by_xpath('//*[@id="markets-table"]')
title_name = driver.find_element_by_class_name('text-large').text
price = driver.find_elements_by_class_name('text-large2')
usd = driver.find_element_by_class_name('details-text-medium').text
marketcap = driver.find_elements_by_class_name("coin-summary-item-detail")
print(title_name)
print(price[0].text+usd)
print(price[1].text)
for i in marketcap:
    print(i.text)
for i in range(0,len(table)):
     tag = table[i].find_elements_by_tag_name('tr')
     for i in range(0,len(tag)):
         #src_graph = image_graph[i].get_attribute('src')
         #print(src_logo)
         #print(src_graph)
         table_data=tag[i].find_elements_by_tag_name('td')
         for i in range(0,len(table_data)-1):
             print(table_data[i].text)
         print('\n')