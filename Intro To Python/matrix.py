
a=[[0,0],[0,0]]
b=[[0,0],[0,0]]
c=[[0,0],[0,0]]
d=[[0,0],[0,0]]
for i in range(0,len(a[0])):
    for j in range(0,len(a[0])):
        a[i][j]=int(input('>> '))
        b[i][j]=int(input('>> '))

for i in range(0,len(a[0])):
    for j in range(0,len(a[0])):
        c[i][j]=a[i][j]+b[i][j]
print(f'adding the lists together results in')
for i in c:
    for j in i:
        print(f'{j} ')