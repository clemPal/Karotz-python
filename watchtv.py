import requests
import time


r_ears = requests.get('http://192.168.234.244/cgi-bin/ears?left=11&right=10') #place the ears in horizontal position. Note that the ears have a bug left=right+1.
print r_ears.text

r_led = requests.get('http://192.168.234.244/cgi-bin/leds?pulse=1&color=00ddff&speed=1550&color2=000000') #the LED is cian and blink slowly.
print r_led.text

time.sleep(10)

execfile("slee.py") #execute slee.py

