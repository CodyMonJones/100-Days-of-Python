# number = int(input("Enter a number to check if Even or Odd: "))

# if number % 2 == 0:
#     print(f"Your number {number} is Even")
# else:
#     print(f"Your number {number} is Odd")    

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))

# bmi = round(weight / height ** 2)

# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal weight")
# elif bmi < 30:
#     print("Overweight")
# elif bmi < 35:
#     print("Obese")
# else:
#     print("clinically obese")       
# 
year_input = int(input("Enter year you would like to check: "))

if year_input % 4 == 0:
    if year_input % 100 == 0:
        if year_input % 400 == 0:
            print(f"The year {year_input} is a leap year!")
        else:
            print(f"The year {year_input} is not a leap year!")    
    else:
        print(f"The year {year_input} is not a leap year!")        
else:
    print(f"The year {year_input} is not a leap year!")