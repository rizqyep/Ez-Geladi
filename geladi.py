import time
from time import sleep
from selenium import webdriver
URL = "https://igracias.telkomuniversity.ac.id/index.php?pageid=2941"
 
PATH_TO_DRIVER = 'chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(PATH_TO_DRIVER)
browser.set_window_position(0,0)
browser.get(URL)
while True:
    sleep(10)
    browser.refresh()