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
dead='no'

def Dice(name): #random dicef
    diceroll = random.randint(1,20)
    import time
    print('rolling dice...')
    time.sleep(1)
    print(f'{name} rolled a {diceroll}')
    print('')
    pause()
    return diceroll

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
                    self.maxhealth+=random.randint(3,14)
                    print(f'max health is now {self.maxhealth} health')
                elif choice == 'damage':
                    self.dmg+=random.randint(1,8)
                    print(f'its lit now deals {self.dmg} damage')
                elif choice == 'dodging':
                    self.dodging+=random.randint(1,2)
                    print(f'dodging skill is now {self.dodging}')
                elif choice == 'applepie':
                    self.applepie+=random.randint(5,15)
                    print(f'apple pie now heals for {self.applepie} health')
                elif choice == 'astrothunder':
                    self.astrothunder+=random.randint(10,25)
                    print(f'astrothunder now deals {self.astrothunder} damage')
                elif choice == 'sicko mode':
                    self.sickomode+=random.randint(10,20)
                    print(f'its sicko mode now deals and heals for {self.sickomode} damage')
                print(f'you upgraded {choice}')
                pause()
            else:
                print('invalid')



def Combat(Travishp,Travisdmg,Travisdodging,Travispriority,Travismaxhealth,Travisapplepie,Travisastrothunder,Travissickomode,Enemyname,Enemyhp,Enemydmg,Enemydodging,Enemypriority,Enemymaxhealth,Enemyapplepie,Enemyastrothunder,Enemysickomode,SuperPoints):
    print('Roll for first turn')
    pause()
    diceroll=Dice('you')
    diceroll += Travispriority
    diceroll -= Enemypriority
    if diceroll>10:
        TravTurn=1
        print('You are up first')
    else:
        TravTurn=0
        print('You will attack 2nd')
    pause()
    print(f'you are fighting {Enemyname}')
    while Travishp>0 and Enemyhp>0:
        while TravTurn==1:
            print(' ')
            AttackType=input('what attack do you want to use?')
            if AttackType == "itslit" or AttackType =='its lit':
                print(f'you use {AttackType}, {Enemyname} is rolling to dodge')
                diceroll=Dice(Enemyname)
                if 20-diceroll>Enemydodging:
                    SuperPoints+=1
                    Enemyhp-=Travisdmg
                    print(f'travis did {Travisdmg} damage to {Enemyname}, the {Enemyname} has {Enemyhp} health left')    
                else:
                    print(f'{Enemyname} dodged {AttackType}')    
                TravTurn=0                    
            elif AttackType == "applepie" or AttackType=='apple pie':
                if SuperPoints>=3:
                    SuperPoints -= 3
                    Travishp+=Travisapplepie
                    if Travishp>Travismaxhealth:
                        Travishp=Travismaxhealth
                    TravTurn=0
                    print(f'you healed for {Travisapplepie} you are at {Travishp}')   
                else:
                    print('not enough superpoints')
            elif AttackType == "astrothunder":
                if SuperPoints>=6:
                    SuperPoints -= 6
                    print(f'you use {AttackType}, {Enemyname} is rolling to dodge')
                    20-diceroll=Dice(Enemyname)
                    if diceroll>Enemydodging:
                        Enemyhp-=Travisastrothunder
                        print(f'you did {Travisastrothunder} damage to {Enemyname}, the {Enemyname} has {Enemyhp} health left')    
                    else:
                        print(f'{Enemyname} dodged {AttackType}')
                    TravTurn=0
                else:
                    print('not enough superpoints')
            elif AttackType == "sickomode" or AttackType=='sicko mode':
                if SuperPoints>=10:
                    SuperPoints -= 10
                    Travishp+=Travissickomode
                    if Travishp>Travismaxhealth:
                        Travishp=Travismaxhealth
                    print(f'you healed for {Travissickomode} you are at {Travishp}') 
                    pause()
                    print(f'you use {AttackType}, {Enemyname} is rolling to dodge')
                    diceroll=Dice(Enemyname)
                    if 20-diceroll>Enemydodging:
                        Enemyhp+=Travissickomode
                        print(f'you did {Travissickomode} damage to {Enemyname}, the {Enemyname} has {Enemyhp} health left')
                    else:
                        print(f'{Enemyname} dodged {AttackType}')
                    TravTurn=0
                else:
                    print('not enough superpoints')
            else:
                print('invalid')
        if Enemyhp>0:
            while TravTurn==0:
                print(' ')
                pause()
                print(f'{Enemyname} is up')
                pause()
                if Enemyname=='zombie' or Enemyname=='nightcrawler'or Enemyname=='YoungThug' or Enemyname=='bird'  or Enemyname=='bigbird' or Enemyname=='skeletons'   :
                    print(f'{Enemyname} uses main attack, roll to dodge')
                    diceroll=Dice('you')
                    if 20-diceroll>Travisdodging:
                        Travishp-=Enemydmg
                        print(f'you took {Enemydmg} damage, you are at {Travishp} health')
                    else:
                        print('you dodged the attack')
                    TravTurn=1
                if Enemyname == 'mama':
                    print(f'{Enemyname} is rolling to decide action.')
                    diceroll=Dice(Enemyname)
                    if diceroll>=14:
                        Enemyhp+=Enemyapplepie
                        if Enemyhp>Enemymaxhealth:
                            Enemyhp=Enemymaxhealth
                        print(f'{Enemyname} healed for {Enemyapplepie} health and is now at {Enemyhp} health using apple pie')
                    else:
                        print(f'{Enemyname} used main attack')
                        if 20-diceroll>Travisdodging:
                            Travishp-=Enemydmg
                            print(f'you took {Enemydmg} damage, you are at {Travishp} health')
                        else:
                            print('you dodged the attack')
                    TravTurn=1
                if Enemyname=='kendrick':
                    if Enemyhp>20:
                        print(f'{Enemyname} uses main attack, roll to dodge')
                        diceroll=Dice('you')
                        if 20-diceroll>Travisdodging:
                            Travishp-=Enemydmg
                            print(f'you took {Enemydmg} damage, you are at {Travishp} health')
                        else:
                            print('you dodged the attack') 
                    else:
                        print('kendrick will try to sing because he is dying of thrist')
                        diceroll=Dice(Enemyname)
                        if diceroll>10:
                            Enemyhp+=50
                            print(f'kendrick healed for 50, he is now at {Enemyhp}')
                        else:
                            print('failed')
                    TravTurn=1   
                if Enemyname == 'Drake':
                    print(f'{Enemyname} is rolling to decide action.')
                    diceroll=Dice(Enemyname)
                    if diceroll>=15:
                        print(f'{Enemyname} used sicko mode!')
                        Enemyhp+=Enemysickomode
                        if Enemyhp>Enemymaxhealth:
                            Enemyhp=Enemymaxhealth
                        print(f'{Enemyname} healed for {Enemysickomode} health and is now at {Enemyhp} health using sicko mode')
                        if 20-diceroll>Travisdodging:
                            Travishp-=Enemysickomode
                            print(f'you took {Enemysickomode} damage, you are at {Travishp} health')
                    else:
                        print(f'{Enemyname} used main attack')
                        if 20-diceroll>Travisdodging:
                            Travishp-=Enemydmg
                            print(f'you took {Enemydmg} damage, you are at {Travishp} health')
                        else:
                            print('you dodged the attack')
                    TravTurn=1
        else:
            pass
    if Travishp>0:
        pause()
        print(' ')
        print(f'you healed for {(Travismaxhealth-Travishp)/3} health')
        pause()
        Travishp+= int((Travismaxhealth-Travishp)/3)
        Travishp=int(Travishp)
        print('you defeated the enemy')
        print(f'you are at {Travishp} health you have {SuperPoints} SuperPoints')
        pause()

        
    else:
        print('you died!')
        dead='yes'
        quit('end')
    return(Travishp,SuperPoints)
