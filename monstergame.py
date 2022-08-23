from random import *


class Monster:
    def __init__(self,name,origin):
        self.name = name
        self.origin = origin
        self.life = 3
        self.bullets = 5
        self.wins = 0
        self.level=1
        
    def shoot(self,other):
        if other.life > 0:
            if self.bullets > 0:
                other.life-=1
                self.bullets-=1
            else:
                 print('you have no bullets')
                 
        if other.life < 1 :
            self.wins+=1
            self.life = 3
        print(self.wins,'wins')
            
    
    def add_life(self):
        self.life+=1
        return self.life
    
    def rank(self):
        if self.wins > 1:
            self.level += 1
            if self.level > 3 :
                self.bullets+=5
        return self.level
    


class Alien(Monster):
    def __init__(self,name,origin,weapon):
        super().__init__(name,origin)
        self.weapon=weapon

    def shootback(self,other):
        if self.bullets > 0 and self.life >0:
                other.life-=1
                self.bullets-=1
   
    def details(self):
        return(f'{self.name} you have: {self.life} lives {self.bullets} bullets , your gun is {self.weapon}')

    

class Preditor(Monster):
    def __init__(self,name,origin,amour):
        super().__init__(name,origin)
        self.amour=amour

    def shootback(self,other):
        if self.bullets > 0 and self.life > 0:
                other.life-=1
                self.bullets-=1

    def details(self):
        return(f'{self.name} you have: {self.life} lives {self.bullets} bullets , your amour is {self.amour}')
        
   
    
A1=Alien('bert','mars','ak47')
M1=Preditor('ugly','jupiter','steel plate')
M2=Preditor('ugly','jupiter','steel plate')
M3=Preditor('ugly','jupiter','steel plate')


print('-------------- match----------')


while M1.life>0 :
    A1.shoot(M1)
    M1.shootback(A1)
    #print(M1.details())
    print('shoter has',A1.wins,'wins and','level',A1.rank(),'with',A1.bullets,'bullets',A1.life,'life')
    print('victim has',M1.wins,'wins and','level',M1.rank(),'with',M1.bullets,'bullets',M1.life,'life')

print('-------------- match----------')
    
while M2.life>0 :
    A1.shoot(M1)
    M2.shootback(A1)
    #print(M1.details())
    print('shoter has',A1.wins,'wins and','level',A1.rank(),'with',A1.bullets,'bullets',A1.life,'life')
    print('victim has',M2.wins,'wins and','level',M2.rank(),'with',M2.bullets,'bullets',M2.life,'life')
    
print('-------------- match----------')
    
while M3.life>0 :
    A1.shoot(M1)
    M2.shootback(A1)
    #print(M1.details())
    print('shoter has',A1.wins,'wins and','level',A1.rank(),'with',A1.bullets,'bullets',A1.life,'life')
    print('victim has',M3.wins,'wins and','level',M3.rank(),'with',M3.bullets,'bullets',M3.life,'life')
    
