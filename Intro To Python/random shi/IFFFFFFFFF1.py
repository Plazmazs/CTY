x= input('')
y = 'yes'
try:
    x=int(x)

except:
    try:
        x=float(x)
    
    except:
        print("invalid")
        y= 'no'

if(y=='yes'):
    if(x>0):
        if(x%10==0):
            print("last digit equal to 0")
        else:
            if(x%10==1):
                print('last digit equal to 1')
            else:
                print('none')
    
    else:
        if(x==-1):
            print('bye')
        else:
            print('invalid number')