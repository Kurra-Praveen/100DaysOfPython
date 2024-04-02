list1=["#","#","#"]
list2=["#","#","#"]
list3=["#","#","#"]
finalList=[list1,list2,list3]
print(f"{list1}\n{list2}\n{list3}")
position=input("Please enter the position you want to change :")
column=int(position[0])
row=int(position[1])
finalList[row - 1][column - 1]= "x"
print(f"{list1}\n{list2}\n{list3}")