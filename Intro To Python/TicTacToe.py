import random

start='no'
team = ''
row= 0
column= 0
ai= 'yes'
aiturn= ''
turn = 'no'
end = 0
win = ''
corner=''
edge=''
A= 0 # ai failed moves
board=[['_','_','_'],['_','_','_'],['_','_','_']]
for i in board:
    print(i)

while start=='no': #X or O
    team = input('X or O')
    if team == "X":
        start = 'yes'
        turn = 'yes'
        ai = "O"
        aiturn= 'no'
    elif team == "O":
        start = 'yes'
        turn = 'no'
        ai = "X"

while start=='yes':
    if win =='yes':
        print('win')
        start=""
    elif end == 9:
        print('tie')
        start=""
    elif win =='no':
        print('loss')
        start=""


    if turn =='yes':    
        row= int(input('row(1-3)>> '))-1
        column = int(input('column(1-3)>> '))-1
        if board[row][column]== '_':
            board[row][column]=team
            for i in board:
                print(i)
            turn = 'no'
            end+=1
            
                
        else:
            print('invalid row or column')
            for i in board:
                print(i)
        if end >=5: # check for win
            for i in range(0,2):
                if board[i][0]==board[i][1]==board[i][2]:
                    win ='yes'
            for c in range(0,2):
                if board[0][c]==board[1][c]==board[2][c]:
                    win ='yes'
            if board[0][0]==board[1][1]==board[2][2]:
                win ='yes'
            if board[0][2]==board[1][1]==board[2][0]:
                win ='yes'

    else:
        #going first
        if end==0:
            row = 1
            column =1

        elif end==2:
            if A==0:
                row = 0
                column =0  
            else:
                row = 2
                column =2

        elif end==4:
            if A==0:
                row = 2
                column =2
            elif A==1:
                row = 0
                column =2
            else:
                row = 2
                column =0

        elif end==6:
            if A==0:
                row = 0
                column =2
            elif A==1:
                row = 2
                column =0
            elif A==2:
                row = 0
                column =1
            else:
                row = 1
                column =0
        #going 2nd
        elif end==1:
            if A==0:
                row = 1
                column =1    
            else:
                row = 0
                column =0

        elif end==3:
            if A==0:
                row = 0
                column =0
            else:
                row = 0
                column =2
    
        



        if board[row][column]== '_':
            board[row][column]=ai
            for i in board:
                print(i)
            turn ='yes'
            end+=1
            A=0
            
        else:
            A=+1
        if end >=5: # check for win
            for i in range(0,2):
                if board[i][0]==board[i][1]==board[i][2]:
                    win ='no'
            for c in range(0,2):
                if board[0][c]==board[1][c]==board[2][c]:
                    win ='no'
            if board[0][0]==board[1][1]==board[2][2]:
                win ='no'
            if board[0][2]==board[1][1]==board[2][0]:
                win ='no'




