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
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[1]/div[5]'))
    WebDriverWait(driver, timeout).until(element_present)

except TimeoutException:
    print("May be you are not connected to internet")


coin_details_table = driver.find_elements_by_xpath('//*[@id="markets-table"]')
coin_name = driver.find_element_by_class_name('text-large').text
coin_price = driver.find_elements_by_class_name('text-large2')
coin_currency = driver.find_element_by_class_name('details-text-medium').text
coin_marketcap = driver.find_elements_by_class_name("coin-summary-item-detail")

print(coin_name)
print(coin_price[0].text+coin_currency)
print(coin_price[1].text)

for i in coin_marketcap:

    print(i.text)

for i in range(0,len(coin_details_table)):

     tag = coin_details_table[i].find_elements_by_tag_name('tr')

     for i in range(0,len(tag)):

         table_data=tag[i].find_elements_by_tag_name('td')

         for i in range(0,len(table_data)-1):

             print(table_data[i].text)

         print('\n')