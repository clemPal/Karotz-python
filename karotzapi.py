import requests
import time


def sleep():
	r_ears = requests.get('http://192.168.234.244/cgi-bin/ears?left=6&right=5') #place the ears in horizontal position. Note that the ears 	have a bug left=right+1.
	#print r_ears.text
	r_led = requests.get('http://192.168.234.244/cgi-bin/leds?color=00ddff') #the LED is cian.
	#print r_led.text


def medicine():
	r_ears = requests.get('http://192.168.234.244/cgi-bin/ears?left=16&right=15') #place the ears in vertical position. Note that the ears have a bug left=right+1.
	#print r_ears.text
	r_led = requests.get('http://192.168.234.244/cgi-bin/leds?pulse=1&color=ffb300&speed=747&color2=000000') #the LED is orange and blink.
	#print r_led.text
	r_voice = requests.get('http://192.168.234.244/cgi-bin/tts?voice=ryan&text=Have you taken your medication? It is about time.&nocache=0') #exorte the karotz to speak.
	#print r_voice.text


def watchtv():
	r_ears = requests.get('http://192.168.234.244/cgi-bin/ears?left=11&right=10') #place the ears in horizontal position. Note that the ears have a bug left=right+1.
	#print r_ears.text
	r_led = requests.get('http://192.168.234.244/cgi-bin/leds?pulse=1&color=00ddff&speed=1550&color2=000000') #the LED is cian and blink slowly.
	#print r_led.text
	time.sleep(10)
	sleep() #execute slee.py

	time.sleep(20)
	medicine()



def relax ():
	r_led = requests.get('http://192.168.234.244/cgi-bin/leds?pulse=1&color=00ff4d&speed=1550&color2=000000') #the LED is grenn and blink slowly.
	#print r_led.text 
	time.sleep(10)
	sleep() #execute slee.py


'''
TO DO
if __name__ == '__main__':

	sleep()
	watchtv()
	medicine()
	relax ()
'''

