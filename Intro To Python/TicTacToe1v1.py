import time
play='yes'
win=''
player1name=''
player2name=''
player1letter='X'
player2letter='O'
result=''
player1turn=''
player2turn=''
player1wins=0
player2wins=0
X='player1'
O='player2'
gameplay=''
ties=''
row= 0
column= 0
moves = 0
board=[['_','_','_'],['_','_','_'],['_','_','_']]
def gameboard():
    for i in board:
        print(i)

while play=='yes':
    player1name=input('player 1, what is your name>>  ')
    player2name=input('player 2, what is your name>>  ')

    board=[['_','_','_'],['_','_','_'],['_','_','_']]
    moves=0
    player1result=''
    player2result=''
    gameplay='yes'
    while gameplay=='yes':
        if moves%2==0:
            if player1letter=='X':
                print(f'{player1name}, its your move')
            if player2letter=='X':
                print(f'{player2name}, its your move')

            row= int(input('row(1-3)>> '))-1
            column = int(input('column(1-3)>> '))-1
            try:
                if board[row][column]== '_':
                    board[row][column]='X'
                    gameboard()
                    moves+=1
            except:
                pass

        elif moves%2==1:
            if player1letter=='O':
                print(f'{player1name}, its your move')
            if player2letter=='O':
                print(f'{player2name}, its your move')

            row= int(input('row(1-3)>> '))-1
            column = int(input('column(1-3)>> '))-1
            try:
                if board[row][column]== '_':
                    board[row][column]='O'
                    gameboard()
                    moves+=1
            except:
                pass       
                    
            else:
                print('invalid row or column')
                gameboard()
                
        if moves >=5: # check for win
            for i in range(0,2):
                if board[i][0]==board[i][1]==board[i][2]:
                    win ='yes'
            for c in range(0,2):
                if board[0][c]==board[1][c]==board[2][c]:
                    win ='yes'
            if board[0][0]==board[1][1]==board[2][2]:
                win ='yes'
            elif board[0][2]==board[1][1]==board[2][0]:
                win ='yes'
            if win=='yes':
                gameplay='no'
                if moves%2==1:
                    if X=='player1':
                        player1wins+=1
                    else:
                        player2wins+=1
                    result=X
                elif moves%2==0:
                    if O=='player1':
                        player1wins+=1
                    else:
                        player2wins+=1
                    result=X
                if result=='player1':
                    print(f'{player1name} wins!')
                if result=='player2':
                    print(f'{player2name} wins!')
            else:
                pass
        if moves==9:
            result='tie'
            ties+=1
            print('tie!')



    #end of game stuff to keep playing and restart     
    print(f'{player1name} has {player1wins} and {player2name} has {player2wins} and there have been {ties} ties')       
    play=input('want to keep playing>>  ')
    if player1letter=='X':
        player1letter='O'
        player2letter="X"
        X='player2'
        O='player1'
    if player1letter=='O':
        player1letter='X'
        player2letter="O"
        X='player1'
        O='player2'




