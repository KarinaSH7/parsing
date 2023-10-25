""""Создать автоматический сбор данных билетов направления Сочи-Дубай на 18 ноября"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.binary_location = r"/Users/karinashalya/Downloads/Firefox 119.0.dmg"
driver = webdriver.Firefox(options=options)
driver.get("https://www.aviasales.ru/")
sleep(3)

search_city = driver.find_element(by="xpath", value='//*[@id="avia_form_origin-input"]')
search_city.clear()
search_city.send_keys("Сочи")
sleep(1)
search_city.send_keys(Keys.ARROW_DOWN)
search_city.send_keys(Keys.ENTER)
sleep(1)

search_city = driver.find_element(by="xpath", value='//*[@id="avia_form_destination-input"]')
search_city.clear()
search_city.send_keys("Дубай")
sleep(1)
search_city.send_keys(Keys.ARROW_DOWN)
search_city.send_keys(Keys.ENTER)
sleep(1)


button_data = driver.find_element(by="xpath", value='/html/body/div[7]/div[2]/div/div/div/div/form/div[1]/div/button[1]')
button_data.click()
sleep(2)
button_18 = driver.find_element(by="xpath", value='/html/body/div[7]/div[2]/div/div/div/div/form/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[3]/div[6]/div/div')
button_18.click()
sleep(0.5)
button_18.click()
sleep(2)
button_back = driver.find_element(by="xpath", value='/html/body/div[7]/div[2]/div/div/div/div/form/div[1]/div[2]/div[1]/div/div/div/div/div/header/div[2]')
button_back.click()
sleep(2)
button = driver.find_element(by="xpath", value='/html/body/div[7]/div[2]/div/div/div/div/form/button')
button.click()

sleep(30)
driver.quit()