import requests
import time


r_led = requests.get('http://192.168.234.244/cgi-bin/leds?pulse=1&color=00ff4d&speed=1550&color2=000000') #the LED is grenn and blink slowly.
print r_led.text
 
time.sleep(10)

execfile("slee.py") #execute slee.py

