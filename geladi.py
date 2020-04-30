import time
from time import sleep
from selenium import webdriver
URL = "https://igracias.telkomuniversity.ac.id"
PATH_TO_DRIVER = 'chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(PATH_TO_DRIVER)

browser.get(URL)
sleep(5)
while True:
    browser.get("https://igracias.telkomuniversity.ac.id/geladi")
    sleep(10) #atur sesuai waktu yang diperluin buat login diawal
    browser.refresh()