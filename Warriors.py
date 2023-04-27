import random
from colored import fg, bg, attr


class Battle:
    
    @staticmethod
    def Duel(w1,w2):
       while True:
          if (w1.hp<=0) and (w2.hp<=0):
            print(f'{fg(166)}Draw{fg(1)}!!!{attr(0)}')
            break 
          elif w1.hp<=0:
            print(w2, f'{fg(166)}Win{fg(1)}!!!{attr(0)}')
            break
          elif w2.hp <= 0: 
            print(w1, f'{fg(166)}Win{fg(1)}!!!{attr(0)}')
            break
          currentw=random.randint(1,2)
          ult = random.randint(1,10)
          if currentw==1:  
              if ult == 10:
                  w1.do_ultimate_attack(w2)  
              else:
                  w1.do_attack(w2)  
          elif currentw ==2:
              if ult == 10:
                  w2.do_ultimate_attack(w1)
              else:
                  w2.do_attack(w1)
        
    @staticmethod
    def findthewinner(arr):   
        if len(arr)>0:
            return arr[0] 
        else:
            return f'{fg(0)}{bg(255)} NOBODY {attr(0)}'     
    
    @staticmethod
    def smbisdead(arr):
        arr=sorted(arr,key=lambda arr:arr.hp,reverse=True) 
        i = len(arr)-1 
        while i>=0:
            if arr[i].hp<=0:  
                print(arr[i], 'is killed')
                arr.remove(arr[i])
            i-=1
        return arr
    
    @staticmethod
    def FFA(arr):
        while True:
            if len(arr) <= 0:
                print(Battle.findthewinner(arr), f'{fg(0)}{bg(255)} WIN {attr(0)}')
                break
            currentw=random.randint(0,len(arr)-1)
            otherw = random.randint(0,len(arr)-1)
            while currentw==otherw:
                otherw = random.randint(0,len(arr)-1)       
            ult = random.randint(1,10)
            if ult == 10:
                  arr[currentw].do_ultimate_attack(arr[otherw])  
            else:
                  arr[currentw].do_attack(arr[otherw])
            arr = Battle.smbisdead(arr)
            
        

class Weapon:
    def __init__(self,name='defaultweapon',damage=5,critvalue=2,critchance=5) -> None:
       self.name=name
       self.damage=damage
       self.critvalue=critvalue
       self.critchance=critchance

class Armour:
   def __init__(self,name='defaultarmour',damagereflect=5) -> None:
      self.name = name
      self.damagereflect = damagereflect

class Warrior:
    def __init__(self, name, hp=50, attack=10, weapon:Weapon=Weapon(), armour:Armour=Armour()) -> None:
      self.name=name
      self.hp=hp
      self.attack=attack
      self.weapon=weapon
      self.armour=armour
      
    def __str__(self) -> str:
       return str(f'{fg(1)}['+f'{fg(255)}{self.name}'+f'{fg(1)}]{attr(0)}') 
    
    def do_attack(self,other):
      currentattack=self.attack+self.weapon.damage
      if random.randint(1,100) <=self.weapon.critchance:
         currentattack*=self.weapon.critvalue
         print(self, f'{fg(166)}Crit{fg(1)}!!!{attr(0)}')
      if (currentattack-other.armour.damagereflect) > 0:
        other.hp-=currentattack-other.armour.damagereflect
      print(self, f'attacks {currentattack} str!', other, f'got {currentattack -other.armour.damagereflect} dmg!', other, f'hp = {other.hp}')
    
    def do_ultimate_attack(self,other):
        currentattack = self.attack*3+self.weapon.damage
        print(self, f'{fg(201)}Ultimate{fg(1)}!!!{attr(0)}')
        if random.randint(1,100) <=self.weapon.critchance:
         currentattack*=self.weapon.critvalue
         print(self, f'{fg(201)}Ultimate Crit{fg(166)}!!!{attr(0)}')
        if (currentattack-other.armour.damagereflect) > 0:
            other.hp-=currentattack-other.armour.damagereflect   
        self.hp -= currentattack/4
        print (self, f'got {currentattack/4} dmg! {self} hp = {self.hp}')
        print(self, f'attacks {currentattack} str!', other, f'got {currentattack -other.armour.damagereflect} dmg!', other, f'hp = {other.hp}')      
         
w1=Warrior('Arthas',100,15,Weapon('Frostmorn',14,critchance=10),Armour('plate',10))
w2=Warrior('Illidan',60,20,Weapon('Moonblade',17,critchance=15), Armour('megaplate',15))
w3=Warrior('Sylvana',80,8,Weapon('Cursedknife',8,3,35), Armour('UnhollyPlate',13))
w4=Warrior('Jason Born', 85,13,Weapon('blade',10,3,20),Armour('jacket',8))
Warriors = [w1, w2, w3, w4]
Battle.FFA(Warriors)
