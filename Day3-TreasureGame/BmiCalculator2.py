# height = float(input("enter you height :"))
# weight = float(input("enter your weight "))
# bmi = round(weight / height ** 2)
bmi = 24
print(bmi)
if bmi < 18.5:
    print("You are under Weight ")
elif 25 > bmi > 18.5:
    print("you are Normal weight")
elif bmi < 30:
    print("You are over weight")
elif 30 > bmi < 35:
    print("you are Obese")
else:
    print("you are clinically obese")
