import random
import time
money=0
DealerScore =0
player1Score = 0
player1Score2 = 0
player1Score3 = 0
player1Score4 = 0
player2Score = 0
player2Score2 = 0
player2Score3 = 0
player2Score4 = 0
CardScore=0
wager = 0
MoveOn= 'no'
randomcard=''
action=''
insurance=''
spilt=''

card1='' 
card2=''
card3=''
card4=''
card5=''
card6=''
card7=''
card8=''
card9=''
card10=''
card11=''
card12=''
card13=''
card14=''
card15=''
card16=''
card17=''
card18=''
card19=''
card20=''
card21=''
card22=''
card23=''
card24=''
card25=''
card26=''
card27=''
card28=''
card29=''
card30=''

card1score=0
card2score=0
card3score=0
card4score=0
card5score=0
card6score=0
card7score=0
card8score=0
card9score=0
card10score=0
card11score=0
card12score=0
card13score=0
card14score=0
card15score=0
card16score=0
card17score=0
card18score=0
card19score=0
card20score=0
card21score=0
card22score=0
card23score=0
card24score=0
card25score=0
card26score=0
card27score=0
card28score=0
card29score=0
card30score=0

def pause(): #pause() for 2 sec
    import time
    time.sleep(1)

def Card():
    cardlist = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
    randomcard = cardlist[random.randint(0,12)]
    return randomcard
randomcard=Card()
def ScoreAssign():
    if randomcard == 'Two':
        CardScore=2
    elif randomcard == 'Three':
        CardScore=3
    elif randomcard == 'Four':
        CardScore=4
    elif randomcard == 'Five':
        CardScore=5
    elif randomcard == 'Six':
        CardScore=6
    elif randomcard == 'Seven':
        CardScore=7
    elif randomcard == 'Eight':
        CardScore=8
    elif randomcard == 'Nine':
        CardScore=9
    elif randomcard == 'Ten':
        CardScore=10
    elif randomcard == 'Jack':
        CardScore=10
    elif randomcard == 'Queen':
        CardScore=10
    elif randomcard == 'King':
        CardScore=10
    elif randomcard == 'Ace':
        CardScore=11
    return CardScore

listofcards= [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15,card16,card17,card18,card19,card20,card21,card22,card23,card24,card25,card26,card27,card28,card29,card30]
listofcardvalues=[card1score,card2score,card3score,card4score,card5score,card6score,card7score,card8score,card9score,card10score,card11score,card12score,card13score,card14score,card15score,card16score,card17score,card18score,card19score,card20score,card21score,card22score,card23score,card24score,card25score,card26score,card27score,card28score,card29score,card30score]

for i in range(0,29):
    randomcard=Card()
    listofcards[i]=randomcard
    print(listofcards[i])
    CardScore=ScoreAssign()
    listofcardvalues[i]=CardScore
    print(listofcardvalues[i])

print('Hello, welcome to Blackjack.')
while MoveOn == 'no':
    wager = input('How much would you like to wager?')
    try:
        wager=int(wager)
        MoveOn = 'yes'
        money -= wager
    except:
        print("invalid")

#actual game
#dealer
DealerScore += card1score
print(f'The dealer has a(n) {card1}, face up') 
pause()
print(f'the dealer score is currently {DealerScore} without their other card')
    #player1
player1Score += card3score
print(f'You have been dealt a(n) {card3}')   
pause()

player1Score += card4score
print(f'You have been dealt a(n) {card4}')
pause()

print(f'your total score is currently {player1Score}')
pause()

MoveOn='no'
while MoveOn == 'no':
    action = input('would you like to hit, stand, double bet, insurance, or spilt') #action
    try:
        wager=str(wager)
        MoveOn = 'yes'
    except:
        print("invalid")

#if statements
    if action == 'insurance':
        if card1== 'ace':
            print('insurance used')
            if card2score==10:
                money += wager/2
        else:
            print('Cannot use insurance unless the dealer has an ace face up')

    if action == 'spilt':
        if card3==card4:
            player1Score==card3
            player1Score2=card4
        else:
            print('cannot spilt, different values')