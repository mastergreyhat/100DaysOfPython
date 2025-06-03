while True:
    try:
        age = int(input("Enter your age: "))
        if type(age) == int:
            break
    except ValueError:
        print("Enter a number please..")

if age >= 18:
    print("You can drive!")
else:
    print("You can't drive!")