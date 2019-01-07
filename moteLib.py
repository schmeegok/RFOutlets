MOTE_A_PP = '01010100000001111000'
MOTE_B_PP = '01000100011001011000'
MOTE_A = 'A'
MOTE_B = 'B'

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

short_delay    = 0.00029
long_delay     = 0.00082
extended_delay = 0.008539

a_short_delay    = short_delay
a_long_delay     = long_delay
a_extended_delay = extended_delay

b_short_delay    = short_delay
b_long_delay     = long_delay
b_extended_delay = extended_delay

# C
MOTE_C_PP  = '00100111011111111010'
MOTE_C_PPI = '11011000100000000101'
MOTE_C = 'C'


MOTE_C_I_ON    = MOTE_C_PP + '11101'
MOTE_C_I_ON_I  = MOTE_C_PPI + '00010'
MOTE_C_I_OFF   = MOTE_C_PP + '10011'
MOTE_C_I_OFF_I = MOTE_C_PPI + '01100'
MOTE_C_II_ON   = MOTE_C_PP + '11011'
MOTE_C_II_OFF  = MOTE_C_PP + '01101'
MOTE_C_III_ON  = MOTE_C_PP + '10111'
MOTE_C_III_OFF = MOTE_C_PP + '01111'

c_short_delay    = 0.00018
c_long_delay     = 0.00092
c_extended_delay = 0.00855

# HLRC23PK (RCTM3PK) FCCID: QJX-004
MOTE_D_PP = '11111110000101000101'
MOTE_D = 'D'

MOTE_D_I_ON    = MOTE_D_PP + '11101'
MOTE_D_I_OFF   = MOTE_D_PP + '10011'
MOTE_D_II_ON   = MOTE_D_PP + '11011'
MOTE_D_II_OFF  = MOTE_D_PP + '01101'
MOTE_D_III_ON  = MOTE_D_PP + '10111'
MOTE_D_III_OFF = MOTE_D_PP + '01111'

d_short_delay    = 0.00029
d_long_delay     = 0.00082
d_extended_delay = 0.008539

# TR-011, FCCID: PAGTR-011, IC:4494A-TR011
MOTE_W_PP = '1001011111'
MOTE_W = 'W'

MOTE_W_ON = MOTE_W_PP + '010011' #ON
MOTE_W_OFF = MOTE_W_PP + '100011' #OFF
w_short_delay    = 0.0006
w_long_delay     = 0.0018
w_extended_delay = 0.012  #0.011846

# TR-011, FCCID: PAGTR-011, IC: 4494A-TR011
MOTE_X_PP = '100101'
MOTE_X = 'X'

MOTE_X_1_ON  = MOTE_X_PP + '1101111011'
MOTE_X_1_OFF = MOTE_X_PP + '1110111011'
MOTE_X_2_ON  = MOTE_X_PP + '1111011011'
MOTE_X_2_OFF = MOTE_X_PP + '1111101011'
MOTE_X_3_ON  = MOTE_X_PP + '1011111011'
MOTE_X_3_OFF = MOTE_X_PP + '0111111011'

x_short_delay    = 0.0006
x_long_delay     = 0.0018
x_extended_delay = 0.012  #0.011846

# UTTNOREM2 (RCTM21), FCCID: QJX-TXTNRC (PRIME OUTDOOR) #not working for some reason
MOTE_V_PP = '101100111111011010111'
MOTE_V = 'V'

MOTE_V_ON  = MOTE_V_PP +'1101'
MOTE_V_OFF = MOTE_V_PP +'0011'
v_short_delay    = a_short_delay
v_long_delay     = a_long_delay
v_extended_delay = a_extended_delay

# UTTNOREM2 (RCTM21), FCCID: QJX-TXTNRC (PRIME OUTDOOR) #not working for some reason
MOTE_U_PP = '111111011001100000111'
MOTE_U = 'U'

MOTE_U_ON  = MOTE_U_PP + '1101'
MOTE_U_OFF = MOTE_U_PP + '0011'
u_short_delay    = 0.00028
u_long_delay     = 0.00082
u_extended_delay = 0.00856

