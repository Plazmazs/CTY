import random
diceroll = random.randint(0,20)
# health starts and 10 and has a max of 15
health = 10
# sanity starts at 9 with a max of 10
sanity = 9
# money starts at $20
money = 20
# 1 to 24, military time
time = 6
stats = f'health:{health} sanity:{sanity} money:{money} time:{time}'

# bunker in the forest with phones and bombs, gingers are evil

name = input("Hello, what is your mame >> ")
print(f'hello {name}, you are a student who has recently moved from pasadena california to a small town in pennsilvania called doylestown')
print(f'you are entering 10th grade at the highschool Central Bucks North, the year is 2040 and phones and other devices have been outlawed')
print(f'you have your first day tomorrow at school and want to be prepared. there is a wawa, a ymca, a park, a walmart, as well as an dense forest. You will roll a dice after each decision you make. you start with 10 health with a max of 15, you have 9 snaity with a max of 10 and 20 dollars.')
print(stats)
sleepIn=input('You wake up at 6 o clock(military time), would you like to sleep in(yes or no)>>  ')


if (sleepIn == "yes"):
    health = health +1
    time = 11
    print(stats)
else:
    health = health - 1
    print(stats)

if (time == "6"):
    print('you watch the news, reports of ')