import random


class Player:
    count = 0

    def __init__(self, names, att, life, defend):
        self.attackNumber = att
        self.lifeNumber = life
        self.defendNumber = defend
        self.name = names

    def beAttacked(self, a):
        if self.lifeNumber <= 0:
            print(self.name + " is died")
        if a > self.defendNumber:
            self.lifeNumber -= a - self.defendNumber
            print(self.name + " be attacked, QAQ . ", end="")
            if self.lifeNumber <= 0:
                print(self.name + " is died")
                exit(1)
        print(self.name + " get atacked is " + str(a))
        print(self.name + " \'s life is " + str(self.lifeNumber))


def init():
    nameplay = input("please input the player name: ")
    att = int(input("please input the player " + str(nameplay) + " \'s attackNumber: "))
    life = int(input("please input the player " + str(nameplay) + " \'s lifeNumber: "))
    defend = int(input("please input the player " + str(nameplay) + " \'s defendNumber: "))
    print("Creat ok")
    return Player(nameplay, att, life, defend)


play1 = init()
play2 = init()

for i in range(10):
    print("\nThe " + str(i + 1) + " start: \n")
    play1.beAttacked(random.randint(0, play1.defendNumber + play1.lifeNumber))
    play2.beAttacked(random.randint(0, play2.defendNumber + play2.lifeNumber))
    nn = input("please input anything to continue: (\"e\" to exit)\n")
    if nn == "e":
        break
