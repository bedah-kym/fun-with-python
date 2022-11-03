""" DO NOT RUN THIS PROGRAM with "letters" IT WILL CRASH UR MACHINE !!! si vako oyah"""
import itertools

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

abc=['a','b','c']

def calculate(letters):
    
    perm=list(itertools.permutations(letters))
    perm2=list(itertools.permutations(letters))

    print(len(perm)**len(perm),perm,len(perm2)**len(perm2),perm2)
    

"""while True:
    calculate(abc)
"""

calculate(abc)
