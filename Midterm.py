# MId Term Exam
# Emily Smith

print("Welcome to Burgers to Go!")

# Set base prices and tax rate
BURGER_PRICE = 10.30
DRINK_PRICE = 1.99
TAX_RATE = 0.085

# Define available toppings and each of their prices
toppings_menu = {
    "cheese": 1.00,
    "lettuce": 0.50,
    "tomato": 0.50,
    "pickles": 0.50,
    "onions": 0.50,
    "bacon": 1.50,
    "jalapenos": 0.75,
    "mushrooms": 0.75
}


# Display the list of available toppings with prices
def show_toppings():
    print("Available toppings:")
    for topping, price in toppings_menu.items():
        print("- " + topping + " $" + "{:.2f}".format(price))


# Calculates total cost of a burger, including toppings and optional drink
def calculate_burger_total(selected_toppings, has_drink):
    total = BURGER_PRICE
    for topping in selected_toppings:
        total += toppings_menu[topping]
    if has_drink:
        total += DRINK_PRICE
    return total


# Prints a detailed receipt showing each burger, toppings, drinks, and totals
def print_receipt(all_burgers):
    total_order_price = 0
    print("\n--- RECEIPT ---")

    for burger in all_burgers:
        print("\n" + burger["name"] + " $" + "{:.2f}".format(BURGER_PRICE))

        if burger["toppings"]:
            for topping in burger["toppings"]:
                print("- " + topping + " $" + "{:.2f}".format(toppings_menu[topping]))
        else:
            print("- no toppings    $0.00")

        if burger["drink"]:
            print("- drink  $" + "{:.2f}".format(DRINK_PRICE))

        burger_total = calculate_burger_total(burger["toppings"], burger["drink"])
        print("subtotal  $" + "{:.2f}".format(burger_total))
        total_order_price += burger_total

    tax = total_order_price * TAX_RATE
    final_total = total_order_price + tax

    print("\n------------------------")
    print("Subtotal          $" + "{:.2f}".format(total_order_price))
    print("Tax               $" + "{:.2f}".format(tax))
    print("TOTAL             $" + "{:.2f}".format(final_total))


# Creates a list to store all burger orders
all_burgers = []

# Prompt the user for the number of burgers they want to order
num = input("\nHow many burgers would you like to order? ")
num_burgers = int(num)

# Loop through each burger to collect customizations
for i in range(1, num_burgers + 1):
    print("\nMaking Burger #" + str(i))
    show_toppings()

    toppings_chosen = []

# Prompts user to add toppings until they say 'no'
    while True:
        add = input("Do you want to add a topping? (yes/no): ").strip().lower()
        if add == "yes":
            topping = input("Enter a topping: ").strip().lower()
            if topping in toppings_menu:
                toppings_chosen.append(topping)
                print(topping + " added.")
            else:
                print("That topping is not on the menu.")
                show_toppings()
        elif add == "no":
            break
        else:
            print("Please type 'yes' or 'no'.")

    # Asks if the user wants to add a drink
    drink_input = input("Would you like a drink for $1.99? (yes/no): ").lower()
    wants_drink = True if drink_input == "yes" else False

# Stores the current burger's details in a dictionary
    burger_info = {
        "name": "Hamburger " + str(i),
        "toppings": toppings_chosen,
        "drink": wants_drink
    }
# Add this burger to the full order list
    all_burgers.append(burger_info)

# Print final receipt with itemized details for each burger
print_receipt(all_burgers)
