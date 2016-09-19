import smbus
import time

bus = smbus.SMBus(1)

addr = 0x38
cntrl = 0x00
cntrl_val = 0x10


bus.write_byte_data(addr,cntrl,0x00)

bus.write_byte_data(addr,cntrl,cntrl_val)

time.sleep(1)

bus.write_byte_data(addr,cntrl,0x00)
