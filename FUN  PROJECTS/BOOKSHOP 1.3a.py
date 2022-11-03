"""THIS IS BOOKSHOP 1.03 I REMOVED SOME BULKY CODE WHICH MADE IT REDUNDANT,ADDED A
LOG FILE TO STORE USERLOGS AND BOUGHT ITEMS: I HOPE TO USE CLASSES TO REPLACE LISTS
AND  ADD PASSWORD AND USER ACCOUNTS.

FYI I DONT UNDERSTAND ALGORITHIMS YET

"""
# i later discovered django so this is BS..

from time import sleep
import os

def clear_console():
    os.system('cls')
    


product_codes={
    101:'math Made Familiar 2021',
    102:'english aid 2020',
    103:'bio kcse a+',
    104:'kidagaa kimemwozea',
    105:'pearls of the savannah',
    106:'caucasian chalk circle',
    107:'bic',
    108:'speedo',
    109:'obama'
}



def product_codez():
    print(product_codes)
    
    
def buy_product(code,bought_items):
    item=(product_codes.get(code,'not found'))
    bought_items =bought_items.append(item)
    
    return bought_items

#start of MAIN PROGRAM...

print('-----------welcome to the bookshop database---------------')
firstpage='''\n  :
                    
                    1.SEE PRODUCT CODES
                    2.BUY PRODUCTS
                    3.SEE YOUR SHOPPING CART
'''
bought_items=[]
i=1
print(firstpage)

usr=input('enter user name\n')

choice=int(input('enter the number for your preffered option -> \t'))
#sleep(2)
print('intializing database........')
#sleep(2)
print('optimizing data..............')
sleep(2)

if choice == 1 :
    product_codez()
    choice=int(input('\n now press 2 to fill up your shopping cart\t'))
    
if choice ==2:
    goods= int(input('\n***how many products do you wish to buy ?***** \t'))
    while i <=goods:
        code=int(input('\n enter the product code to continue =>'))
        buy_product(code,bought_items)
        i+=1
    print('\n wow you made a purchase, press 3 to see what you bought')
    choice=int(input())
    clear_console()
if choice==3 and bought_items!=[]:
    print(bought_items)
    
else :
    print('\n SORRY !! you havent bought any items')
sleep(2)    
print('\n````$$$$$$..... THANKS FOR SHOPPING WITH US BYE \t B~)')
sleep(2)


userlogs={}
flag=0

b_items=open('newfile.txt','a')
b_items.write('\n'+'username:'+usr+str(bought_items))
b_items.close()

b_items=open('newfile.txt','r')
for line in b_items:
    if usr in line:
        flag+=1
        
userlogs[usr]=flag
        
b_items.close()
print(userlogs)









             



















