import re

num = '078677515'

pattern = r'^("+254"|"0"),[0-9]{9}$'

x = re.search(pattern , num)
"""
x=""
#just a longer way to do it
try:

    if num[1] == '+' or num[1] =='0':
        
        num = 'invalid'
        x=None
    else:
        if num[0]=='0':
            num=num[1:]
            x = re.search("\d{9}$", num)
        elif num[0]=='+':
            num=num[4:]
            x = re.search("\d{9}$", num)
            
    num = '0'+ x.group()
    
except (IndexError):
    num = 'invalid'
    x=None

"""
if  x == None:
    print('false',x)
else:
    print('True',x)
1
