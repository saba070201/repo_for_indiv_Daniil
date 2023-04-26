# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
   
# p=Person('misha',22)
# print(p.age,p.name)
# p1=Person('daniil',25)
# print(p1.name,p1.age)
import math
# class Point:
#     def __init__(self,x,y) -> None:
#         self.x=x
#         self.y=y
#     def __str__(self) -> str:
#         return f'x:{self.x} , y:{self.y}'
#     def __add__(self,other):
#         return Line(self,other)


# class Line:
#     def __init__(self,p1:Point,p2:Point) -> None:
#         self.p1=p1
#         self.p2=p2
#     def __str__(self) -> str:
#         return f'p1:{self.p1},p2:{self.p2}'
# class CalcModule:
#     @staticmethod
#     def dist(p1,p2):
#         return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
# p1=Point(1,1)
# p2=Point(1,2)
# # print(CalcModule.dist(p1,p2))
# print(p1+p2)
# class CustomList:
#     def __init__(self,arr) -> None:
#         self.arr=arr
#     def __getitem__(self,i):
#         return self.arr[i-1]
# cl=CustomList([1,2,3])
# print(cl[1])
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

class Warrior:
    def __init__(self,name,hp,attack,weapon:Weapon) -> None:
      self.name=name
      self.hp=hp
      self.attack=attack
      self.weapon=weapon
    def do_attack(self,other):
      currentattack=self.attack+self.weapon.damage
      if random.randint(1,100) <=self.weapon.kritchance:
         currentattack*=self.weapon.kritvalue
         print('Kritical hit')
      other.hp-=currentattack
         
w1=Warrior('Artes',100,10,Weapon('frostmorn',10,kritchance=10))
w2=Warrior('Illidan',50,20,Weapon('moonblade',20,kritchance=15))
Batle.batle(w1,w2)       


    

