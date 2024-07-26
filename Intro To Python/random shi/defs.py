
a=[1.1,5,.25,7,8,9.1,2.2,3.2]
maxi=0


def most(v1):
    maxi =max(v1)
    return maxi
most(a)
print(maxi)



z=0
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
panagramcheck='yes'
panagraminput=''
panagraminput=input('')
def panagram(v1):
    for i in v1:
        if i in panagraminput:
            pass
        else:
            panagramcheck='no'
    return panagramcheck


panagramcheck=panagram(alphabet)

