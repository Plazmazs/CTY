import random
import time
money=0
DealerScore =0
CardScore=0
wager = 0
MoveOn= 'no'
randomcard=''
action=''
insurance=''
spilt=''
continueplaying='yes'
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
winlosstie=''
continuefoward=''
def pause(): #pause() for 2 sec
    import time
    time.sleep(2)

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

def winlosscheck(v1,v2):
    if(v1)>21:
        winlosstie='loss'
        MoveOn='yes'
        print('you busted!')
        

    elif(v1==21):
        if v1==v2:
            winlosstie='tie'
            MoveOn='yes'
            print('push')
            
        if v1>v2:
            winlosstie='win'
            MoveOn='yes'
            print('you won!')
    elif(v1<21):
        winlosstie=''
        MoveOn='no'

    return(winlosstie,MoveOn,)
    

while continueplaying=='yes':
    player1Score = 0
    DealerScore=0
    listofcards=[card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15,card16,card17,card18,card19,card20,card21,card22,card23,card24,card25,card26,card27,card28,card29,card30]
    listofcardvalues=[card1score,card2score,card3score,card4score,card5score,card6score,card7score,card8score,card9score,card10score,card11score,card12score,card13score,card14score,card15score,card16score,card17score,card18score,card19score,card20score,card21score,card22score,card23score,card24score,card25score,card26score,card27score,card28score,card29score,card30score]

    for i in range(0,29):
        randomcard=Card()
        listofcards[i]=randomcard
        CardScore=ScoreAssign()
        listofcardvalues[i]=CardScore
        

    card1=listofcards[0]
    card2=listofcards[1]
    card3=listofcards[2]
    card4=listofcards[3]
    card5=listofcards[4]
    card6=listofcards[5]
    card7=listofcards[6]
    card8=listofcards[7]
    card9=listofcards[8]
    card10=listofcards[9]
    card11=listofcards[10]
    card12=listofcards[11]
    card13=listofcards[12]
    card14=listofcards[13]
    card15=listofcards[14]
    card16=listofcards[15]
    card17=listofcards[16]
    card18=listofcards[17]
    card19=listofcards[18]
    card20=listofcards[19]
    card21=listofcards[20]
    card22=listofcards[21]
    card23=listofcards[22]
    card24=listofcards[23]
    card25=listofcards[24]
    card26=listofcards[25]
    card27=listofcards[26]
    card28=listofcards[27]
    card29=listofcards[28]
    card30=listofcards[29]

    card1score=listofcardvalues[0]
    card2score=listofcardvalues[1]
    card3score=listofcardvalues[2]
    card4score=listofcardvalues[3]
    card5score=listofcardvalues[4]
    card6score=listofcardvalues[5]
    card7score=listofcardvalues[6]
    card8score=listofcardvalues[7]
    card9score=listofcardvalues[8]
    card10score=listofcardvalues[9]
    card11score=listofcardvalues[10]
    card12score=listofcardvalues[11]
    card13score=listofcardvalues[12]
    card14score=listofcardvalues[13]
    card15score=listofcardvalues[14]
    card16score=listofcardvalues[15]
    card17score=listofcardvalues[16]
    card18score=listofcardvalues[17]
    card19score=listofcardvalues[18]
    card20score=listofcardvalues[19]
    card21score=listofcardvalues[20]
    card22score=listofcardvalues[21]
    card23score=listofcardvalues[22]
    card24score=listofcardvalues[23]
    card25score=listofcardvalues[24]
    card26score=listofcardvalues[25]
    card27score=listofcardvalues[26]
    card28score=listofcardvalues[27]
    card29score=listofcardvalues[28]
    card30score=listofcardvalues[29]

    print('Hello, welcome to Blackjack.')
    while MoveOn == 'no':
        wager = input('How much would you like to wager?')
        try:
            wager=int(wager)
            MoveOn ='yes'
            money -= wager
        except:
            print("invalid")


    #actual game
    #dealer
    DealerScore += card1score
    DealerScore += card2score
    print(f'The dealer has a(n) {card1}, face up') 
    pause()
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
        action = input('would you like to hit, stand, double(the bet), or insurance') #action

    #if statements
        if action == 'insurance':
            if card1== 'Ace':
                print('insurance used')
                if card2score==10:
                    money += wager/2
                else:
                    continuefoward='no'
                MoveOn='yes'
            else:
                print('Cannot use insurance unless the dealer has an Ace face up')
        elif action =='double':
            money -= wager
            wager = wager*2
            print('doubled')
            action='hit'
        elif action == 'stand':
            MoveOn= 'yes'

        elif action=='hit':
            player1Score += card5score
            print(f'You have been dealt a(n) {card5}')
            print(f'your total score is currently {player1Score}')
            pause()
            continuefoward='no'
            winlosstie =winlosscheck(player1Score,DealerScore)
            MoveOn='yes'
            if winlosstie== 'win' or winlosstie == 'tie' or winlosstie=='loss'or player1Score>=21:
                continuefoward='yes'
                MoveOn='yes'
                action=''
                print('blackjack')
            if continuefoward=='no':
                action = input('would you like to hit or stand') #action
        
        if action=='hit':
            player1Score += card6score
            print(f'You have been dealt a(n) {card6}')
            print(f'your total score is currently {player1Score}')
            pause()
            continuefoward='no'
            winlosstie = winlosscheck(player1Score,DealerScore)
            if winlosstie== 'win' or winlosstie == 'tie' or winlosstie=='loss' or player1Score>=21 :
                MoveOn='yes'
                continuefoward='yes'
                action=''
                print('blackjack')
            if continuefoward=='no':
                action = input('would you like to hit or stand') #action
                
                if action=='hit':
                    player1Score += card7score
                    print(f'You have been dealt a(n) {card7}')
                    print(f'your total score is currently {player1Score}')
                    pause()
                    continuefoward='no'
                    winlosstie = winlosscheck(player1Score,DealerScore)
                    if winlosstie== 'win' or winlosstie == 'tie'or winlosstie=='loss'or player1Score>=21:
                        continuefoward='yes'
                        MoveOn='yes'
                        action=''
                        print('blackjack')
                    if continuefoward=='no':
                        action = input('would you like to hit or stand') #action
                        
                        if action=='hit':
                            player1Score += card8score
                            print(f'You have been dealt a(n) {card8}')
                            print(f'your total score is currently {player1Score}')
                            pause()
                            continuefoward='no'
                            winlosstie = winlosscheck(player1Score,DealerScore)
                            if winlosstie== 'win' or winlosstie == 'tie'or winlosstie=='loss'or player1Score>=21:
                                continuefoward='yes'
                                MoveOn='yes'
                                action=''
                                print('blackjack')
                            if continuefoward=='no':
                                action = input('would you like to hit or stand') #action
                                
                                if action=='hit':
                                    player1Score += card9score
                                    print(f'You have been dealt a(n) {card9}')
                                    print(f'your total score is currently {player1Score}')
                                    pause()
                                    continuefoward='no'
                                    winlosstie = winlosscheck(player1Score,DealerScore)
                                    if winlosstie== 'win' or winlosstie == 'tie'or winlosstie=='loss'or player1Score>=21:
                                        continuefoward='yes'
                                        MoveOn='yes'
                                        action=''
                                elif action == 'stand':
                                    continuefoward='yes'
                                    action =''
                                else:
                                    continuefoward='yes'
                                    action =''
                        elif action == 'stand':
                            continuefoward='yes'
                            action =''
                        else:
                            continuefoward='yes'
                            action =''
                elif action == 'stand':
                    continuefoward='yes'
                    action =''
                else:
                    continuefoward='yes'    
                    action =''    
        elif action == 'stand':
            continuefoward='yes'
            action =''
        else:
            continuefoward='yes'
            action =''
    else:
        continuefoward='yes'
        action =''
        
    if winlosstie== 'yes':
        money+= wager*2
    elif winlosstie== 'tie':
        money+= wager
    else:
        continuefoward='no'
        action =''

    MoveOn='no'
    

    if winlosstie== 'yes':
        money+= wager*2
    elif winlosstie== 'tie':
        money+= wager
    elif player1Score ==21:     
        money+= wager*2
    elif player1Score >21:     
        pass
    else:
        print(f'the dealer has {DealerScore}')
        if DealerScore>21:
            money+= wager*2
            print('the house busted!!')
        elif DealerScore>player1Score:
            print(f'dealer wins {DealerScore} to {player1Score}')
            
        else:
            DealerScore += card10score
            print(f'The dealer got an {card10}')
            print(f'the dealer has {DealerScore}')
            pause()
            if DealerScore>21:
                money+= wager*2
                print('the house busted!!')
            elif DealerScore>player1Score:
                print(f'dealer wins {DealerScore} to {player1Score}')
            elif DealerScore>=17:
                money+= wager*2
            else:
                DealerScore += card11score
                print(f'The dealer also has a(n) {card11}')
                print(f'the dealer has {DealerScore}')
                pause()
                if DealerScore>21:
                    money+= wager*2
                    print('the house busted!!')
                elif DealerScore>player1Score:
                    print(f'dealer wins {DealerScore} to {player1Score}')
                elif DealerScore>=17:
                    money+= wager*2
                else:
                    DealerScore += card12score
                    print(f'The dealer also has a(n) {card12}')
                    print(f'the dealer has {DealerScore}')
                    pause()
                    if DealerScore>21:
                        money+= wager*2
                        print('the house busted!!')
                    if DealerScore>player1Score:
                        print(f'dealer wins {DealerScore} to {player1Score}')
                    elif DealerScore>=17:
                        money+= wager*2
    print(f'you have {money} dollars')
    continueplaying=str(input('want to keep playing?'))

print('hope you enjoyed')