import requests


r_ears = requests.get('http://192.168.234.244/cgi-bin/ears?left=6&right=5') #place the ears in the horizontal position. Note that the ears have a bug left=right+1.
print r_ears.text


r_led = requests.get('http://192.168.234.244/cgi-bin/leds?color=00ddff') #the LED is cian.
print r_led.text

