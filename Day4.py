# import random

# names_string = input("Please enter names separated by a comma: ")
# names_list = names_string.split(",");

# random_name = random.randint(0, len(names_list) - 1)
# paying_bill = names_list[random_name]

# print(f"{paying_bill} is paying for the bill")

row1 = ["*", "*", "*"]
row2 = ["*", "*", "*"]
row3 = ["*", "*", "*"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
location = input("Please enter a location: ")

row = int(location[0])
col = int(location[1])

selected_row = map[col - 1]
selected_row[row - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")