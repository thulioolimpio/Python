first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

if first_number > second_number :
    print("The first number is greater ")
else:
    print("The first number is not greater ")

if second_number > first_number :
    print("The second number is greater")
else:
    print("The second number is not greater")
    
if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

animal = input("What is your facorite animal? ")

if animal.capitalize() == "Cachorro" :
    print("That's my favorite animal too! ")
else:
    print("That one is not my favorite.")