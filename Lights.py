#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

import argparse

frequencyFlicker = 240; # Set the output to pulse at 240hz

parser = argparse.ArgumentParser(description='Set light brightness')
parser.add_argument('-r', '--red', help='Red Channel Percentage', required=False)
parser.add_argument('-g', '--green', help='Green Channel Percentage', required=False)
parser.add_argument('-b', '--blue', help='Blue Channel Percentage', required=False)
parser.add_argument('-w', '--white', help='White Channel Percentage', required=False)
args = vars(parser.parse_args())

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)

# Set the PWM frequency
pwm.setPWMFreq(frequencyFlicker)
if args['r'] is not None:
  intPwmTicksOff = float(args['r']) / float(100)
  pwm.setPWM(0,0,intPwmTicksOff)
if args['g'] is not None:
  intPwmTicksOff = float(args['g']) / float(100)
  pwm.setPWM(0,0,intPwmTicksOff)
if args['b'] is not None:
  intPwmTicksOff = float(args['b']) / float(100)
  pwm.setPWM(0,0,intPwmTicksOff)
