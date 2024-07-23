weight = input('weight?')
destination = input('destination')
z = 'yes'
cost = int
try:
    weight=int(weight)

except:
    try:
        weight=float(weight)
    
    except:
        print("invalid")
        z= 'no'

try:
    destination=str(destination)

except:
    print("invalid")
    z= 'no'
if(weight <0):
    z= 'no'

if(z=='yes'):
    if(destination=='I'):
        if(weight<=1):
            cost= weight *.01
            print(f'shipping cost:{cost}')

        elif(weight<=2):
            cost= weight *.013
            print(f'shipping cost:{cost}')
        elif(weight<=4):
            cost= weight *.015
            print(f'shipping cost:{cost}')
        else:
            cost= weight *.02
            print(f'shipping cost:{cost}')
    else:
        if(weight<=1):
            cost= 10
            print(f'shipping cost:{cost}')

        elif(weight<=2):
            cost= 20
            print(f'shipping cost:{cost}')
        elif(weight<=4):
            cost= 40
            print(f'shipping cost:{cost}')
        else:
            cost= 60
            print(f'shipping cost:{cost}')
            