height = int(input("Enter your height in cm: "))
bill = 0
if height >=120:
    print("You can ride the rollercoaster !")
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Child tickets are $5")
        bill = 5
    elif age <=18:
        print("Youth tickets are $7")
        bill = 7
    else:
        print("Adult tickets are $12")
        bill = 12
    
    want_photo = input("Do you want to take a photo with an added cost of $3 ? type y for yes and n for no: ")
    if want_photo == 'y':
        bill += 3  #can also be written as 'bill = bill + 3'
        print(f"Your bill amount is: ${bill}")
    else:  #here any input other than 'y' will execute below else statement
        print(f"Your bill amount is: ${bill}")
else:
    print("You cannot ride the rollercoaster")