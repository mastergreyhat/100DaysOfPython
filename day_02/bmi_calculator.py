#BMI calculator
weight = float(input("Enter your weight (in Kilograms): "))
height = float(input("Enter your height (in metres): "))
bmi = weight/height**2

# print(type(bmi)) -> gives type as float

''' follows PEMDAS -> (Paranthesis, exponent, multiplication, division, addition, subtraction)
    with division and multiplication having equal priority, hence evaluated from left to right '''

print(f"Your BMI: {round(bmi, 2)}")

''' here 
        round(value)          : strips off the decimal values, and 
        round(value, number)  : keeps the number of decimal places we pass '''

# if bmi < 18.5:
#     print("You are underweight")
# elif bmi >= 18.5 and bmi < 24.9:
#     print("You are normal weight")
# elif bmi >= 24.9 and bmi < 29.9:
#     print("You are overweight")
# elif bmi >= 29.9 and bmi < 34.9:
#     print("You are obese")
# elif bmi >= 34.9:
#     print("You are extremely obese")

#modified the above code in an efficient and concise way
if bmi < 18.5:
    print("You are underweight")
elif bmi < 24.9:
    print("You are normal weight")
elif bmi < 29.9:
    print("You are overweight")
elif bmi < 34.9:
    print("You are obese")
else:
    print("You are extremely obese")