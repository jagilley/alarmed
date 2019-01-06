import datetime
import os
import time
import random
import subprocess
import random
import platform

import getAlarm
wakeupTime = getAlarm.wakeupTime

theFinalCountdown = (wakeupTime - datetime.datetime.now()).seconds
print("Sleeping for", theFinalCountdown, "seconds")

#time.sleep(theFinalCountdown)

# Time for the alarm to go off
print("Wake Up!")
import cal
import weather

with open("/Users/jaspergilley/Code/alarmed/greetings.txt", 'r') as f:
	greetings = f.read().split("\n")

finalText = random.choice(greetings) + " " + weather.toSpeak + " " + cal.toSpeak
print(finalText)

if platform.system() == "Darwin":
	#it's running on my MBP
	command = "say"
else:
	#it's running on RPi
	command = "espeak"

subprocess.call([command, "'{}'".format(finalText)])