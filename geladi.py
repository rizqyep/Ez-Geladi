import time
from datetime import datetime
from time import sleep
from selenium import webdriver
URL = "https://igracias.telkomuniversity.ac.id"
PATH_TO_DRIVER = 'chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(PATH_TO_DRIVER)

browser.get(URL)
sleep(20) #atur sesuai waktu yang diperluin buat login diawal
browser.get("https://igracias.telkomuniversity.ac.id/geladi?pageid=20391")
   
count = 0
now = datetime.now()
while True:
    
    if now.hour == 9 and now.minute == 00:
        break
    print(count)
    sleep(5)
    count+=1
    browser.refresh()
  