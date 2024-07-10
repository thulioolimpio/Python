number = int(input("Please type a positive number: "))

while number < 0:
    print("Sorry, that is a nagative number. Please try again!")
    number = int(input("Please type a positive number: "))
print(f"the number is {number}")