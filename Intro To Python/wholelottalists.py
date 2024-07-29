givenlist=[4,'moo',7,'cow','moose',36,2.3,53.1,34]
nonint=0
for i in givenlist:
    try:
        i=float(i)
        if i%1==0:
            pass
        else:
            nonint+=1
    except:
        nonint+=1
print(f'{nonint} non intigers')
        

numberlist=[]
for i in givenlist:
    try:
        i=float(i)
        numberlist.append(i)
    except:
        try:
            i=int(i)
            numberlist.append(i)
        except:
            print("invalid")
            y= 'no'

print(numberlist)


    