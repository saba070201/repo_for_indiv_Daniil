import random
class Batle:
    @staticmethod
    def batle(w1,w2):
       while True:
          if w1.hp<=0:
             print(f'{w2.name} win!!!')
             break
          elif w2.hp <= 0: 
             print(f'{w1.name} win!!!')
             break
          currentw=random.randint(1,2)
          if currentw==1:
             w1.do_attack(w2)
             print(f'w1attack:{w1.attack} w2hp:{w2.hp}')
          elif currentw ==2:
             w2.do_attack(w1)
             print(f'w2attack:{w2.attack} w1hp:{w1.hp}')


class Weapon:
    def __init__(self,name,damage,kritvalue=2,kritchance=20) -> None:
       self.name=name
       self.damage=damage
       self.kritvalue=kritvalue
       self.kritchance=kritchance

class Armour:
   def __init__(self,name,damagereflect) -> None:
      self.name = name
      self.damagereflect = damagereflect

class Warrior:
    def __init__(self,name,hp,attack,weapon:Weapon, armour:Armour) -> None:
      self.name=name
      self.hp=hp
      self.attack=attack
      self.weapon=weapon
      self.armour=armour
    def do_attack(self,other):
      currentattack=self.attack+self.weapon.damage
      if random.randint(1,100) <=self.weapon.kritchance:
         currentattack*=self.weapon.kritvalue
         print('Kritical hit')
      other.hp-=currentattack-other.armour.damagereflect
         
w1=Warrior('Artes',100,10,Weapon('frostmorn',10,kritchance=10),Armour('plate',10))
w2=Warrior('Illidan',50,20,Weapon('moonblade',20,kritchance=15), Armour('megaplate',15))
Batle.batle(w1,w2)  
