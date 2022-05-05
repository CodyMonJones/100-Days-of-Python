# print("Welcome to the tip calculator")
# bill = int(input("How much was the bill?\n"))
# num_of_people = int(input("How many people ate dinner?\n"))
# tip_percent = float(input("How much would you like to tip 10, 15 or 20 percent\n"))
# bill_with_tip = bill + (bill * tip_percent)
# total_per_person = (bill_with_tip / num_of_people)

# print(f'Each person will pay: {total_per_person}')

current_age = int(input("How old are you\n"))
years_left = 70 - current_age
weeks_left = years_left * 52
days_left = years_left * 365
months_left = years_left * 12

print(f"you have {years_left} years left, {months_left} months left, {weeks_left} weeks left, {days_left} days left")