#!/usr/bin/env python

import RPi.GPIO as gpio
import time
import subprocess

ch = 2

gpio.setmode(gpio.BCM)
gpio.setup(ch, gpio.OUT, initial = gpio.HIGH)

# while True:
#     time.sleep(1)

# turn off
subprocess.run("sync", shell = True)
gpio.output(ch, gpio.LOW)

# this stuff will likely never happen
time.sleep(10)
gpio.cleanup(ch)
