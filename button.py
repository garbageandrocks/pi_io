#!/usr/bin/python

import time   # For sleeping zzzz...

try:
  import RPi.GPIO as GPIO
except RuntimeError:
  print("Error importing RPi.GPIO!  Need sudo!!\n")

gpio_state = {
  'low':  GPIO.LOW,
  'high': GPIO.HIGH,
}

pd_state = {
  'down':  GPIO.PUD_DOWN,
  'up':    GPIO.PUD_UP,
}

gpio_func = {
  'input':    GPIO.IN,        # Input
  'output':   GPIO.OUT,       # Output
  'spi':      GPIO.SPI,       # Serial Peripheral Interface
  'i2c':      GPIO.I2C,       # Inter-Integrated Circuit
  'pwm':      GPIO.HARD_PWM,  # Hardware Pulse Width Modulator
  'serial':   GPIO.SERIAL,    # Serial Interface
  'unknown':  GPIO.UNKNOWN,   # Unknown
}

gpio_func_str = {
  GPIO.IN:        'input',    # Input
  GPIO.OUT:       'output',   # Output
  GPIO.SPI:       'spi',      # Serial Peripheral Interface
  GPIO.I2C:       'i2c',      # Inter-Integrated Circuit
  GPIO.HARD_PWM:  'pwm',      # Hardware Pulse Width Modulator
  GPIO.SERIAL:    'serial',   # Serial Interface
  GPIO.UNKNOWN:   'unknown',  # Unknown
}

gpio_bcm_mapping = {
  'BCM0':  0,   # ID_SD
  'BCM1':  1,   # ID_SC
  'BCM2':  2,   # SDA
  'BCM3':  3,   # SCL
  'BCM4':  4,   # GPCLK0
  'BCM5':  5,
  'BCM6':  6,
  'BCM7':  7,   # CE1
  'BCM8':  8,   # CE0
  'BCM9':  9,   # MISO
  'BCM10': 10,  # MOSI
  'BCM11': 11,  # SCLK
  'BCM12': 12,  # PWMO
  'BCM13': 13,  # PWM1
  'BCM14': 14,  # TXD
  'BCM15': 15,  # RXD
  'BCM16': 16,
  'BCM17': 17,
  'BCM18': 18,  # PWM0
  'BCM19': 19,  # MISO
  'BCM20': 20,  # MOSI
  'BCM21': 21,  # SCLK
  'BCM22': 22,
  'BCM23': 23,
  'BCM24': 24,
  'BCM25': 25,
  'BCM26': 26,
  'BCM27': 27,
}

pins = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,}

def print_chan_func():
  for x in (pins):
    print("Channel : " + str(x) + " is set to " + gpio_func_str[GPIO.gpio_function(x)] + "\n")

def print_RPi_info():
  out_str = "Print Info about RPi:\n" + str(GPIO.RPI_INFO) + "\n"
  print(out_str)

def print_GPIO_version():
  out_str = "Print Rpi.GPIO version: " + str(GPIO.VERSION)  + "\n"
  print(out_str)

def setup_inputs(gpio_in, pd):
  for x in xrange(0, len(gpio_in)):
    GPIO.setup(gpio_in[x], gpio_func['input'], pd[x])

def setup_outputs(gpio_out, init_val):
  for x in xrange(0, len(gpio_out)):
    GPIO.setup(gpio_out[x], gpio_func['output'], initial=init_val[x])

def toggle_outputs(gpio_out):
  for x in xrange(0, len(gpio_out)):
    GPIO.output(gpio_out[x], not GPIO.input(gpio_out[x]))

def main():

  print_RPi_info()
  print_GPIO_version()

  # BCM Numbering (Channel numbers on the Broadcom SOC)
  GPIO.setmode(GPIO.BCM)

  # Disable GPIO warnings (Warnings occur when another script is using GPIO)
  GPIO.setwarnings(False)

  # Map Channels
  gpio_in  = [5, 6]
  pd = [pd_state['down'], pd_state['up']]

  gpio_out = [13, 19]
  init_val = [gpio_state['low'], gpio_state['high']]

  setup_inputs(gpio_in, pd)
  setup_outputs(gpio_out, init_val)

  button_pressed = None

  print_chan_func()

  no = "no"
  yes = "yes"

  while True:

    print("ZZZzzzz...\n")
    button_pressed = GPIO.wait_for_edge(gpio_in[0], GPIO.BOTH, timeout=5000)

    if button_pressed != None:
      print("Button has been pressed!!  Toggle output channel states..\n")
      toggle_outputs(gpio_out)
    else:
      print("No button pressed :((\n")

    stop = input("Do you want to quit? (yes or no)\n")

    if stop == yes:
      print("Bye Bye, Baby Bitch\n")
      break
    elif stop == no:
      print("Fine, let's do this\n")

  print("Cleaning up\n")
  GPIO.cleanup()

main()
