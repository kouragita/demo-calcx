#bot name chunkz
#chunkz @ yur service
#chunkz is in a competition with Bee, tag him for more
# Define menu items and their prices
menu = {
    "coffee": 5,
    "burger": 10,
    "sandwich": 7,
    "cappuccino": 6,
    "sausage": 8,
}

# Initialize the total cost
total = 0

# Welcome the customer
name = input('What is your name?\n')
print('Hi, ' + name + ', I am CHUNKZ, and welcome to Coffers Cafe.')
print('Here is our menu:')

# Display the menu
for item, price in menu.items():
    print(f'{item.capitalize()}: ${price}')

# Ask for orders
while True:
    order = input('What would you like to order from the menu (or type "done" to finish)?\n').lower()

    if order == "done":
        break

    if order not in menu:
        print("Sorry, we don't have that item on our menu.")
        continue

    quantity = int(input(f"How many {order}s would you like?\n"))
    total += menu[order] * quantity

# Display the total cost
print(f"Thank you, {name}! Your total is: ${total}")
print(f"Have a blast, {name}, and enjoy your meal!")
print('CHUNKZ is in a competition with Bee, tag him for more... AND whom yu love. drop a rating.🔥🔥')