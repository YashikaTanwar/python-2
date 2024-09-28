print("Select your ride:")
print("1. Bike")
print("2. Car")

# select your ride
choice=int(input("Enter your choice:"))
if(choice==1):
    print("What type of bike?")
    print("1. Scooty")
    print("2. Bike")

    # condition for selecting type of bike
    choice2=int(input("Select type of bike"))
    if choice2==1:
        print("you have selected scooty")
    else:
        print("you have selected bike")

elif(choice==2):
    print("What type of Car?")
    print("1. Sedan")
    print("2. XUV")
    choice3=int(input("Enter your choice:"))
    if choice3==1:
        print("you have selected sedan")
    else:
        print("you have selected XUV")
else:
    print("wrong choice")