#!/usr/bin/python

import time   # For sleeping zzzz...
import spidev # Spi interface

def ReverseBits(byte):
  byte = ((byte & 0xF0) >> 4) | ((byte & 0x0F) << 4)
  byte = ((byte & 0xCC) >> 2) | ((byte & 0x33) << 2)
  byte = ((byte & 0xAA) >> 1) | ((byte & 0x55) << 1)
  return byte
#end def

def BytesToHex(Bytes):
   return ''.join(["0x%02X " % x for x in Bytes]).strip()
#end def

# for 23k256 SRAM IC
instruction_set_23k256 = {
  'read':   0x03,     # read data from memory array beginning at selected address
  'write':  0x02,     # write data to memory array beginning at selected address
  'rdsr':   0x05,     # read STATUS register
  'wrsr':   0x01,     # write STATUS register
}

# BYTE sequence 23k256
# Instruction, 16-bit Address, Data

# Status Register 23k256
# 7 6 5 4 3 2 1 0
# M M 0 0 0 0 0 H

# Mode truth table
# 0 0 = Byte mode (default)
# 1 0 = Page mode
# 0 1 = Sequential mode
# 1 1 = Reserved

# Hold bit
# 0 = pin brought to low (enables hold funtionality
# 1 = hold disabled

spi = spidev.SpiDev()   # create spi object

spi.open(0,0)           # open spi port 0, device (CS) 0

try:
  while True:
    resp = spi.xfer2([0x03,0x00])    # transfer one read instruction
    print("Response from device: " + str(resp) + "\n")
    time.sleep(1)             # sleep for 1 seconds
  #end while

except KeyboardInterrupt:       # Ctrl+C pressed, so...
  spi.close()                   # close the port before exit
#end try
