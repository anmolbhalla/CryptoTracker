from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

def Coin_Market_Details():

    data_file=open('crypto_market_data.txt','w')

    try:

        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[1]/div[5]'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:

        print("May be you are not connected to internet")


    coin_details_table = driver.find_elements_by_xpath('//*[@id="markets-table"]')
    coin_name = driver.find_element_by_class_name('text-large').text

    for i in range(0,len(coin_details_table)):

         tag = coin_details_table[i].find_elements_by_tag_name('tr')

         for j in range(0,len(tag)):

             table_data=tag[j].find_elements_by_tag_name('td')

             if(j!=0):data_file.writelines(str(coin_name) + '-')

             for k in range(0,len(table_data)-1):

                 data_file.writelines(str(table_data[k].text) + '-' + '\n')

    data_file.close()

def Coin_Market_Headers():

    data_file = open('crypto_market_data_headers.txt', 'w')

    try:

        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[1]/div[5]'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:

        print("May be you are not connected to internet")

    coin_name = driver.find_element_by_class_name('text-large').text
    coin_price = driver.find_elements_by_class_name('text-large2')
    coin_currency = driver.find_element_by_class_name('details-text-medium').text
    coin_marketcap = driver.find_elements_by_class_name("coin-summary-item-detail")
    coin_market_header = driver.find_elements_by_class_name("coin-summary-item-header")

    data_file.writelines(str(coin_name) + '-')
    data_file.writelines(str(coin_price[0].text) + coin_currency + '-' )
    data_file.writelines(str(coin_price[1].text ))

    for i in range(0,len(coin_marketcap)):
        data_file.writelines(str(coin_market_header[i].text) + '-' + str(coin_marketcap[i].text + '\n'))

if __name__ == '__main__':


    driver = webdriver.Chrome()
    url = 'https://coinmarketcap.com/currencies/iconomi/#markets'
    driver.get(url)
    timeout = 200
    Coin_Market_Details()
    Coin_Market_Headers()