# number = int(input("Enter a number to check if Even or Odd: "))

# if number % 2 == 0:
#     print(f"Your number {number} is Even")
# else:
#     print(f"Your number {number} is Odd")    

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese")
else:
    print("clinically obese")              