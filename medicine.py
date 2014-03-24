import requests


r_ears = requests.get('http://192.168.234.244/cgi-bin/ears?left=16&right=15') #place the ears in vertical position. Note that the ears have a bug left=right+1.
print r_ears.text

r_led = requests.get('http://192.168.234.244/cgi-bin/leds?pulse=1&color=ffb300&speed=747&color2=000000') #the LED is orange and blink.
print r_led.text

r_voice = requests.get('http://192.168.234.244/cgi-bin/tts?voice=ryan&text=Have you taken your medication? It is about time.&nocache=0') #exorte the karotz to speak.
print r_voice.text




