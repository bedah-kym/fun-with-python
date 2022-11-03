""" THIS IS MY LITLE PROJECT MY BOOKHOP 1.01 I AM BUILDING AS I LEARN PYTHON ADDING FEATURES AND MAKING THE CODE
SMARTER AS I LEARN NEW CONCEPTS. FOLLOW ALONG,THANK YOU
IN THIS VERSION YOU CAN SEE THE PRODUCTS AND BUY ANYTHING BUT ANY BUT ONLY ONE
You can remove sleep() so its runs faster

"""

from time import sleep

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
print('-----------welcome to the bookshop database---------------')
firstpage='''\n  :
                    1.SHOW PRODUCTS
                    2.SHOW PRICES
                    3.SEE PRODUCT CODES
                    4.SEE BOUGHT PRODUCTS
'''
print(firstpage)
choice=int(input())
sleep(2)
print('intializing database........')
sleep(2)
print('optimizing data..............')
sleep(4)
if choice == 1:
    
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
    choice=int(input())
sleep(2)
if choice == 2 :
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
    print('press 3 to see product codes')
    choice=int(input())
sleep(2)
if choice == 3 :
    bought_items=" "
    print(product_codes)
    code=int(input('enter the product code to continue'))
    if code==101:
             item=(product_codes.get(101,'not found'))
             bought_items += item
    if code==102:
             item=(product_codes.get(102,'not found'))
             bought_items += item
    if code==103:
             item=(product_codes.get(103,'not found'))
             bought_items += item
    if code==104:
             item=(product_codes.get(104,'not found'))
             bought_items += item
    if code==105:
             item=(product_codes.get(105,'not found'))
             bought_items += item
    if code==106:
             item=(product_codes.get(106,'not found'))
             bought_items += item
    if code==107:
             item=(product_codes.get(107,'not found'))
             bought_items += item
    if code==108:
             item=(product_codes.get(108,'not found'))
             bought_items += item
    if code==109:
             item=(product_codes.get(109,'not found'))
             bought_items += item
    print('\n wow you made your first purchase, press 4 to see what you bought')
    choice=int(input())        
    if choice== 4:
        print(bought_items)

else :
    print('sorry! you havent bought any items')

sleep(5)









             



















