import random
random.seed()
diceroll=0
TravTurn=0
AttackType=''
SuperPoints=0
itslit="unlocked"
applepie=''
astrothunder=''
sickomode=''
moveon='no'

def Dice(): #random dicef
    diceroll = random.randint(1,20)
    import time
    print('rolling dice...')
    time.sleep(1)
    print(f'you rolled a {diceroll}')
    pause()
    return diceroll



def Combat(Travishp,Travisdmg,Travisdodging,Travispriority,Travismaxhealth,Travisapplepie,Travisastrothunder,Travissickomode,Enemyname,Enemyhp,Enemydmg,Enemydodging,Enemypriority,Enemymaxhealth,Enemyapplepie,Enemyastrothunder,Enemysickomode,SuperPoints):
    diceroll=Dice()
    diceroll += Travispriority
    diceroll -= Enemypriority
    if diceroll>10:
        TravTurn=1
        print('You are up first')
    else:
        TravTurn=0
        print('You will attack 2nd')
    print(f'you are fighting {Enemyname}')
    while Travishp>0 and Enemyhp>0:
        while TravTurn==1:
            AttackType=input('what attack do you want to use?')
            if AttackType == "itslit" or AttackType =='its lit':
                diceroll=Dice()
                if diceroll>Enemydodging:
                    SuperPoints+=1
                    Enemyhp-=Travisdmg
                    TravTurn=0
                    print(f'travis did {Travisdmg} to {Enemyname}, the {Enemyname} has {Enemyhp} left')    
                else:
                    print(f'{Enemyname} dodged {AttackType}')                        
            elif AttackType == "applepie" or AttackType=='Apple pie':
                if SuperPoints>=3:
                    SuperPoints -= 3
                    Travishp+=Travisapplepie
                    TravTurn=0
                    print(f'you healed for {Travisapplepie} you are at {Travishp}')   
                else:
                    print('not enough superpoints')
            elif AttackType == "astrothunder":
                if SuperPoints>=7:
                    SuperPoints -= 7
                    diceroll=Dice()
                    if diceroll>Enemydodging:
                        Enemyhp-=Travisastrothunder
                        TravTurn=0
                        print(f'you did {Travisastrothunder} to {Enemyname}, the {Enemyname} has {Enemyhp} left')    
                    else:
                        print(f'{Enemyname} dodged {AttackType}')
                else:
                    print('not enough superpoints')
            elif AttackType == "sickomode" or AttackType=='sicko mode':
                if SuperPoints>=10:
                    SuperPoints -= 10
                    Travishp+=Travissickomode
                    print(f'you healed for {Travissickomode} you are at {Travishp}') 
                    diceroll=Dice()
                    if diceroll>Enemydodging:
                        Enemyhp+=Travissickomode
                        TravTurn=0
                        print(f'you did {Travissickomode} to {Enemyname}, the {Enemyname} has {Enemyhp} left')
                    else:
                        print(f'{Enemyname} dodged {AttackType}')
                else:
                    print('not enough superpoints')
            else:
                while AttackType!= 'unlocked':
                    AttackType=input('what attack do you want to use?')
                print(f'{Enemyname} dodged the attack')
                TravTurn=0
        while TravTurn==0:
            if Enemyhp>=0:
                print('the zombie is attacking')
                pause()
                diceroll=Dice()
                if 20-diceroll>Travisdodging:
                    if Enemyapplepie != 0:
                        diceroll=Dice()
                        if diceroll>=15:
                            Enemyhp+=Enemyapplepie
                            print(f'{Enemyname} healed for {Enemyapplepie} and is now at {Enemyhp} health')
                        else:
                            Travishp-=Enemydmg
                            print(f'you took {Enemydmg}, you are at {Travishp} health')
                    else:
                        Travishp-=Enemydmg
                        print(f'you took {Enemydmg}, you are at {Travishp} health')
                    TravTurn=1  
                else:
                    print('you dodged the attack')
                    TravTurn=1
            else:
                break
    if Travishp>0:
        Travishp= (Travismaxhealth-Travishp)/2
        print('you defeated the enemy')
    else:
        print('you died!')
        quit('end')
    return(Travishp,SuperPoints)
        
            

def pause(): #pause() for 2 sec
    import time
    time.sleep(3)

class character:
    def __init__(self,name,hp,dmg,dodging,priority,maxhealth,applepie,astrothunder,sickomode,butterflyeffect):
        self.name=name
        self.hp=hp
        self.dmg=dmg
        self.dodging=dodging
        self.priority=priority
        self.maxhealth=maxhealth
        self.applepie=applepie
        self.astrothunder=astrothunder
        self.sickomode=sickomode
        self.butterflyeffect=butterflyeffect
    def Upgrade(self,choice):
        while choice!='health' and choice!='damage' and choice!='dodging' and choice!='applepie' and choice!='apple pie' and choice!='astrothunder' and choice!='sicko mode' and choice!='sickomode':
            choice=input('do you want to upgrade health, damage, dodging, apple pie, astrothunder or sicko mode?')
            if choice=='health' or choice=='damage'or choice=='dodging'or choice=='applepie'  or choice=='apple pie' or choice=='astrothunder'or choice=='sicko mode' or choice=='sickomode'  :
                if choice == 'health':
                    self.maxhealth+=15
                elif choice == 'damage':
                    self.dmg+=5
                elif choice == 'dodging':
                    self.dodging+=1
                elif choice == 'applepie':
                    self.applepie+=10
                elif choice == 'astrothunder':
                    self.astrothunder+=20
                elif choice == 'sicko mode':
                    self.sickomode+=15
                print(f'you upgraded {choice}')
                moveon='yes'
                pause()
            else:
                print('invalid')

print('you are Travis Scott. you now have to make it through the rodeo, the trap, and ASTROWORLD to make it to utopia, good luck!')
pause()
print('you have 100 health and you get healed half after each fight and fully healed when you change worlds')
pause()
print('your attack is called itslit')
pause()
Travis=character('travis',100,15,3,2,100,20,40,30,0)
Zombie=character('zombie,',30,10,0,0,50,0,0,0,0)

print('you are walking towards the rodeo when you encounter a zombie')
print('')
Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,Zombie.name,Zombie.hp,Zombie.dmg,Zombie.dodging,Zombie.priority,Zombie.maxhealth,Zombie.applepie,Zombie.astrothunder,Zombie.sickomode,SuperPoints)
print('congrats, you won your first fight! you get to upgrade a skill.')
pause()
Travis.Upgrade()
print('you are now in the rodeo')
pause()
print('you spot a mama armed with an apple pie and shes angry')
Mama=character('zombie,',60,5,1,5,50,20,0,0,0)
Travis.hp,SuperPoints=Combat(Travis.name,Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,Mama.name,Mama.hp,Mama.dmg,Mama.dodging,Mama.priority,Mama.maxhealth,Mama.applepie,Mama.astrothunder,Mama.sickomode,SuperPoints)
pause()
print('youve unlocked apple pie!')
pause()
pause()
print('apple pie requires 3 superpoints')
pause()
print('you get a powerpoint every time you successfully use your main attack')
pause()
print('applepie heals for 20')