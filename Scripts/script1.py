from datetime import datetime
import time


while True:
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    x = int(currentDateAndTime.strftime("%S"))
    if (x == 15 or x==30 or x==45 or x==0):
        f = open("myLog", "a")
        f.write(f'\n{currentTime}')
        f.close()
        time.sleep(3)
    else: pass


