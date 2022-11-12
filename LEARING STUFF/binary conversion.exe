#this program converts binary to decimal and vice versa
binary_string=" "
decimal_input=int(float(input('enter any number from 0 to 128\n')))
if 0<= decimal_input <=256 :
    if decimal_input >= 128 :
        binary_string='1'
        decimal_input%=128
    else:
        binary_string='0'

    if decimal_input >=64 :
        binary_string+='1'
        decimal_input%=64
    else :
        binary_string+='0'

    if decimal_input >=32 :
        binary_string+='1'
        decimal_input%=32

    else :
        binary_string+='0'

    if decimal_input >=16 :
        binary_string+='1'
        decimal_input%=16

    else :
        binary_string+='0'

    if decimal_input >=8 :
        binary_string+='1'
        decimal_input%=8

    else :
        binary_string+='0'

    if decimal_input >=4 :
        binary_string+='1'
        decimal_input%=4

    else :
        binary_string+='0'

    if decimal_input >=2 :
        binary_string+='1'
        decimal_input%=1

    else :
        binary_string+='0'


    binary_string+=str(decimal_input)
    print(binary_string)
