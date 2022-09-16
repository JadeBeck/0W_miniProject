from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("C:/Users/okyee/OneDrive/바탕 화면/코딩/웹종/PreProject/chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = 'https://playboard.co/chart/video/most-viewed-all-videos-in-worldwide-total'
driver.get(url)

elems = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/main/div/div[2]/table/tbody/tr[1]/td[3]/a/h3')
print(elems.text)


