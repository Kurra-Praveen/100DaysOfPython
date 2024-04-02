# weight=int(input("Enter weight"))
# yourUnderWeight=20
# if yourUnderWeight==0:
#     print("Under weight is zero")
#
# else:
#     print("Under weight is not zero")





# Under 15: Very severely underweight
# 15 to 18: Underweight
# 25 to 30: Overweight
# 30 to 40: Obese
# Above 40: Very severely obese

weight=int(input("Enter your Weight"))
height=int(input("Enter your height"))

bmi=weight/height
print(bmi)
if bmi<15:
    print("Very severely underweight")
elif bmi>15 and bmi <18:
    print("underweight")
elif bmi>25 and bmi <30:
    print("Over Weight")
elif bmi>30 and bmi <40:
    print("obese")
elif bmi>40:
    print("very severely obese")

#Fovourite Number
#Below 100- cool
#100-200  -Nice
#300-400 -Excellent
# Better Luck Next Time
