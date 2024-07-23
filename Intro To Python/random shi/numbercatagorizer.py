x = input('')


try:
    x=int(x)
    print('number')
    if(x/3==int):
        print(f'{x} is divisble by 3')
    if(x%2==0):
        print('even')
    else:
        print('odd')
    if(x==0):
        print('zero')
    elif(x>0):
        print('positive')
    elif(x<0):
        print('negative')


    if(x<1000 and x>-1000):
        print('the absolute value of x is less than 1000')

        
except:
    try:
        if(x==float(x)):
            print('float')
        if(x==0):
            print('zero')
        elif(x>0):
            print('positive')
        elif(x<0):
            print('negative')


        if(x<1000 and x>-1000):
            print('the absolute value of x is less than 1000')

    except:
        print('string')

