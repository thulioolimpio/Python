child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal?" ))
#I included the variable 'juice' to fulfill the exceeding requirements.
juice_for_child = float(input("What is the price of a child's juice? "))
juice_for_adult = float(input("What is the price of an adult's juice? " ))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

subtotal = (child_meal * number_of_children * juice_for_child) + (adult_meal * number_of_adults * juice_for_adult)
str(subtotal)
print(f"Subtotal: ${subtotal:.2f}")

sales_tax_rate = float(input("What is the sales tax rate? "))
sale_tax = (sales_tax_rate * subtotal) / 100
print(f"Sales Tax: ${sale_tax:.2f}")

total = subtotal + sale_tax
print(f"Total: ${total:.2f}")

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
print(f"Change: ${change:.2f}")