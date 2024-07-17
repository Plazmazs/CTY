brawlers = ["Angelo" , " Leon", "Dynamike", "Berry"]
x = "y"
add= ""
while x == "y" :
    y= (input("What brawler would you like to add: "))
    brawlers.append(y)
    x = input("Type y to add to the list: ")
print(brawlers)

newBrawlers = []
for i in brawlers:
    add= input("would you like to add", i )
    if(add=="yes"):
        newBrawlers.append(i)




print(newBrawlers)