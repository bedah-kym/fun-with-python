""" in this game we have two types of monsters , aliens and preditors now each can get a match to play aginist
each other or the other party .each match has a shooter and a victim the shooter kills the victim and gets
renewed life for the next match but since the shooter has less bullets it gets killed in the second match
and the victim in the second match becomes the shooter in the next match and dies there and so on """

# i use this game to learn python oop and edge cases in programs

class Monster:
    def __init__(self,name,origin):
        self.name = name
        self.origin = origin
        self.life = 3
        self.bullets = 5
        self.wins = 0
        self.level=1

    def __str__(self):
        return self.name
        
    def shoot(self,other):
        if other.life > 0:
            if self.bullets > 0:
                other.life-=1
                self.bullets-=1
            else:
                 other.wins+=1
                 other.life = 3
                 print('you have no bullets')
                 
        if other.life < 1 :
            self.wins+=1
            self.life = 3


        print('-.>>>>>>>>>round----')     
    
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
M2=Preditor('mose','jupi','steel')
M3=Preditor('ujing','jupit','steel-plate')

print('-------------- match 1 ----------')


while M1.life>0 :
    A1.shoot(M1)
    M1.shootback(A1)
    #print(M1.details())
    print('shoter has',A1.wins,'wins and','level',A1.rank(),'with',A1.bullets,'bullets',A1.life,'life')
    print('victim has',M1.wins,'wins and','level',M1.rank(),'with',M1.bullets,'bullets',M1.life,'life')

print('-------------- match 2 ----------')
    
while M2.life>0 and M2.bullets>0:
    if A1.life >0 or A1.bullets >0 :
        A1.shoot(M2)
        M2.shootback(A1)
        print('shoter has',A1.wins,'wins and','level',A1.rank(),'with',A1.bullets,'bullets',A1.life,'life')
        print(M2.name,'has',M2.wins,'wins and','level',M2.rank(),'with',M2.bullets,'bullets',M2.life,'life')
    else:
        print('shooter is dead')
        break
print('-------------- match 3 ----------')
    
while M3.life>0 and M3.bullets>0:
    if M2.life >0 or M2.bullets >0 :
        M2.shoot(M3)
        M3.shootback(M2)
        print('shoter has',M2.wins,'wins and','level',M2.rank(),'with',M2.bullets,'bullets',M2.life,'life')
        print(M3.name,'has',M3.wins,'wins and','level',M3.rank(),'with',M3.bullets,'bullets',M3.life,'life')
    else:
        print('shooter is dead')
        break
"""
this here 'lol' leaderboard function takes players as an arg and uses binary search to sort the .wins of the players
but another loop prints the sorted list with the .names and .wins to make a lit leaderboard"""

players=[A1,M1,M2,M3]

def leaderboard(players):

    for a in range(0,len(players)):
        for x in range (0,len(players)-1):
            if players[x].wins < players [x+1].wins:
                players[x],players[x+1]=players[x+1],players[x]

            else:
                pass
    for player in players:
        print(player.name,player.wins)
    
print('----leader board-----')
print(leaderboard(players))
print('----leader board-----')            
