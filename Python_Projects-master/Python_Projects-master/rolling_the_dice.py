import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes":
    print("Rolling the dices... wait a second...")
    print("The values are......")
    print(random.randint(min,max))
    print(random.randint(min,max))

    roll_again=  input("Roll the dices again ? : ")