

x= [1,2,3]
try:
    z= int(input(">>  "))
            
    if (z <=0 and z>=4):
        print("no")
        print(x)
    else:
        x.append(z)
        print(x)
except:
        print('error')
        print(x)
    