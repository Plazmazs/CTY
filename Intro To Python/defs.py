a=[1.1,5,.25,7,8,9.1,2.2,3.2]
max=0
def maximum(v1):
    max=v1[0]
    for i in v1:
        if i>max:
            max=i
    return max
maximum(a)
print(max)

