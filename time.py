from datetime import datetime
from time import sleep
now = datetime.now()
while True:
    if now.hour == 00 and now.minute == 25:
        break
    print("Not yet")