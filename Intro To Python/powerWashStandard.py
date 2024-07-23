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



x= input('')
y = 'yes'
try:
    x=int(x)

except:
    print("invalid")
    y= 'no'

                