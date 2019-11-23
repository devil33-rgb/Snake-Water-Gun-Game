import random
list = ["s","w","g"]

chance=10
no_of_chance=0
humanpoint=0
pcpoint=0

print("this is snake water gun game")

while no_of_chance < chance:
 choice = random.choice(list)
 no_of_chance+=1

 take=input("s for snake \n"
           "w for water \n"
           "g for gun\n")
 if take==choice:
    print("tie")

 if take =="s" and choice =="g":
    pcpoint+=1
    print(f"{take} guess and {choice} guess")
    print("computer wins 1 points")
    print(f"{pcpoint} compuet point and {humanpoint} ypour point")
    print(chance-no_of_chance,"left \n")

 elif take=="g" and choice =="w":
   pcpoint+=1
   print(f"{take} guess and {choice} guess")
   print("computer wins 1 points")
   print(f"{pcpoint} computer point and {humanpoint} your point")
   print(chance - no_of_chance, "left \n")

 elif take=="g" and choice =="s":
   humanpoint+=1
   print(f"{take} guess and {choice} guess")
   print("human wins 1 points")
   print(f"{pcpoint} computer point and {humanpoint} your point")
   print(chance - no_of_chance, "left \n")

 elif take=="w" and choice=="s":
     pcpoint+=1
     print(f"{take} guess and {choice} guess")
     print("computer wins 1 points")
     print(f"{pcpoint} computer point and {humanpoint} your point")
     print(chance - no_of_chance, "left \n")

 elif take =="w" and choice =="g":
     humanpoint += 1
     print(f"{take} guess and {choice} guess")
     print("human wins 1 points")
     print(f"{pcpoint} computer point and {humanpoint} your point")
     print(chance - no_of_chance, "left \n")

 elif take =="g" and choice =="w":
     pcpoint += 1
     print(f"{take} guess and {choice} guess")
     print("computer wins 1 points")
     print(f"{pcpoint} computer point and {humanpoint} your point")
     print(chance - no_of_chance, "left \n")

 elif take =="g" and choice =="s":
     humanpoint += 1
     print(f"{take} guess and {choice} guess")
     print("human wins 1 points")
     print(f"{pcpoint} computer point and {humanpoint} your point")
     print(chance - no_of_chance, "left \n")





print("game over")


print(f"human point is {humanpoint} and pc point is {pcpoint}")

if humanpoint<pcpoint:
    print("pc wins")

elif pcpoint<humanpoint:
    print("human wins")

else :
    print('tie')

