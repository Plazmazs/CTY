import random
diceroll=0
def Dice(): #random dicef
    diceroll = random.randint(1,20)
    import time
    time.sleep(1)
    print(f'you rolled a {diceroll}')
    pause()
    return diceroll

def pause(): #pause() for 2 sec
    import time
    time.sleep(2)

class character:
    def __init__(self,name,hp,dmg,dodging,maxhealth,dmgstat,dodgingstat,applepie,astrothunder):
        self.name=name
        self.hp=hp
        self.dmg=dmg
        self.dodging=dodging
        self.maxhealth=maxhealth
        self.dmgstat=dmgstat
        self.dodgingstat=dodgingstat
        self.applepie=applepie
        self.astrothunder=astrothunder
    def Upgrade(self,choice):
        if choice == 'health':
            self.maxhealth+=15
        elif choice == 'damage':
            self.dmgstat+=5
        elif choice == 'dodging':
            self.dodgingstat+=1
        elif choice == 'applepie':
            self.applepie+=10
        elif choice == 'astrothunder':
            self.astrothunder+=25
        else:
            print('invalid')
        print(f'you upgraded {choice}')
    def DealDamage(self,):
        pass
    def TakeDamage(self,):
        pass
print('you are Travis Scott. you now have to make it through the rodeo, the trap, and ASTROWORLD to make it to utopia, good luck!')
print('you have 100 health and you get healed half after each fight and fully healed when you change worlds')
travis=character('travis',100,15,1,100,0,0,0,0)
zombie=character('zombie,',30,10,0,50,0,0,0,0)





