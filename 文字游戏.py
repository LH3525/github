class Tiger:
    TypeName = 'Tiger'
    def __init__(self,Weight=200):
        self.Weight = Weight
    def feed(self,food):
        if food == 'meat':
            self.Weight +=10
        else:
            print('喂食错误！')
            self.Weight -=10
    def roar(self):
        print('Wow !！')
        self.Weight -=5
class Sheep:
    TypeName = 'Sheep'
    def __init__(self, Weight=100):
        self.Weight = Weight
    def feed(self, food):
        if food == 'grass':
            self.Weight += 10
        else:
            print('喂食错误！')
            self.Weight -= 10
    def roar(self):
        print('Mie')
        self.Weight -= 5
class Room:
    def __init__(self,num,animal):
        self.num = num
        self.animal = animal
from random import randint
import time
Roomlist = []
for one in range(0,10):
    if randint(0,1) ==1:
        ani = Tiger(200)
    else:
        ani = Sheep(100)
    Roomlist.append(Room(one,ani))
starttime = time.time()
while True:
    curtime = time.time()
    if (curtime - starttime) >180:
        for one in Roomlist:
            print('房间号{}:动物是{}:体重是{}'.format(one.num+1,one.animal.TypeName,one.animal.Weight))
        break
    roomNum = randint(1,10)
    print('房间号是：{}'.format(roomNum))
    room = Roomlist[roomNum-1]
    qm = input('是否需要敲门(y/n)?: ')
    if qm.strip() == 'y':
        room.animal.roar()
    food = input('是否需要喂食(meat/grass)?: ')
    room.animal.feed(food.strip())

print('game is over')

