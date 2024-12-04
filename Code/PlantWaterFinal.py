# ECE 1000 Automatic Plant Watering System trial mk1
# Tyler Beerman, tmbeerman42@tntech.edu & Dominic Duong, dlduong42@tntech.edu

# Introduction:

from PicoBreadboard import LED, BUZZER, BUTTON
from machine import ADC, Pin
import utime

MoistureValue = ADC(Pin(28)) # create class for sensor and set the sensor to GP28
Pump = Pin(17, Pin.OUT) # create class for pump and set it to GP17
 
DrySoil = 53000 # set the threshold for dry soil to 53000
WetSoil = 30000 # set the threshold for wet soil to 30000

def Runpump(): # runs pump for half a second, turns it off, and back on
    Pump.value(1) # pump on
    utime.sleep(0.5)
    Pump.value(0) # pump off
    utime.sleep(2)
    Pump.value(1)

while 1:
    Moisture = MoistureValue.read_u16() # read the sensor value
    if Moisture <= WetSoil: # sees the moisture level is good
        print("Plant Was Just Watered")
    if WetSoil < Moisture < DrySoil: # sees the moisture level is good
        print("Plant Does Not Need Watered")
    if Moisture >= DrySoil: # sees the moisture level is too low
        print("Plant Needs To Be Watered")
        Runpump() # waters the plant
    utime.sleep(3)
