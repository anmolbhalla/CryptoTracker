from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from pyvirtualdisplay import Display
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time

def Coin_details():

    data_file=open('crypto_data.txt','w')

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

         for i in range(0,100):

                src_logo = image_logo[i].get_attribute('src')
                src_graph = image_graph[i].get_attribute('src')
                data_file.writelines(str(src_logo) + '***')

                data_file.writelines(str(src_graph) + '***')
                table_data=tag[i+1].find_elements_by_tag_name('td')

                for i in table_data:

                    data_file.writelines(str(i.text) + '***')
                data_file.writelines('\n')

    data_file.close()

def Coin_Links() :

    file_data=open('coin_links.txt','w')

    coin_links=driver.find_elements_by_class_name('currency-name-container')

    for i in range(0,len(coin_links)):

        individual_link=coin_links[i].get_attribute('href')
        file_data.writelines(str(individual_link) + '#markets' + '\n')

    file_data.close()



if __name__ == '__main__':

    display = Display(visible=0, size=(800, 800))
    display.start()
    driver = webdriver.Chrome()
    url = 'https://coinmarketcap.com/'
    driver.get(url)
    timeout = 200

    # while (True) :
    #
    Coin_details()
    Coin_Links()
    #     time.sleep(150)
    #     driver.refresh()