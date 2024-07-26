actualword='stick'
print('Welcome to Wordle, you have 6 chances to guess a 5 letter word, good luck.')
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

            

while guesses<6:
    guess=input('what is your guess>> ')
    if len(guess)==5:
        try:
            guess=str(guess)
            if guesses==0:
                guess1=guess
                guesses+=1
                for i in range[0,4]:
                    board[0][i]=guess1[i]
                    print(board)
                
            if guesses==1:
                guess1=guess
                guesses+=1
                

        except:
            pass
    else:
        pass
    
    

    