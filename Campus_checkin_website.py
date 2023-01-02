from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import Campus_checkin_info

PATH = r"chromedriver.exe"

driver = webdriver.Chrome(PATH)

def fill_out(link):
    #open the link
    driver.get(link)

    #click the no button
    no_button = driver.find_element_by_xpath("/html/body/div/div[2]/div/form/table/tbody/tr/td[3]/input")
    #no_button = driver.find_element_by_id("pass")
    no_button.click()

    time.sleep(1)

    #submit
    submit_button = driver.find_element_by_name("what")
    submit_button.click()
    
    time.sleep(1)

def close_browser():
    driver.quit()

