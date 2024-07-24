even=[]
for i in range(1,100):
    if i%2==0:
        even.append(i)
print(even)


z= 0
matrix = [[1,5,6],[7,8,9],[11,15,-3]]
for j in matrix:
    for r in j:
        if matrix[j][r] <0:
            z =matrix[j][r]
            print(f'the negative number is {z} at {j}, {r}')
    





odd=[]
A=int(input('what is your first edge'))
B=int(input('what is your first edge'))
for i in range(A,B):
    if i%2==1:
        odd.append(i)
print(odd)