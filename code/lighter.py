# Methods for sending lighting schematic to Rainbowduino
# Input schematic should be an array of arrays
# The values in those arrays should be the number of attacks by each player
import smbus
bus = smbus.SMBus(0)
address = 0x04

def lighter(schematic):
    for rank in len(schematic):
        for file in len(schematic[rank]):
            value = schematic[rank][file]
            pos = rank * 8 + file
            if value > 0:
                bus.write_byte_data(address, 0, 64 + pos)
            elif value == 0:
                bus.write_byte_data(address, 0, pos)
            elif value < 0:
                bus.write_byte_data(address, 0, 128 + pos)
            #need another else case for when squares are attacked equally