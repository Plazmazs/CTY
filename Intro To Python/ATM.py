five = 0
one = 0
ten = 0
end = 'no'
password = 1234
balance = 0
newpassword = 0
deposit = 0
start = "no"


guess = int(input('what is the password'))
try:
    guess=int(guess)
except:
    print("invalid")


if(guess==password):
    start = "yes"
else:
    guess = input('what is the password')
    try:
        guess=int(guess)
    except:
        print("invalid")
    if(guess==password):
        start = "yes"
    else:
        guess = input('what is the password')
        try:
            guess=int(guess)
        except:
            print("invalid")
        if(guess==password):
            start = "yes"
        else:
            pass


if(start=="yes"):
    x = input(f'your password is {password}, you can withdraw, password(to change it), deposit, or check(balance) or stop to stop.')

try:
    x=str(x)
    while(x !="stop"):
        if(x=='withdraw'):
            withdraw = input("how much would you like to withdraw")
            try:
                withdraw=int(withdraw)
                if(withdraw>=0):
                    balance = balance - withdraw
                    while withdraw>=10:
                        withdraw = withdraw-10
                        ten = ten + 1
                    while withdraw>=5:
                        withdraw = withdraw-5
                        five = five + 1
                    while withdraw>=1:
                        withdraw = withdraw-1
                        one = one + 1
                    print(f'{ten} tens, {five} fives, and {one} ones')
                else:
                    print('invalid')
            except:
                print("invalid")
            x = input(f'your password is {password}, you can withdraw, password(to change it), deposit, or check(balance) or stop to stop.')

        elif(x=='password'):
            newpassword = input('make a 4 digit password')
            try:
                newpassword=int(newpassword)
                if(newpassword<9999):
                    password = newpassword 
                else:
                   print("invalid") 
            except:
                print("invalid")
            x = input(f'your password is {password}, you can withdraw, password(to change it), deposit, or check(balance) or stop to stop.')
        elif(x=='deposit'):
            deposit= input('how much would you like to deposit')
            try:
                deposit=int(deposit)
                if(deposit>=0):
                    balance = balance + deposit
                else:
                    print('invalid')
            except:
                print("invalid")
            x = input(f'your password is {password}, you can withdraw, password(to change it), deposit, or check(balance) or stop to stop.')
        elif(x=='check'):
            print(f'you have {balance} dollars.')
            x = input(f'your password is {password}, you can withdraw, password(to change it), deposit, or check(balance) or stop to stop.')
        
except:
    print("invalid")
