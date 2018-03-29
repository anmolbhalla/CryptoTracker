from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

def Coin_Market_Details():

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

             if(j!=0):
                 data_file1.writelines(str(table_data[0].text) + '***')
                 data_file1.writelines(str(coin_name) + '***')

             for k in range(1,len(table_data)-1):
                 data_file1.writelines(str(table_data[k].text) + '***')
             data_file1.writelines('\n')

    data_file1.writelines('\n\n')
    data_file1.close()

def Coin_Market_Headers():

    try:

        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[1]/div[5]'))
        WebDriverWait(driver, timeout).until(element_present)

    except TimeoutException:

        print("May be you are not connected to internet")

    coin_name = driver.find_element_by_class_name('text-large').text
    coin_price = driver.find_elements_by_class_name('text-large2')
    coin_currency = driver.find_elements_by_class_name('details-text-medium')

    data_file2.writelines(str(coin_name) + '\n')
    data_file2.writelines(str(coin_price[0].text) + coin_currency[0].text + '\n')
    data_file2.writelines(str(coin_price[1].text + '\n'))

    for i in range(1,len(coin_currency),2):
        data_file2.writelines(str(coin_currency[i].text) + '\n' + str(coin_currency[i+1].text) + '\n')

    data_file2.writelines('\n\n')
    data_file2.close()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    coin_link_file=open('coin_links.txt','r')
    data_file1 = open('crypto_market_data.txt', 'w')
    data_file2 = open('crypto_market_data_headers.txt', 'w')
    link=coin_link_file.readline()
    i=1
    while(link):
        print(i)
        i=i+1
        driver.get(link)
        timeout = 200
        Coin_Market_Details()
        Coin_Market_Headers()
        link=coin_link_file.readline()
    coin_link_file.close()