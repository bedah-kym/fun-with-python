
"""Here i create a random  number generator by using the function _flip_
to create a string of random zeros and ones  in a binary string and feeding the
result to a binary to decimal converter function"""

from random import randrange
coin_start=[]
stack=[128,64,32,16,8,4,2,1]
decimal=0
#like a coin flip the state can only be a 1 or 0 for each bit of an 8 character string
def flip():
    for x in range (0,8):
        
        y=randrange(0,2)
        coin_start.append(y)

    print(coin_start)
         
#binary string from flip converted to decimal
    
def binary_conv(coin_start,decimal,stack):
    for x in range(0,8,) :
        
        if coin_start[x]==1:
            decimal+=stack[x]
            
        else:
            decimal+=0       
    
    print(decimal)

newrand=flip(),binary_conv(coin_start,decimal,stack)

