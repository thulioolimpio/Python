child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

subtotal = (child_meal * number_of_children) + (adult_meal * number_of_adults)
str(subtotal)
print(f"Subtotal: {subtotal}")