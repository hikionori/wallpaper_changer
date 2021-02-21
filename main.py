'''Avtor: Danila (hikionori) Verbinsky
   Version: 1.0(beta)
'''

import ctypes
import time
import datetime

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

BG = input("Input B(bliss) or F(fluent) and you can select your files just input SF(select files) for stop just press (Ctrl + C) : ")

def changeBG(path):
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

a = 1

if BG == 'B' or BG == 'b':
	while a == 1:
		if hour>= 6 and hour<12:
			changeBG(bliss_day)
			time.sleep(1)
			continue
		elif hour>= 12 and hour<18:
			changeBG(bliss_dusk)
			time.sleep(1)
			continue
		else:
			changeBG(bliss_night)
			time.sleep(1)
			continue

if BG == 'F' or BG == 'f':
	while a == 1:
		if hour>= 6 and hour<12:
			changeBG(fluent_day)
			time.sleep(1)
			continue
		elif hour>= 12 and hour<18:
			changeBG(fluent_dusk)
			time.sleep(1)
			continue
		else:
			changeBG(fluent_night)
			time.sleep(1)
			continue

if BG == 'SF':

	sf_day = input('Input day wallpaper: ')
	sf_dusk = input('Input dusk wallpaper: ')
	sf_night = input('Input night wallpaper: ')

	while a == 1:
		if hour>= 6 and hour<12:
			changeBG(sf_day)
			time.sleep(1)
			continue
		elif hour>= 12 and hour<18:
			changeBG(sf_dusk)
			time.sleep(1)
			continue
		else:
			changeBG(sf_night)
			time.sleep(1)
			continue
