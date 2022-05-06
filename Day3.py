print('''
********************
    ___
    ).x)
   (:_(
 
********************''')

print("Welcome to treasure island.\nYour mission is to find the treasure!")
print("You're at a crossroad. Where do you want to go? type 'left' or 'right'")
choice_1 = input().lower()

if choice_1 == "left":
    print("You have come across an ocean. Would you like to 'swim' or 'wait'")
    choice_2 = input().lower()
    if choice_2 == "swim":
        print("Congratulations you have made it to an island. There is a lone pirate standing in front of you. Will you take the 'blue' pill or the 'red' pill")
        choice_3 = input().lower()
        if choice_3 == 'blue':
            print("You have discovered treasure of your wildest dreams! Congratulations you WIN!!")
        else:
            print("You have been banished from Treasure Island never to return again")    
    else:    
        print("You have been attacked by the island natives! Game Over...")

else:
    print("You fell into a hole! Game Over...")    