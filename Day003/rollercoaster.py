#its a rollercoaster ticket counter
print("Rollercoaster ticket counter")
height = eval(input("Enter your height(CM): "))
if (height >= 120):
    print("you can ride rollercoaster")
    age = int(input("please enter your age: "))
    if (age >= 18):
        print("please pay $15 ")
    elif (age < 18 and age > 12 ):
        print("please pay $12")
    else :
        print("please pay $10 ")
else:
    print("Sorry you can't ride the rollercoaster")