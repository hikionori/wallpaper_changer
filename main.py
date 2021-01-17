'''Avtor: Danila (hikionori) Verbinsky
   Version: 0.1(beta)
'''

import ctypes
from datetime import datetime
import time
import math

#This is a wallpaper ad. Here you can change the default wallpaper to your own
bliss_day = 'C:\\Users\\danv4\\OneDrive\\Документы\\DДемки\\Сменна обоев\\Bliss Day.png'
bliss_night = 'C:\\Users\\danv4\\OneDrive\\Документы\\DДемки\\Сменна обоев\\Bliss Night.png'
bliss_dusk = 'C:\\Users\\danv4\\OneDrive\\Документы\\DДемки\\Сменна обоев\\Bliss Dusk.png'

fluent_day = 'C:\\Users\\danv4\\OneDrive\\Документы\\DДемки\\Сменна обоев\\Fluent Day.png'
fluent_night = 'C:\\Users\\danv4\\OneDrive\\Документы\\DДемки\\Сменна обоев\\Fluent Night.png'
fluent_dusk = 'C:\\Users\\danv4\\OneDrive\\Документы\\DДемки\\Сменна обоев\\Fluent Dusk.png'

SPI_SETDESKWALLPAPER = 20

def changeBG(path):
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

hour = int(datetime.now().hour)

BG = input("Input B(bliss) or F(fluent) and you can select your files just input SF(select files) : ")

def restartab():
	'''This is a function that sends another function that calls this for BLISS'''
	if hour>= 6 and hour<12:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows
		
		timesleep = 21600
		
		sleeptime = abs(summ - timesleep)
		changeBG(bliss_day)
		time.sleep(sleeptime)
		changeBG(bliss_dusk)
		tims = 21600
		time.sleep(tims)
		changeBG(bliss_night)
		tims = 46800
		time.sleep(tims)
		restartbb()
	elif hour>= 12 and hour<18:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep2 = 21600
		
		sleeptime = abs(summ - timesleep2)
		changeBG(bliss_dusk)
		time.sleep(sleeptime)
		changeBG(bliss_night)
		tims = 46800
		time.sleep(tims)
		restartbb()
	else:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep3 = 46800

		sleeptime = abs(summ - timesleep3)
		changeBG(bliss_night)
		time.sleep(sleeptime)
		restartbb()

def restartbb():
	if hour>= 6 and hour<12:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows
		
		timesleep = 21600
		
		sleeptime = abs(summ - timesleep)
		changeBG(bliss_day)
		time.sleep(sleeptime)
		changeBG(bliss_dusk)
		tims = 21600
		time.sleep(tims)
		changeBG(bliss_night)
		tims = 46800
		time.sleep(tims)
		restartab()
	elif hour>= 12 and hour<18:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep2 = 21600
		
		sleeptime = abs(summ - timesleep2)
		changeBG(bliss_dusk)
		time.sleep(sleeptime)
		changeBG(bliss_night)
		tims = 46800
		time.sleep(tims)
		restartab()
	else:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep3 = 46800

		sleeptime = abs(summ - timesleep3)
		changeBG(bliss_night)
		time.sleep(sleeptime)
		restartab()


if BG == 'B':
		
	restartab()

def restartaf():
	if hour>= 6 and hour<12:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep = 21600

		sleeptime = abs(summ - timesleep)
		changeBG(fluent_day)
		time.sleep(sleeptime)
		changeBG(fluent_dusk)
		tims = 21600
		time.sleep(tims)
		changeBG(fluent_night)
		tims = 46800
		time.sleep(tims)
		restartbf()
	elif hour>= 12 and hour<18:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep2 = 21600

		sleeptime = abs(summ - timesleep2)
		changeBG(fluent_dusk)
		time.sleep(sleeptime)
		changeBG(fluent_night)
		tims = 46800
		time.sleep(tims)
		restartbf()

	else:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep3 = 46800

		sleeptime = abs(summ - timesleep3)
		changeBG(fluent_night)
		time.sleep(sleeptime)
		restartbf()

def restartbf():
	if hour>= 6 and hour<12:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep = 21600

		sleeptime = abs(summ - timesleep)
		changeBG(fluent_day)
		time.sleep(sleeptime)
		changeBG(fluent_dusk)
		tims = 21600
		time.sleep(tims)
		changeBG(fluent_night)
		tims = 46800
		time.sleep(tims)
		restartaf()
	elif hour>= 12 and hour<18:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep2 = 21600

		sleeptime = abs(summ - timesleep2)
		changeBG(fluent_dusk)
		time.sleep(sleeptime)
		changeBG(fluent_night)
		tims = 46800
		time.sleep(tims)
		restartaf()

	else:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep3 = 46800

		sleeptime = abs(summ - timesleep3)
		changeBG(fluent_night)
		time.sleep(sleeptime)
		restartaf()

if BG == 'F':

	restartaf()

def restartsfa():
	if hour>= 6 and hour<12:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep = 21600

		sleeptime = abs(summ - timesleep)
		changeBG(sf_day)
		time.sleep(sleeptime)
		changeBG(sf_dusk)
		tims = 21600
		time.sleep(tims)
		changeBG(sf_night)
		tims = 46800
		time.sleep(tims)
		restartsfb()
	elif hour>= 12 and hour<18:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep2 = 21600

		sleeptime = abs(summ - timesleep2)
		changeBG(sf_dusk)
		time.sleep(sleeptime)
		changeBG(sf_night)
		tims = 46800
		time.sleep(tims)
		restartsfb()

	else:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep3 = 46800

		sleeptime = abs(summ - timesleep3)
		changeBG(sf_night)
		time.sleep(sleeptime)
		restartsfb()

def restartsfb():
	if hour>= 6 and hour<12:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep = 21600

		sleeptime = abs(summ - timesleep)
		changeBG(sf_day)
		time.sleep(sleeptime)
		changeBG(sf_dusk)
		tims = 21600
		time.sleep(tims)
		changeBG(sf_night)
		tims = 46800
		time.sleep(tims)
		restartsfa()
	elif hour>= 12 and hour<18:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep2 = 21600

		sleeptime = abs(summ - timesleep2)
		changeBG(sf_dusk)
		time.sleep(sleeptime)
		changeBG(sf_night)
		tims = 46800
		time.sleep(tims)
		restartsfa()

	else:
		now = datetime.now().hour
		mnow = datetime.now().minute
		
		nowm = now * 60
		
		nows = nowm * 60
		mnows = mnow * 60
		
		summ = nows + mnows

		timesleep3 = 46800

		sleeptime = abs(summ - timesleep3)
		changeBG(sf_night)
		time.sleep(sleeptime)
		restartsfa()



if BG == 'SF':

	sf_day = input('Input day wallpaper')
	sf_dusk = input('Input dusk wallpaper')
	sf_night = input('Input night wallpaper')

	restartsfa()
