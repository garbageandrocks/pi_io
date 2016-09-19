#!/usr/bin/python

import time   # For sleeping zzzz...

try:
  import RPi.GPIO as GPIO
except RuntimeError:
  print("Error importing RPi.GPIO!  Need sudo!!\n")

gpio_mode = [ GPIO.BOARD, GPIO.BCM, None ]

gpio_state = [ GPIO.LOW, GPIO.HIGH ]

gpio_bcm_mapping = {
  "BCM0": 0,    # ID_SD
  "BCM1": 1,    # ID_SC
  "BCM2": 2,    # SDA
  "BCM3": 3,    # SCL
  "BCM4": 4,    # GPCLK0
  "BCM5": 5,
  "BCM6": 6,
  "BCM7": 7,    # CE1
  "BCM8": 8,    # CE0
  "BCM9": 9,    # MISO
  "BCM10": 10,  # MOSI
  "BCM11": 11,  # SCLK
  "BCM12": 12,  # PWMO
  "BCM13": 13,  # PWM1
  "BCM14": 14,  # TXD
  "BCM15": 15,  # RXD
  "BCM16": 16,
  "BCM17": 17,
  "BCM18": 18,  # PWM0
  "BCM19": 19,  # MISO
  "BCM20": 20,  # MOSI
  "BCM21": 21,  # SCLK
  "BCM22": 22,
  "BCM23": 23,
  "BCM24": 24,
  "BCM25": 25,
  "BCM26": 26,
  "BCM27": 27,
}

# Discover info about RPi
out_str = "Print Info about RPi:\n" + str(GPIO.RPI_INFO) + "\n"
print(out_str)

# Discover Raspberry Pi Board Revision
out_str = "Print Raspberry Pi Board Revision:\n" + str(GPIO.RPI_INFO['P1_REVISION']) + "\n"
print(out_str)

# Discover version of RPi.GPIO
out_str = "Print Rpi.GPIO version:\n" + str(GPIO.VERSION)  + "\n"
print(out_str)

# Set IO pin numbering

# Board Numbering (Numbers of P1 header of the Raspberry Pi board
GPIO.setmode(GPIO.BCM)

# BCM Numbering (Channel numbers on the Broadcom SOC)
# GPIO.setmode(GPIO.BCM)

# Check which pin numbering mode has been set
mode = GPIO.getmode()

if mode == gpio_mode[0]:
  print("Pin Numbering mode is Board\n")
elif mode == gpio_mode[1]:
  print("Pin Numbering mode is BCM\n")
elif mode == gpio_mode[2]:
  print("No Pin Numbering mode selected!\n")
else:
  print("Invalid mode!\n")

# Disable GPIO warnings (Warnings occur when another script is using GPIO)
GPIO.setwarnings(False)

# Setup a channel as input
in_chan = 5

GPIO.setup(in_chan, GPIO.IN)

# Setup a channel as output, and initialize to value HIGH
out_chan = 6

out_str = "Output pin: " + str(out_chan) + " is going high.\n"
print(out_str)

GPIO.setup(out_chan, GPIO.OUT, initial=GPIO.HIGH)

print("Sleeping for 5 seconds\n")

time.sleep(5)

# Setup multiple channels with one setup call

out_chans = [13,19]  # Works with lists and tuples

print("Setup channels " + str(out_chans[0]) + " and " + str(out_chans[1]) + " without inititialization\n") 

GPIO.setup(out_chans, GPIO.OUT)

print("Sleeping for 5 seconds\n")

time.sleep(5)


# Read the value of a GPIO pin:

in_chan_val = GPIO.input(in_chan)

if in_chan_val == gpio_state[0]:
  print("Input 1 is low\n")
elif in_chan_val == gpio_state[1]:
  print("Input 1 is high\n")
else:
  print("Input 1 is undefined?\n")

# Set the output state

out_chan_val = GPIO.LOW

out_str = "Output pin: " + str(out_chan) + " is being set to low.\n" 

print(out_str)

GPIO.output(out_chan, out_chan_val)

print("Sleeping for 5 seconds\n")

time.sleep(5)

# Set the output state of multiple output channels with one call

out_chans_val = [GPIO.HIGH, GPIO.LOW]

for x in xrange(0, 2):
  out_str = "Output pin: " + str(out_chans[x]) + " is being set to: " + str(out_chans_val[x]) + ".\n" 
  print(out_str)

GPIO.output(out_chans, GPIO.LOW)              # Set both to low
GPIO.output(out_chans, (out_chans_val[0], out_chans_val[1]))   # Set first to high, second to low

print("Sleeping for 5 seconds\n")

time.sleep(5)

for x in xrange(0, 2):
  out_str = "Output pin: " + str(out_chans[x]) + " is being set to: " + str(out_chans_val[1-x]) + ".\n" 
  print(out_str)

GPIO.output(out_chans, (out_chans_val[1], out_chans_val[0]))   # Set first to high, second to low

print("Sleeping for 5 seconds\n")

time.sleep(5)

# Cleanup
# return all channels to inputs with no pull up/down
# clear pin numbering mode

print("Cleaning up\n")

# Cleanup individual channels or list or tuple of channels
GPIO.cleanup(in_chan)
GPIO.cleanup(out_chan)
GPIO.cleanup(out_chans)

GPIO.cleanup()

