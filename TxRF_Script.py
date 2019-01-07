import time
import sys
import RPi.GPIO as GPIO

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
MOTE_A_PP = '01010100000001111000'
MOTE_B_PP = '01000100011001011000'

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


NUM_ATTEMPTS = 15
TRANSMIT_PIN = 22

def transmit_code(code):
    '''Transmit a chosen code string using the GPIO transmitter'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRANSMIT_PIN, GPIO.OUT)
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
    #for argument in sys.argv[1:]:
    #    exec('transmit_code(' + str(argument) + ')')
    time.sleep(60)
    i = 0
    while i <= 5:
        print "Running Part One (loops: %i)"%i
        if i == 0:
            dLay = 1.5
        elif i%2 == 0:
            dLay = 1.5
        else:
            dLay = 0.5
        transmit_code(MOTE_A_III_ON)
        time.sleep(dLay)
        transmit_code(MOTE_A_I_ON)
        transmit_code(MOTE_B_I_ON)
        time.sleep(dLay)
        transmit_code(MOTE_A_II_ON)
        transmit_code(MOTE_B_II_ON)
        time.sleep(dLay*3)
        transmit_code(MOTE_B_III_ON)
        
        # Let run for a while
        time.sleep(30*60)
    
        transmit_code(MOTE_A_III_OFF)
        time.sleep(dLay)
        transmit_code(MOTE_A_I_OFF)
        transmit_code(MOTE_B_I_OFF)
        time.sleep(dLay)
        transmit_code(MOTE_A_II_OFF)
        transmit_code(MOTE_B_II_OFF)
        time.sleep(dLay)
    
        time.sleep(10)
    
        print "Running Part Two (loops: %i)"%i
        transmit_code(MOTE_A_III_ON)
        transmit_code(MOTE_A_I_ON)
        transmit_code(MOTE_B_I_ON)
        transmit_code(MOTE_A_II_ON)
        transmit_code(MOTE_B_II_ON)
    
        # Let this run for a while
        time.sleep(30*60)
    
        transmit_code(MOTE_A_III_OFF)
        time.sleep(dLay)
        transmit_code(MOTE_A_I_OFF)
        transmit_code(MOTE_B_I_OFF)
        time.sleep(dLay)
        transmit_code(MOTE_A_II_OFF)
        transmit_code(MOTE_B_II_OFF)
        time.sleep(dLay)
        transmit_code(MOTE_B_III_OFF)
        
        time.sleep(10)
        
        i += 1
    

