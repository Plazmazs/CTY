grade = input()
x = 'yes'
try:
    grade=int(grade)

except:
    try:
        grade=float(grade)
    
    except:
        print("invalid")
        x= 'no'

if(x=='yes'):
    if(grade>100 or grade<0 ):
        print('invalid input')

    elif(grade>=90):
        print('a')

    elif(grade>=80):
        print('b')

    elif(grade>=70):
        print('c')  

    elif(grade>= 60):
        print('d')

    elif(grade>=0):
        print('f')

