import datetime
import os
import time
import random
import subprocess
import random
import platform
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='immediately trigger alarm')
args = parser.parse_args()

if not args.debug:
	import getAlarm
	wakeupTime = getAlarm.wakeupTime

	theFinalCountdown = (wakeupTime - datetime.datetime.now()).seconds
	print("Sleeping for", theFinalCountdown, "seconds")
	time.sleep(theFinalCountdown)
else:
	print("Entering debug mode, triggering alarm immediately")

# Time for the alarm to go off
print("Wake Up!")
import cal
import weather



if platform.system() == "Darwin":
	#it's running on my MBP
	command = "say"
	with open("/Users/jaspergilley/Code/alarmed/greetings.txt", 'r') as f:
		greetings = f.read().split("\n")
else:
	#it's running on RPi
	command = "espeak"
	with open("/home/pi/Code/alarmed/greetings.txt", 'r') as f:
		greetings = f.read().split("\n")
	subprocess.call(["omxplayer", "--vol", "-600", "/home/pi/Code/alarmed/audio/Collins Avenue Short.caf"])

finalText = random.choice(greetings) + " " + weather.toSpeak + " " + cal.toSpeak
print(finalText)

subprocess.call([command, "'{}'".format(finalText)])