import random
import time

diceroll = 0
# health starts at 80 
health = 80
# sanity starts at 9 with a max of 10
sanity = 9
# money starts at $20
money = 20
# 1 to 24, military time
# JAUNT
clock = 6
healthloss =int
action = ''
caught= 0
fight= 0
escape= 0
def Stats(v1,v2,v3,v4): #stats
    print ("Health:",v1," money:",v2," time:",v3," sanity:",v4)
Stats(health,money,clock,sanity)
# bunker in the forest with phones and bombs, gingers are evil
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

name = input("Hello, what is your mame >> ")
print(f'hello {name}, you are a student who has recently moved from pasadena california')
pause()
print('to a small town in pennsilvania called doylestown')
pause()
print(f'you are entering 10th grade at the highschool Central Bucks North')
pause()
print('the year is 2040 and phones and other devices have been outlawed')
pause()
print(f'you have your first day tomorrow at school and want to be prepared.')
pause()
print('there is a wawa, a ymca, a park, a walmart, as well as an dense forest called Wailing Woods.')
pause()
print('You will roll a dice after each decision you make.')
pause()
print('you start with 80 health you have 9 sanity with a max of 10 as well as starting with 20 dollars.')
pause()

sleepIn=input('You wake up at 6 o clock(military time), would you like to sleep in(yes or no)>>  ')
diceroll=Dice()


if (sleepIn == "yes"):
    if(diceroll<=4):
        clock = 15
        print('you slept in way too late!')
    elif(diceroll<=15):
        health += 5
        clock = 12
    elif(diceroll>15):
        health =+ 15
        clock = 12
        print('you got an awesome sleep')
else:
    if(diceroll<=10):
        health -= 5
        clock = 6
        print('you are tired')
    elif(diceroll>10):
        clock= 6
Stats(health,money,clock,sanity)
cindyfriend= "no"
pause()

if (clock == 6):
    print('you watch the news. today will be a real burner, 92 degrees and it wont be any cooler in the near future. In other news an Irish man was taken away and sent to the caverns after being discovered with a phone. a young kid named Billy Stewart has gone missing. There have been reported noises coming from Wailing Woods')
    clock = 8
    pause()
    action = input('do you want to water the neighbors plants for 5 dollars?')

if(action=='yes'):    #going to water plants
    print('your neighbor a few houses down gave you and your family cookies when you moved in.')
    pause()
    print('it is a 70 year old grandma in a rundown blue house, her name is cindy')
    gingerEncounterCindyHouse =""
    pause()
    diceroll=Dice()
    
    if(diceroll<12):
        print('you are watering the plant and cindy goes inside after being on her porch.')
        pause()
        print('you notice a young man maybe 18 years old walking on the sidewalk staring at you. his face looks hollow and he looks starved. he has flecks of dried blood around his mouth. he is 5 foot nine and has orange hair and a tattered hoodie and jeans')
        pause()
        gingerEncounterCindyHouse = input('would you like to (go) inside, run (home), approach>> ')
        pause()
        diceroll=Dice()
    else:
        print('you water the plants and cindy gives you five dollars')
        pause()
        money+= 5
        Stats(health,money,clock,sanity)
        diceroll=Dice()

        if(diceroll <11):
            print('you walk home and chill out for a while')
            clock=12
        else:
            print('you see a fast shuffling in the house then the old woman walks out, odd considering she said no one lived with her.')
            diceroll=Dice()
            if(diceroll<10):
                print('cindy gives you 2 extra dollars for your hard work')
                money=+2
            elif(diceroll<17):
                print('cindy gives you a 10 dollar tip and says you are her friend.')
                money=+10
            else:
                print('cindy gives you a 10 dollar tip and says you are her friend.')
                pause()
                print('as you are walking away, you see the skin of the old woman fall and a young man around 5 foot nine and ginger hair, skinwalker?')
                money =+10
                clock=12


if(gingerEncounterCindyHouse=="inside"): #choose inside
    if(diceroll<5):
        print('the door is locked, the man walks directly at you')
        gingerEncounterCindyHouse= input('run or fight')
        pause()
        if(gingerEncounterCindyHouse=='run'):
            diceroll=Dice()
            if(diceroll<8):
                caught =1
            else: #got away
                escape=1             
        else:     # fight
            fight=1

            
    else:
        print('you run and open the door, closing it behind you')
        diceroll=Dice()

        if(diceroll<7):
            print('you turn around and see cindy shedding her skin into a 25ish year old red-headed man with bloodshot eyes.')
            gingerEncounterCindyHouse = input('run(out the back),fight (cindy)')

        elif(diceroll<15):
            print('you get inside the house and lock the door. You do not see cindy anywhere. The man outside waits for a while then walks away. You hear shuffling upstairs and Cindy comes down. ')
            print('cindy gives you 4 dollars for your work')
            money=+4
        else:
            print('you hear running upstairs and cindy comes down but you notice a strand of red hair on her, odd considering that she has gray hair, also flecks on blood on her hair. odd.')
            print('cindy gives you 4 dollars for your work')
            money=+4
# inside
if(gingerEncounterCindyHouse=="approach"): #choose approach

else: #run 
    diceroll=Dice()
    if diceroll<6:
        caught= 1
        


if caught==1: #caught
    print('the man runs you down and tackles you to the floor')
    diceroll=Dice()
                
    healthloss = int(diceroll*3)
    print(f'you lost {healthloss} health')
    health -= healthloss
    Stats(health,money,clock,sanity)
    if(health<=0):
        SystemExit('you died!')
    gingerEncounterCindyHouse= input('run or fight')
    if(gingerEncounterCindyHouse=='run'):
        diceroll=Dice()
        if(diceroll<15):
            print('he tracks you down again')
            diceroll=Dice()
            healthloss = int((20-diceroll)*3)
            print(f'you lost {healthloss} health')
            Stats(health,money,clock,sanity)
            fight=1
    else: #got away
        escape=1
        

if fight==1:
    diceroll=Dice()
            
    if(diceroll<5):
        print('he lands a mean right hook')
        diceroll=Dice()

        healthloss = (20-diceroll) * 4
    elif(diceroll<10):
        print('he hits you in the shoulder')
        diceroll=Dice()

        healthloss = (20-diceroll) *2

    elif(diceroll<15):
        print('he misses and falls over')
    elif(diceroll<20):
        print('you pick up a big metal rod and smash it over his head, knocking him out on impact')
        print('you search the body and find an id card ')

if escape==1:
    print('he trips and runs away, you got home and made yourself some food')
    health =+ 5
    Stats(health,money,clock,sanity)    
