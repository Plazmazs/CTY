actualword='earth'
print('Welcome to Wordle, you have 6 chances to guess a 5 letter word,. Good luck!')
validguess='no'
letter1=actualword[0]
letter2=actualword[1]
letter3=actualword[2]
letter4=actualword[3]
letter5=actualword[4]
letters=[letter1,letter2,letter3,letter4,letter5]

guess1=""
guess2=""
guess3=""
guess4=""
guess5=""
guess6=""
guesses=0
board=[['_','_','_','_','_'],['_','_','_','_','_'],['_','_','_','_','_'],['_','_','_','_','_'],['_','_','_','_','_'],['_','_','_','_','_']]
for a in board:
    print(a)
        
while guesses<6:
    guess=input('What is your guess? >> ')
    if len(guess)==5:
        try:
            guess=str(guess)         
            if guess == actualword:
                print('You won!')
                guesses=6
            else:
                for b in range(0,5):
                    if guess[b]==letters[b]:
                        board[guesses][b]=guess[b].capitalize()
                    else:
                        board[guesses][b]=guess[b]
                    
            for a in board:
                print(a)
            guesses+=1             
        except:
            pass
    else:
        pass
    
    

    