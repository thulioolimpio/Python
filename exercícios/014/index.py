# Initialize empty lists to store items and prices
items = []
prices = []

# Function to add a new item to the shopping cart
def add_item():
    item_name = input("What item would you like to add? ")
    item_price = float(input(f"What is the price of '{item_name}'? $"))
    items.append(item_name)
    prices.append(item_price)
    print(f"'{item_name}' has been added to the cart.")

# Function to display the contents of the shopping cart
def display_cart():
    print("The contents of the shopping cart are:")
    for i, (item, price) in enumerate(zip(items, prices), start=1):
        print(f"{i}. {item} - ${price:.2f}")

# Function to remove an item from the shopping cart
def remove_item():
    if not items:
        print("The shopping cart is empty.")
        return
    
    display_cart()
    item_number = int(input("Which item would you like to remove? ")) - 1
    if 0 <= item_number < len(items):
        removed_item = items.pop(item_number)
        removed_price = prices.pop(item_number)
        print(f"'{removed_item}' has been removed from the cart.")
    else:
        print("Sorry, that is not a valid item number.")

# Function to compute the total price of items in the shopping cart
def compute_total():
    total = sum(prices)
    print(f"The total price of the items in the shopping cart is ${total:.2f}")

# Main function to run the program
def main():
    print("Welcome to the Shopping Cart Program!\n")
    while True:
        print("Please select one of the following: ")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        choice = input("Please enter an action: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            display_cart()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            compute_total()
        elif choice == '5':
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main function
if __name__ == "__main__":
    main()