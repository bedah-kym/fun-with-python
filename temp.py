class Monster:
    def __init__(self,name,origin,life,bullets):
        self.name = name
        self.origin = origin
        self.life = life
        self.bullets=bullets
        
    def shoot(self,other):
        if other.life > 0:
            if self.bullets > 0:
                other.life-=1
                self.bullets-=1
            else:
                return print('you have no bullets')
        else:
            return print('victim is dead')
    
    def add_life(self):
        self.life+=1
        return self.life
    


class Alien(Monster):
    def __init__(self,name,origin,life,bullets,weapon):
        super().__init__(name,origin,life,bullets)
        self.weapon=weapon
        
    def details(self):
        return(f'{self.name} you have: {self.life} lives {self.bullets} bullets , your gun is {self.weapon}')

    

class Preditor(Monster):
    def __init__(self,name,origin,life,bullets,amour):
        super().__init__(name,origin,life,bullets)
        self.amour=amour

    def details(self):
        return(f'{self.name} you have: {self.life} lives {self.bullets} bullets , your amour is {self.amour}')
        
       

A1=Alien('bert','mars',3,5,'ak47')
M1=Preditor('ugly','jupiter',3,5,'steel plate')
A1.shoot(M1)
print(M1.details())
print(A1.details())
