print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
new_name1=name1.lower()
new_name2=name2.lower()
count1=0
count2=0
t=int(new_name1.count("t"))+int((new_name2.count("t")))
r=int(new_name1.count("r"))+int((new_name2.count("r")))
u=int(new_name1.count("u"))+int((new_name2.count("u")))
e=int(new_name1.count("e"))+int((new_name2.count("e")))
count1=t+r+u+e
l=int(new_name1.count("l"))+int((new_name2.count("l")))
o=int(new_name1.count("o"))+int((new_name2.count("o")))
v=int(new_name1.count("v"))+int((new_name2.count("v")))
e=int(new_name1.count("e"))+int((new_name2.count("e")))
count2=l+o+v+e
count3=str(count1)+str(count2)
if 10>int(count3) or int(count3)>90:
    print(f"Your score is {count3}, you go together like coke and mentos.")
elif   40<int(count3)<50:
    print(f"Your score is {count3}, you are alright together.")
else:
    print(f"Your score is {count3}.")

