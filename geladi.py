import time
from time import sleep
from selenium import webdriver
URL = "https://igracias.telkomuniversity.ac.id"
PATH_TO_DRIVER = 'chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(PATH_TO_DRIVER)
username = input("Input username igracias : ")
password = input("Input password igracias : ")


browser.get(URL)
uname_field = browser.find_element_by_id("textUsername")
uname_field.send_keys(username)
pass_field  = browser.find_element_by_id("textPassword")
pass_field.send_keys(password)
login_btn = browser.find_element_by_id("submit")
login_btn.click()
while True:
    browser.get("https://igracias.telkomuniversity.ac.id/geladi")
    sleep(10) #atur sesuai waktu yang diperluin buat login diawal
    browser.refresh()