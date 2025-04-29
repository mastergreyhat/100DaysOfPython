print("Welcome to the tip calculator!")
total_bill = float(input("Enter the total bill amount: $"))
tip = int(input("what percentage of tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

''' tip_amount = total_bill * tip / 100
    total_with_tip = total_bill + tip_amount
    per_head = total_with_tip / people '''

#combining above 3 steps into a single line
per_head = (total_bill * (tip/100) + total_bill)/people

print(f"Each person should pay: ${round(per_head, 2)}")