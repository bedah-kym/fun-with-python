"""THIS IS BOOKSHOP 1.03 I REVOVED SOME BULKY CODE WHICH MADE IT REDUNDANT,ADDED A
LOG FILE TO STORE USERLOGS AND BOUGHT ITEMS: I HOPE TO USE CLASSES TO REPLACE LISTS
AND  ADD PASSWORD AND USER ACCOUNTS.

FYI I DONT UNDERSTAND ALGORITHIMS YET

"""

from time import sleep
import os

def clear_console():
    os.system('cls')
    
#COLLECTION TYPES TO ACT AS A DATABASE
    
books=['math Made Familiar 2021','english aid 2020','bio kcse a+']
books_prices=['math->[150/=]','english->[250/=]','bio->[350/=]']
novels=['kidagaa kimemwozea','pearls of the savannah','caucasian chalk circle']
novels_prices=['kidagaa->[500/=]','pearls->[600/=]','caucasian->[820/=]']
pens=['bic','speedo','obama']
pens_prices=['bic->[20/=]','speedo->[10]','obama->[30/=]']

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

# FUCTIONS TO CALL IN THE MAIN PROGRAM

def show_products():    
    print('\n....................................')
    print('...........BOOKS....................')
    
    for x in books:
        print(x)
    print('....................................')
    print('...........NOVELS...................')
    
    for x in novels:
        print(x)
    print('...................................')
    print('...........PENS....................')
    
    for x in pens:
        print(x)
    print('...................................')
    print('\n What would you like to buy ?,first press 2 to check the prices')
    

def show_prices():
    print('....................................')
    print('...........BOOKS....................')
    
    for x in books_prices:
        print('{a:>20}' . format (a=x))
    print('....................................')
    print('...........NOVELS...................')
    
    for x in novels_prices:
        print('{a:>20}' . format (a=x))
    print('...................................')
    print('...........PENS....................')
    
    for x in pens_prices:
        print('{a:>20}' . format (a=x))
    print('...................................')
    print('\n AWESOME !!! now lets buy stuff ')
    print('\n press 3 to see product codes')

def product_codez():
    print(product_codes)
    
    
def buy_product(code,bought_items):
    item=(product_codes.get(code,'not found'))
    bought_items =bought_items.append(item)
    
    return bought_items

#start of MAIN PROGRAM...

print('-----------welcome to the bookshop database---------------')
firstpage='''\n  :
                    1.SHOW PRODUCTS
                    2.SHOW PRICES
                    3.SEE PRODUCT CODES
                    4.BUY PRODUCTS
                    5.SEE YOUR SHOPPING CART
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
if choice == 1:
    show_products()
    choice=int(input())
    clear_console()

if choice == 2 :
    show_prices()
    choice=int(input())
    clear_console()

if choice == 3 :
    product_codez()
    choice=int(input('\n now press 4 to fill up your shopping cart\t'))
    
if choice ==4:
    goods= int(input('\n***how many products do you wish to buy ?***** \t'))
    while i <=goods:
        code=int(input('\n enter the product code to continue =>'))
        buy_product(code,bought_items)
        i+=1
    print('\n wow you made a purchase, press 5 to see what you bought')
    choice=int(input())
    clear_console()
if choice==5 and bought_items!=[]:
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









             



















