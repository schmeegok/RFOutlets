import time
import sys
import RPi.GPIO as GPIO

from moteLib import *

MOTE_A_PP = '01010100000001111000'
MOTE_B_PP = '01000100011001011000'

"""
MOTE_B_I_ON    = MOTE_B_PP + '11101'
MOTE_B_I_OFF   = MOTE_B_PP + '10011'
MOTE_B_II_ON   = MOTE_B_PP + '11011'
MOTE_B_II_OFF  = MOTE_B_PP + '01101'
MOTE_B_III_ON  = MOTE_B_PP + '10111'
MOTE_B_III_OFF = MOTE_B_PP + '01111'

MOTE_A_I_ON    = MOTE_A_PP + '11101'
MOTE_A_I_OFF   = MOTE_A_PP + '10011'
MOTE_A_II_ON   = MOTE_A_PP + '11011'
MOTE_A_II_OFF  = MOTE_A_PP + '01101'
MOTE_A_III_ON  = MOTE_A_PP + '10111'
MOTE_A_III_OFF = MOTE_A_PP + '01111'

short_delay = 0.00029
long_delay = 0.00082
extended_delay = 0.008539
"""

#NUM_ATTEMPTS = 15
TRANSMIT_PIN = 22

def transmit_code(code,mote,attempts):
    '''Transmit a chosen code string using the GPIO transmitter'''
    
    # Figure delays first
    if mote == 'A' or mote == 'B' or mote == 'V':
        short_delay    = a_short_delay
        long_delay     = a_long_delay
        extended_delay = a_extended_delay
    elif mote == 'C':
        #short_delay    = c_short_delay
        #long_delay     = c_long_delay
        #extended_delay = c_extended_delay
        short_delay    = 0.00029
        long_delay     = 0.00082
        extended_delay = 0.008539
    elif mote == 'D':
        short_delay    = d_short_delay
        long_delay     = d_long_delay
        extended_delay = d_extended_delay
    elif mote == 'U':
        short_delay = u_short_delay
        long_delay  = u_long_delay
        extended_delay = u_extended_delay
        print 'USING U DELAYS'
    elif mote == 'W':
        short_delay    = w_short_delay
        long_delay     = w_long_delay
        extended_delay = w_extended_delay
    elif mote == 'X':
        short_delay    = x_short_delay
        long_delay     = x_long_delay
        extended_delay = x_extended_delay
    else:
        short_delay    = a_short_delay
        long_delay     = a_long_delay
        extended_delay = a_extended_delay
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
    for t in range(attempts):
        for i in code:
            if i == '1':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(short_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(long_delay)
            elif i == '0':
                GPIO.output(TRANSMIT_PIN, 1)
                time.sleep(long_delay)
                GPIO.output(TRANSMIT_PIN, 0)
                time.sleep(short_delay)
            else:
                continue
        GPIO.output(TRANSMIT_PIN, 0)
        time.sleep(extended_delay)
    GPIO.cleanup()
    
def lightsOn_NORMAL(attempts = 5):
    # ICICLE MAIN
    transmit_code(MOTE_A_III_ON,'A',attempts)
    time.sleep(5)
    # ICICLE_LOWER
    transmit_code(MOTE_D_III_ON,'D',attempts)
    transmit_code(MOTE_D_III_ON,'D',attempts)
    transmit_code(MOTE_X_1_ON,'X',attempts)
    # ICICLE UPPER
    transmit_code(MOTE_X_2_ON,'X',attempts)
    transmit_code(MOTE_X_3_ON,'X',attempts)
    # WINDOW RIGHT
    transmit_code(MOTE_A_I_ON,'A',attempts)
    transmit_code(MOTE_B_I_ON,'B',attempts)
    # WINDOW LEFT
    transmit_code(MOTE_A_II_ON,'A',attempts)
    transmit_code(MOTE_B_II_ON,'B',attempts)
    # WINDOW ODD
    transmit_code(MOTE_B_III_ON,'B',attempts)
    
    timeLightsOn = time.localtime()
    print "Normal - Lights ON: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)
    
def lightsOn_P1(attempts = 7):
    # ICICLE MAIN
    transmit_code(MOTE_A_III_ON,'A',attempts)
    time.sleep(5)
    # ICICLE_LOWER RIGHT
    transmit_code(MOTE_D_III_ON,'D',attempts)
    transmit_code(MOTE_A_I_ON,'A',attempts)
    transmit_code(MOTE_A_II_ON,'A',attempts)
    time.sleep(1.3)
    # ICICLE UPPER LEFT
    transmit_code(MOTE_X_3_ON,'X',attempts)
    transmit_code(MOTE_B_III_ON,'X',attempts)
    time.sleep(1.4)
    # ICICLE LOWER LEFT
    transmit_code(MOTE_X_1_ON,'X',attempts)
    time.sleep(1.5)
    # ICICLE UPPER RIGHT
    transmit_code(MOTE_X_2_ON,'X',attempts)
    transmit_code(MOTE_B_I_ON,'B',attempts)
    transmit_code(MOTE_B_II_ON,'B',attempts)
    time.sleep(1.5)
    
    timeLightsOn = time.localtime()
    print "P1 - Lights ON: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)

def lightsOn_P2(attempts = 7):
    # ICICLE MAIN
    transmit_code(MOTE_A_III_ON,'A',attempts)
    time.sleep(5)
    # ICICLE RIGHT
    transmit_code(MOTE_D_III_ON,'D',attempts)
    transmit_code(MOTE_X_2_ON,'X',attempts)
    transmit_code(MOTE_A_I_ON,'A',attempts)
    transmit_code(MOTE_B_I_ON,'B',attempts)
    transmit_code(MOTE_A_II_ON,'A',attempts)
    transmit_code(MOTE_B_II_ON,'B',attempts)
    time.sleep(1.5)
    # ICICLE LEFT
    transmit_code(MOTE_X_1_ON,'X',attempts)
    transmit_code(MOTE_X_3_ON,'X',attempts)
    transmit_code(MOTE_B_III_ON,'X',attempts)
    time.sleep(1.4)
        
    timeLightsOn = time.localtime()
    print "P2 - Lights ON: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)
    
def lightsOff():    
    transmit_code(MOTE_A_III_OFF,'A',20)
    transmit_code(MOTE_A_I_OFF,'A',20)
    transmit_code(MOTE_B_I_OFF,'B',20)
    transmit_code(MOTE_A_II_OFF,'A',20)
    transmit_code(MOTE_B_II_OFF,'A',20)
    transmit_code(MOTE_B_III_OFF,'B',20)
    # String D Outlets
    transmit_code(MOTE_D_I_OFF,'D',20)
    transmit_code(MOTE_D_II_OFF,'D',20)
    transmit_code(MOTE_D_III_OFF,'D',20)
    timeLightsOn = time.localtime()
    print "Lights OFF: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)

def villageOn(attempts=20):
    # String D Outlets
    transmit_code(MOTE_D_II_ON,'D',attempts)  # Village
    timeLightsOn = time.localtime()
    print "Village ON: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)

def villageOff(attempts=20):
    # String D Outlets
    transmit_code(MOTE_D_II_OFF,'D',attempts)  # Village
    timeLightsOn = time.localtime()
    print "Village OFF: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)

def treeOn(attempts=20):
    # String D Outlets
    transmit_code(MOTE_D_I_ON,'D',attempts)  # Tree
    timeLightsOn = time.localtime()
    print "Tree ON: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)    

def treeOff(attempts=20):
    # String D Outlets
    transmit_code(MOTE_D_I_OFF,'D',attempts)  # Tree
    timeLightsOn = time.localtime()
    print "Tree OFF: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)    
    
def stairsOn(attempts=20):
    # String D Outlets
    transmit_code(MOTE_W_ON,'W',attempts)  # Stairs
    timeLightsOn = time.localtime()
    print "Stairs ON: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)    

def stairsOff(attempts=20):
    # String D Outlets
    transmit_code(MOTE_W_OFF,'W',attempts)  # Stairs
    timeLightsOn = time.localtime()
    print "Stairs OFF: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)    
    
def plantsOn(attempts=20):
    # String W Outlets
    transmit_code(MOTE_W_ON,'W',attempts)  # Plants
    timeLightsOn = time.localtime()
    print "Plants ON: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)    

def plantsOff(attempts=20):
    # String W Outlets
    transmit_code(MOTE_W_OFF,'W',attempts)  # Plants
    timeLightsOn = time.localtime()
    print "Plants OFF: %i-%i-%i, %i:%i:%i"%(timeLightsOn.tm_mon, timeLightsOn.tm_mday, timeLightsOn.tm_year, timeLightsOn.tm_hour, timeLightsOn.tm_min, timeLightsOn.tm_sec)    

if __name__ == '__main__':
    
    # TEST
    
    # Run Forever        
    while True:
        # Snapshot time
        currentTime = time.localtime()

        # Turn on Plants at 6:00:00 AM
        if currentTime.tm_hour == 6 and currentTime.tm_min == 0 and currentTime.tm_sec == 0:
            plantsOn(30)
            
        # Turn off plants at 9:00 PM
        if currentTime.tm_hour == 7 and currentTime.tm_min == 0 and currentTime.tm_sec == 0:
            treeOff(20)
            villageOff(20)
            stairsOff(20)
            
        # Turn on lights at 4:00:00 PM
        if currentTime.tm_hour == 16 and currentTime.tm_min == 0 and currentTime.tm_sec == 0:
            lightsOff()
            time.sleep(10)
            lightsOn_P1(10)
            treeOn(20)
            villageOn(20)
            stairsOn(20)
        """
        if currentTime.tm_hour == 17 and currentTime.tm_min == 0 and currentTime.tm_sec == 0:
            lightsOff()
            
        # Turn on lights at 5:00:30 PM - 6:00 PM
        if currentTime.tm_hour == 17 and currentTime.tm_min == 0 and currentTime.tm_sec == 30:
            lightsOn_P2(10)
        if currentTime.tm_hour == 18 and currentTime.tm_min == 0 and currentTime.tm_sec == 0:
            lightsOff()
            
        # Turn on lights at 6:00:30 PM - 7:00 PM
        if currentTime.tm_hour == 18 and currentTime.tm_min == 0 and currentTime.tm_sec == 30:
            lightsOn_P1(10)
        if currentTime.tm_hour == 19 and currentTime.tm_min == 0 and currentTime.tm_sec == 0:
            lightsOff()
            
        # Turn on lights at 7:00:30 PM - 8:00 PM
        if currentTime.tm_hour == 19 and currentTime.tm_min == 0 and currentTime.tm_sec == 30:
            lightsOn_P2(10)
        if currentTime.tm_hour == 20 and currentTime.tm_min == 0 and currentTime.tm_sec == 0:
            lightsOff()
            
        # Turn on lights at 8:00:30 PM - 9:00 PM
        if currentTime.tm_hour == 20 and currentTime.tm_min == 0 and currentTime.tm_sec == 30:
            lightsOn_P1(10)
        if currentTime.tm_hour == 21 and currentTime.tm_min == 0 and currentTime.tm_sec == 0:
            lightsOff()
            
        # Turn on lights at 9:00:30 PM - 10:00 PM
        if currentTime.tm_hour == 21 and currentTime.tm_min == 0 and currentTime.tm_sec == 30:
            lightsOn_NORMAL(10)
        """
        if currentTime.tm_hour == 22 and currentTime.tm_min == 0 and currentTime.tm_sec == 0:
            lightsOff()
            
        if currentTime.tm_hour == 22 and currentTime.tm_min == 15 and currentTime.tm_sec == 0:
            lightsOff()
