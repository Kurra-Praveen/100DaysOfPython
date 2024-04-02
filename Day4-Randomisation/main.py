import random

print("What do you choose? Type 0 for Rock ,! for Paper,2 for Scissors ")
choice=int(input("Enter your choice :"))
computerChoice=random.randint(0,2)
if choice==0 and computerChoice==2:
    print("You wins")
elif computerChoice >choice:
    print("computer wins")
elif computerChoice==choice:
    print("Match drawn !!!")
else :
    print("Invalid input.."
          "")





