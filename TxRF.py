import time
import sys
import RPi.GPIO as GPIO
from moteLib import *
#a_on = '1111111111111010101011101'
#a_off = '1111111111111010101010111'
#b_on = '1111111111101110101011101'
#b_off = '1111111111101110101010111'
#c_on = '1111111111101011101011101'
#c_off = '1111111111101011101010111'
#d_on = '1111111111101010111011101'
#d_off = '1111111111101010111010111'
#short_delay = 0.00045
#long_delay = 0.00090
#extended_delay = 0.0096
"""
MOTE_A_PP = '01010100000001111000'
MOTE_B_PP = '01000100011001011000'

MOTE_A = 'A'
MOTE_B = 'B'
MOTE_W = 'W'

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

b_short_delay = 0.00029
b_long_delay = 0.00082
b_extended_delay = 0.008539

#a_short_delay = 0.00027
#a_long_delay = 0.00083
#a_extended_delay = 0.0086

a_short_delay = b_short_delay
a_long_delay = b_long_delay
a_extended_delay = b_extended_delay
"""

NUM_ATTEMPTS = 25
TRANSMIT_PIN = 22

def transmit_code(code,mote):
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
    print 'Trasmitting...'
    print "Delays (s,l,e) = %f,%f,%f"%(short_delay,long_delay,extended_delay)
    for t in range(NUM_ATTEMPTS):
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

if __name__ == '__main__':
    for argument in sys.argv[1:]:
        if str(argument).find('MOTE_A') != -1:
            exec('transmit_code(' + str(argument) + ',' + str('MOTE_A') + ')')
        elif str(argument).find('MOTE_B') != -1:
            exec('transmit_code(' + str(argument) + ',' + str('MOTE_B') + ')')
        elif str(argument).find('MOTE_C') != -1:
            exec('transmit_code(' + str(argument) + ',' + str('MOTE_C') + ')')
        elif str(argument).find('MOTE_D') != -1:
            exec('transmit_code(' + str(argument) + ',' + str('MOTE_D') + ')')
        elif str(argument).find('MOTE_U') != -1:
            exec('transmit_code(' + str(argument) + ',' + str('MOTE_U') + ')')
        elif str(argument).find('MOTE_V') != -1:
            exec('transmit_code(' + str(argument) + ',' + str('MOTE_V') + ')')
        elif str(argument).find('MOTE_W') != -1:
            exec('transmit_code(' + str(argument) + ',' + str('MOTE_W') + ')')
        elif str(argument).find('MOTE_X') != -1:
            exec('transmit_code(' + str(argument) + ',' + str('MOTE_X') + ')')

