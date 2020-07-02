import pywhatkit
from time import sleep

for i in range(21, 60, 2):
    pywhatkit.sendwhatmsg("+5511...", "MESSAGE", 23, i)
    sleep(15)