while dead=='no':
    print('''
    █████   ███   █████          ████                                            
    ░░███   ░███  ░░███          ░░███                                            
    ░███   ░███   ░███   ██████  ░███   ██████   ██████  █████████████    ██████ 
    ░███   ░███   ░███  ███░░███ ░███  ███░░███ ███░░███░░███░░███░░███  ███░░███
    ░░███  █████  ███  ░███████  ░███ ░███ ░░░ ░███ ░███ ░███ ░███ ░███ ░███████ 
    ░░░█████░█████░   ░███░░░   ░███ ░███  ███░███ ░███ ░███ ░███ ░███ ░███░░░  
        ░░███ ░░███     ░░██████  █████░░██████ ░░██████  █████░███ █████░░██████ 
        ░░░   ░░░       ░░░░░░  ░░░░░  ░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░  
                                                                                
                                                                                
                                                                                
    █████                ███████████                █████                       
    ░░███                ░░███░░░░░███              ░░███                        
    ███████    ██████     ░███    ░███   ██████   ███████   ██████   ██████      
    ░░░███░    ███░░███    ░██████████   ███░░███ ███░░███  ███░░███ ███░░███     
    ░███    ░███ ░███    ░███░░░░░███ ░███ ░███░███ ░███ ░███████ ░███ ░███     
    ░███ ███░███ ░███    ░███    ░███ ░███ ░███░███ ░███ ░███░░░  ░███ ░███     
    ░░█████ ░░██████     █████   █████░░██████ ░░████████░░██████ ░░██████      
    ░░░░░   ░░░░░░     ░░░░░   ░░░░░  ░░░░░░   ░░░░░░░░  ░░░░░░   ░░░░░░        ''')
    print('you are Travis Scott. you now have to make it through the rodeo, the trap, and ASTROWORLD to make it to utopia, good luck!')
    print('https://youtu.be/w3LGyvzv7yg?si=DAh-FIQLZ-sAWI3C')
    pause()
    print('you have 100 health and you get healed a third after each fight and fully healed when you change worlds')
    pause()
    print('your attack is called its lit')
    pause()
    Travis=character('travis',100,15,4,3,100,25,40,30,0)
    Zombie=character('zombie',50,10,1,1,40,0,0,0,0)

    print('you are walking towards the rodeo when you encounter a zombie')
    pause()
    Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,Zombie.name,Zombie.hp,Zombie.dmg,Zombie.dodging,Zombie.priority,Zombie.maxhealth,Zombie.applepie,Zombie.astrothunder,Zombie.sickomode,SuperPoints)
    print('congrats, you won your first fight! you get to upgrade a skill.')
    pause()
    Travis.Upgrade('')
    print('you are now in the rodeo')
    pause()
    print('you spot a mama armed with an apple pie and shes angry')
    print('https://youtu.be/cLx87ceoNT8?si=pwd7Y5VUH42dDu_I')
    Mama=character('mama',60,8,1,7,60,25,0,0,0)
    Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,Mama.name,Mama.hp,Mama.dmg,Mama.dodging,Mama.priority,Mama.maxhealth,Mama.applepie,Mama.astrothunder,Mama.sickomode,SuperPoints)
    pause()
    print(' ')
    print('youve unlocked apple pie!')
    pause()
    pause()
    print('apple pie requires 3 superpoints')
    pause()
    print('you get a superpoint every time you successfully use your main attack')
    pause()
    print('applepie heals for you 25')
    pause()
    Travis.Upgrade('')

    print('you now encounter a zombie with armor')
    Zombie=character('zombie',70,11,1,1,70,0,0,0,0)
    Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,Zombie.name,Zombie.hp,Zombie.dmg,Zombie.dodging,Zombie.priority,Zombie.maxhealth,Zombie.applepie,Zombie.astrothunder,Zombie.sickomode,SuperPoints)
    Travis.Upgrade('')
    print('that was pretty easy wasnt it!')
    pause()
    print('the lights flicker and go out')
    pause()
    print('https://youtu.be/rNr6X0_vmWM?si=6wDY1yYtUY-rCSDm')
    print('the nightcrawler, a huge black cat jumps from a tree')
    nightcrawler=character('nightcrawler',75,20,5,15,75,0,0,0,0)

    Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,nightcrawler.name,nightcrawler.hp,nightcrawler.dmg,nightcrawler.dodging,nightcrawler.priority,nightcrawler.maxhealth,nightcrawler.applepie,nightcrawler.astrothunder,nightcrawler.sickomode,SuperPoints)
    print('that was tough, but its only the beginning')
    pause()
    print('its about time to leave the rodeo')
    Travis.Upgrade('')
    print('two upgrades for your hard work')
    Travis.Upgrade('')
    print('youll be healed up soon')
    pause()
    print('a zombie ambushes you')
    Zombie=character('zombie',40,10,1,10,50,0,0,0,0)
    Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,Zombie.name,Zombie.hp,Zombie.dmg,Zombie.dodging,Zombie.priority,Zombie.maxhealth,Zombie.applepie,Zombie.astrothunder,Zombie.sickomode,SuperPoints)
    Travis.Upgrade('')
    print('nice job, now its time to go the trap')
    Travis.hp=Travis.maxhealth
    print(f'you are healed, you are now at {Travis.hp}')
    pause()
    pause()
    print(' \n \n \n \n')
    print('''                          ████                                            
                            ░░███                                            
    █████ ███ █████  ██████  ░███   ██████   ██████  █████████████    ██████ 
    ░░███ ░███░░███  ███░░███ ░███  ███░░███ ███░░███░░███░░███░░███  ███░░███
    ░███ ░███ ░███ ░███████  ░███ ░███ ░░░ ░███ ░███ ░███ ░███ ░███ ░███████ 
    ░░███████████  ░███░░░   ░███ ░███  ███░███ ░███ ░███ ░███ ░███ ░███░░░  
    ░░████░████   ░░██████  █████░░██████ ░░██████  █████░███ █████░░██████ 
    ░░░░ ░░░░     ░░░░░░  ░░░░░  ░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░  
                                                                            
                                                                            
                                                                            
    █████                 █████    █████                                    
    ░░███                 ░░███    ░░███                                     
    ███████    ██████     ███████   ░███████    ██████                       
    ░░░███░    ███░░███   ░░░███░    ░███░░███  ███░░███                      
    ░███    ░███ ░███     ░███     ░███ ░███ ░███████                       
    ░███ ███░███ ░███     ░███ ███ ░███ ░███ ░███░░░                        
    ░░█████ ░░██████      ░░█████  ████ █████░░██████                       
    ░░░░░   ░░░░░░        ░░░░░  ░░░░ ░░░░░  ░░░░░░                        
                                                                            
                                                                            
                                                                            
    █████                                                                   
    ░░███                                                                    
    ███████   ████████   ██████   ████████                                   
    ░░░███░   ░░███░░███ ░░░░░███ ░░███░░███                                  
    ░███     ░███ ░░░   ███████  ░███ ░███                                  
    ░███ ███ ░███      ███░░███  ░███ ░███                                  
    ░░█████  █████    ░░████████ ░███████                                   
    ░░░░░  ░░░░░      ░░░░░░░░  ░███░░░                                    
                                ░███                                       
                                █████                                      
                                ░░░░░                                       ''')
    pause()
    print('https://youtu.be/VAybGW3DI9Q?si=J9k8xcBKIn5I6S0W')
    pause()
    pause()
    phone=input('would you like to pick up the phone>>>  ')
    if phone=='yes':
        Travis.Upgrade('')
    else:
        Travis.hp-=20
        print(f'terrible decision you lose 20 health')
    print('you encounter a young thug and hes armed with a bat')
    YoungThug=character('YoungThug',35,20,1,1,35,0,0,0,0)
    Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,YoungThug.name,YoungThug.hp,YoungThug.dmg,YoungThug.dodging,YoungThug.priority,YoungThug.maxhealth,YoungThug.applepie,YoungThug.astrothunder,YoungThug.sickomode,SuperPoints)
    Travis.Upgrade('')
    pause()
    print('you hear flapping overhead')
    pause()
    print('suddenly, birds from the trap attack!')
    pause()
    print('they are very elusive')
    bird=character('bird',60,5,15,10,60,0,0,0,0)
    Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,bird.name,bird.hp,bird.dmg,bird.dodging,bird.priority,bird.maxhealth,bird.applepie,bird.astrothunder,bird.sickomode,SuperPoints)
    print('you finally killed all the birds')
    pause()
    Travis.Upgrade('')
    pause()
    Travis.Upgrade('')
    pause()

    print('https://youtu.be/Dst9gZkq1a8?si=rwuAhubVHeurjXgw')
    pause()
    pause()
    print('you see a dwarf approach')
    pause()
    print('hes an angry little dwarf and his name is kendrick lamar')
    pause()
    kendrick=character('kendrick',75,20,4,3,75,0,0,0,0)
    Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,kendrick.name,kendrick.hp,kendrick.dmg,kendrick.dodging,kendrick.priority,kendrick.maxhealth,kendrick.applepie,kendrick.astrothunder,kendrick.sickomode,SuperPoints)
    Travis.Upgrade('')
    pause()
    Travis.Upgrade('')
    pause()
    print('')

    print('you hear more flapping overhead')
    pause()
    print('a huge bird comes diving down')
    pause()
    bigbird=character('bigbird',30,15,15,10,60,0,0,0,0)
    Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,bigbird.name,bigbird.hp,bigbird.dmg,bigbird.dodging,bigbird.priority,bigbird.maxhealth,bigbird.applepie,bigbird.astrothunder,bigbird.sickomode,SuperPoints)
    print('you killed it!')
    pause()
    print('literally')
    Travis.Upgrade('')
    pause()
    print(' ')
    print('you made it through the trap!')
    Travis.hp=Travis.maxhealth
    print(f'travis healed back to {Travis.maxhealth} health')
    pause
    print(f'\n \n\n\n\n\n')
    print(''' █████   ███   █████ ██████████ █████         █████████     ███████    ██████   ██████ ██████████    ███████████    ███████                
    ░░███   ░███  ░░███ ░░███░░░░░█░░███         ███░░░░░███  ███░░░░░███ ░░██████ ██████ ░░███░░░░░█   ░█░░░███░░░█  ███░░░░░███              
    ░███   ░███   ░███  ░███  █ ░  ░███        ███     ░░░  ███     ░░███ ░███░█████░███  ░███  █ ░    ░   ░███  ░  ███     ░░███             
    ░███   ░███   ░███  ░██████    ░███       ░███         ░███      ░███ ░███░░███ ░███  ░██████          ░███    ░███      ░███             
    ░░███  █████  ███   ░███░░█    ░███       ░███         ░███      ░███ ░███ ░░░  ░███  ░███░░█          ░███    ░███      ░███             
    ░░░█████░█████░    ░███ ░   █ ░███      █░░███     ███░░███     ███  ░███      ░███  ░███ ░   █       ░███    ░░███     ███              
        ░░███ ░░███      ██████████ ███████████ ░░█████████  ░░░███████░   █████     █████ ██████████       █████    ░░░███████░               
        ░░░   ░░░      ░░░░░░░░░░ ░░░░░░░░░░░   ░░░░░░░░░     ░░░░░░░    ░░░░░     ░░░░░ ░░░░░░░░░░       ░░░░░       ░░░░░░░                 
                                                                                                                                            
                                                                                                                                            
                                                                                                                                            
    █████████    █████████  ███████████ ███████████      ███████    █████   ███   █████    ███████    ███████████   █████       ██████████  
    ███░░░░░███  ███░░░░░███░█░░░███░░░█░░███░░░░░███   ███░░░░░███ ░░███   ░███  ░░███   ███░░░░░███ ░░███░░░░░███ ░░███       ░░███░░░░███ 
    ░███    ░███ ░███    ░░░ ░   ░███  ░  ░███    ░███  ███     ░░███ ░███   ░███   ░███  ███     ░░███ ░███    ░███  ░███        ░███   ░░███
    ░███████████ ░░█████████     ░███     ░██████████  ░███      ░███ ░███   ░███   ░███ ░███      ░███ ░██████████   ░███        ░███    ░███
    ░███░░░░░███  ░░░░░░░░███    ░███     ░███░░░░░███ ░███      ░███ ░░███  █████  ███  ░███      ░███ ░███░░░░░███  ░███        ░███    ░███
    ░███    ░███  ███    ░███    ░███     ░███    ░███ ░░███     ███   ░░░█████░█████░   ░░███     ███  ░███    ░███  ░███      █ ░███    ███ 
    █████   █████░░█████████     █████    █████   █████ ░░░███████░      ░░███ ░░███      ░░░███████░   █████   █████ ███████████ ██████████  
    ░░░░░   ░░░░░  ░░░░░░░░░     ░░░░░    ░░░░░   ░░░░░    ░░░░░░░         ░░░   ░░░         ░░░░░░░    ░░░░░   ░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░   ''')
    pause()
    print('https://youtu.be/tAyYYKcySXA?si=E4118Fn-Cc5qNVFQ')
    pause()
    pause()
    print('A god approaches you')
    pause()
    print('he gives you a scroll')
    readit=input('do you want to read it>>  ')
    if readit=='yes':
        print('''       ▐ ▄  ▄▄· ▄▄▄ .     ▄· ▄▌      ▄• ▄▌     ▄▄▄·  ▄▄· .▄▄▄  ▄• ▄▌▪  ▄▄▄  ▄▄▄ .    .▄▄ · ▄▄▄ . ▌ ▐·▄▄▄ . ▐ ▄                                 
    ▪     •█▌▐█▐█ ▌▪▀▄.▀·    ▐█▪██▌▪     █▪██▌    ▐█ ▀█ ▐█ ▌▪▐▀•▀█ █▪██▌██ ▀▄ █·▀▄.▀·    ▐█ ▀. ▀▄.▀·▪█·█▌▀▄.▀·•█▌▐█                                
    ▄█▀▄ ▐█▐▐▌██ ▄▄▐▀▀▪▄    ▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ▄█▀▀█ ██ ▄▄█▌·.█▌█▌▐█▌▐█·▐▀▀▄ ▐▀▀▪▄    ▄▀▀▀█▄▐▀▀▪▄▐█▐█•▐▀▀▪▄▐█▐▐▌                                
    ▐█▌.▐▌██▐█▌▐███▌▐█▄▄▌     ▐█▀·.▐█▌.▐▌▐█▄█▌    ▐█ ▪▐▌▐███▌▐█▪▄█·▐█▄█▌▐█▌▐█•█▌▐█▄▄▌    ▐█▄▪▐█▐█▄▄▌ ███ ▐█▄▄▌██▐█▌                                
    ▀█▄▀▪▀▀ █▪·▀▀▀  ▀▀▀       ▀ •  ▀█▄▀▪ ▀▀▀      ▀  ▀ ·▀▀▀ ·▀▀█.  ▀▀▀ ▀▀▀.▀  ▀ ▀▀▀      ▀▀▀▀  ▀▀▀ . ▀   ▀▀▀ ▀▀ █▪                                
    .▄▄ · ▄• ▄▌ ▄▄▄·▄▄▄ .▄▄▄   ▄▄▄·      ▪   ▐ ▄ ▄▄▄▄▄.▄▄ ·      ▄· ▄▌      ▄• ▄▌     ▄▄·  ▄▄▄·  ▐ ▄     ▄• ▄▌.▄▄ · ▄▄▄ .     ▄· ▄▌      ▄• ▄▌▄▄▄  
    ▐█ ▀. █▪██▌▐█ ▄█▀▄.▀·▀▄ █·▐█ ▄█▪     ██ •█▌▐█•██  ▐█ ▀.     ▐█▪██▌▪     █▪██▌    ▐█ ▌▪▐█ ▀█ •█▌▐█    █▪██▌▐█ ▀. ▀▄.▀·    ▐█▪██▌▪     █▪██▌▀▄ █·
    ▄▀▀▀█▄█▌▐█▌ ██▀·▐▀▀▪▄▐▀▀▄  ██▀· ▄█▀▄ ▐█·▐█▐▐▌ ▐█.▪▄▀▀▀█▄    ▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ██ ▄▄▄█▀▀█ ▐█▐▐▌    █▌▐█▌▄▀▀▀█▄▐▀▀▪▄    ▐█▌▐█▪ ▄█▀▄ █▌▐█▌▐▀▀▄ 
    ▐█▄▪▐█▐█▄█▌▐█▪·•▐█▄▄▌▐█•█▌▐█▪·•▐█▌.▐▌▐█▌██▐█▌ ▐█▌·▐█▄▪▐█     ▐█▀·.▐█▌.▐▌▐█▄█▌    ▐███▌▐█ ▪▐▌██▐█▌    ▐█▄█▌▐█▄▪▐█▐█▄▄▌     ▐█▀·.▐█▌.▐▌▐█▄█▌▐█•█▌
    ▀▀▀▀  ▀▀▀ .▀    ▀▀▀ .▀  ▀.▀    ▀█▄▀▪▀▀▀▀▀ █▪ ▀▀▀  ▀▀▀▀       ▀ •  ▀█▄▀▪ ▀▀▀     ·▀▀▀  ▀  ▀ ▀▀ █▪     ▀▀▀  ▀▀▀▀  ▀▀▀       ▀ •  ▀█▄▀▪ ▀▀▀ .▀  ▀
    ·▄▄▄▄  ▄▄▄ . ▄▄▄· ·▄▄▄▄  ▄▄▌  ▪  ▄▄▄ ..▄▄ · ▄▄▄▄▄     ▄▄▄· ▄▄▄▄· ▪  ▄▄▌  ▪  ▄▄▄▄▄ ▄· ▄▌                                                        
    ██▪ ██ ▀▄.▀·▐█ ▀█ ██▪ ██ ██•  ██ ▀▄.▀·▐█ ▀. •██      ▐█ ▀█ ▐█ ▀█▪██ ██•  ██ •██  ▐█▪██▌                                                        
    ▐█· ▐█▌▐▀▀▪▄▄█▀▀█ ▐█· ▐█▌██▪  ▐█·▐▀▀▪▄▄▀▀▀█▄ ▐█.▪    ▄█▀▀█ ▐█▀▀█▄▐█·██▪  ▐█· ▐█.▪▐█▌▐█▪                                                        
    ██. ██ ▐█▄▄▌▐█ ▪▐▌██. ██ ▐█▌▐▌▐█▌▐█▄▄▌▐█▄▪▐█ ▐█▌·    ▐█ ▪▐▌██▄▪▐█▐█▌▐█▌▐▌▐█▌ ▐█▌· ▐█▀·.                                                        
    ▀▀▀▀▀•  ▀▀▀  ▀  ▀ ▀▀▀▀▀• .▀▀▀ ▀▀▀ ▀▀▀  ▀▀▀▀  ▀▀▀      ▀  ▀ ·▀▀▀▀ ▀▀▀.▀▀▀ ▀▀▀ ▀▀▀   ▀ •                                                         
    ▄▄▄· .▄▄ · ▄▄▄▄▄▄▄▄        ▄▄▄▄▄ ▄ .▄▄• ▄▌ ▐ ▄ ·▄▄▄▄  ▄▄▄ .▄▄▄                                                                                
    ▐█ ▀█ ▐█ ▀. •██  ▀▄ █·▪     •██  ██▪▐██▪██▌•█▌▐███▪ ██ ▀▄.▀·▀▄ █·                                                                              
    ▄█▀▀█ ▄▀▀▀█▄ ▐█.▪▐▀▀▄  ▄█▀▄  ▐█.▪██▀▐██▌▐█▌▐█▐▐▌▐█· ▐█▌▐▀▀▪▄▐▀▀▄                                                                               
    ▐█ ▪▐▌▐█▄▪▐█ ▐█▌·▐█•█▌▐█▌.▐▌ ▐█▌·██▌▐▀▐█▄█▌██▐█▌██. ██ ▐█▄▄▌▐█•█▌                                                                              
    ▀  ▀  ▀▀▀▀  ▀▀▀ .▀  ▀ ▀█▄▀▪ ▀▀▀ ▀▀▀ · ▀▀▀ ▀▀ █▪▀▀▀▀▀•  ▀▀▀ .▀  ▀ ▀                                                                            ''')
    else:
        print('ur dumb')

    print('you see an army of skeletons')
    skeletons=character('skeletons',200,15,2,0,200,0,0,0,0)
    Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,skeletons.name,skeletons.hp,skeletons.dmg,skeletons.dodging,skeletons.priority,skeletons.maxhealth,skeletons.applepie,skeletons.astrothunder,skeletons.sickomode,SuperPoints)
    print('nice job')
    Travis.Upgrade('')
    print('you see a butterfly')
    pause()
    print('you reach out to touch it and thousands more appear and charge at you')
    print('\n')
    pause()
    print('roll to dodge')
    pause()
    diceroll=Dice('you')
    Travis.hp-=diceroll*4
    print(f'you take {diceroll*5} damage')
    if Travis.hp <=0:
        dead='yes'
    else:
        pass
    print('you get an upgrade and 5 superpoints')
    SuperPoints+=5
    Travis.Upgrade('')
    print('drake appears.')
    pause()
    print('you will fight to see who makes it to utopia.')
    Drake=character('Drake',100,20,4,2,100,0,0,0,40)
    Travis.hp,SuperPoints=Combat(Travis.hp,Travis.dmg,Travis.dodging,Travis.priority,Travis.maxhealth,Travis.applepie,Travis.astrothunder,Travis.sickomode,Drake.name,Drake.hp,Drake.dmg,Drake.dodging,Drake.priority,Drake.maxhealth,Drake.applepie,Drake.astrothunder,Drake.sickomode,SuperPoints)
    Travis.Upgrade('')
    print('you have defeated Drake.')
    pause()
    print('you now have the ability called sicko mode.')
    pause()
    print('base sicko mode deals 30 damage and heals for 30 health')
    pause()
    pause('you will go to utopia')

    
    Travis.hp=Travis.maxhealth
    print(f'travis healed back to {Travis.maxhealth} health')
    print(''' █████   ███   █████          ████                                            
░░███   ░███  ░░███          ░░███                                            
 ░███   ░███   ░███   ██████  ░███   ██████   ██████  █████████████    ██████ 
 ░███   ░███   ░███  ███░░███ ░███  ███░░███ ███░░███░░███░░███░░███  ███░░███
 ░░███  █████  ███  ░███████  ░███ ░███ ░░░ ░███ ░███ ░███ ░███ ░███ ░███████ 
  ░░░█████░█████░   ░███░░░   ░███ ░███  ███░███ ░███ ░███ ░███ ░███ ░███░░░  
    ░░███ ░░███     ░░██████  █████░░██████ ░░██████  █████░███ █████░░██████ 
     ░░░   ░░░       ░░░░░░  ░░░░░  ░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░  
                                                                              
                                                                              
                                                                              
  █████                                                                       
 ░░███                                                                        
 ███████    ██████                                                            
░░░███░    ███░░███                                                           
  ░███    ░███ ░███                                                           
  ░███ ███░███ ░███                                                           
  ░░█████ ░░██████                                                            
   ░░░░░   ░░░░░░                                                             
                                                                              
                                                                              
                                                                              
 █████  █████  █████                        ███                               
░░███  ░░███  ░░███                        ░░░                                
 ░███   ░███  ███████    ██████  ████████  ████   ██████                      
 ░███   ░███ ░░░███░    ███░░███░░███░░███░░███  ░░░░░███                     
 ░███   ░███   ░███    ░███ ░███ ░███ ░███ ░███   ███████                     
 ░███   ░███   ░███ ███░███ ░███ ░███ ░███ ░███  ███░░███                     
 ░░████████    ░░█████ ░░██████  ░███████  █████░░████████                    
  ░░░░░░░░      ░░░░░   ░░░░░░   ░███░░░  ░░░░░  ░░░░░░░░                     
                                 ░███                                         
                                 █████                                        
                                ░░░░░                                         ''')