import ctypes
from datetime import datetime
import time
import math


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

BG = input("Введи B(bliss) или F(fluent) : ")

def restartab():
	'''Это функция которая высывает другую функцию которая вызывает эту для BLISS'''
	if hour>= 6 and hour<12:
		changeBG(bliss_day)
		restartbb()
	elif hour>= 12 and hour<18:
		changeBG(bliss_dusk)
		restartbb()
	else:
		changeBG(bliss_night)
		restartbb()

def restartbb():
	if hour>= 6 and hour<12:
		changeBG(bliss_day)
		restartab()
	elif hour>= 12 and hour<18:
		changeBG(bliss_dusk)
		restartab()
	else:
		changeBG(bliss_night)
		restartab()


if BG == 'B':
		
	restartab()

def restartaf():
	if hour>= 6 and hour<12:
		changeBG(fluent_day)
		restartbf()
	elif hour>= 12 and hour<18:
		changeBG(fluent_dusk)
		restartbf()
	else:
		changeBG(fluent_night)
		restartbf()

def restartbf():
	if hour>= 6 and hour<12:
		changeBG(fluent_day)
		restartaf()
	elif hour>= 12 and hour<18:
		changeBG(fluent_dusk)
		restartaf()
	else:
		changeBG(fluent_night)
		restartaf()

if BG == 'F':

	restartaf()