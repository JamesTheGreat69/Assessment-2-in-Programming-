import time # this will allow my program to pause fo a bit to make a realistic vending machine process 
import pyttsx3 #this will allow my program to speak 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
print("\nWelcome to James Vending Machine!") # This will show to the screen and the\n will add a space
speak("Welcome to James Vending Machine!")
time.sleep(1) # this will delay the the program for 1 second to add an effect 

# this is dictionary for my items 
menu = {
    "A1": {"name": "Water", "price": 1.00, "stock": 10},
    "A2": {"name": "Coca Cola", "price": 2.40, "stock": 8},
    "A3": {"name": "Fanta", "price": 2.36, "stock": 5},
    "B1": {"name": "Kitkat", "price": 1.95, "stock": 6},
    "B2": {"name": "Lays Chips", "price": 7.49, "stock": 4},
    "B3": {"name": "Gatorade", "price": 8.00, "stock": 7},
    "C1": {"name": "Red Bull", "price": 3.00, "stock": 5},
    "C2": {"name": "Pandesal", "price": 1.70, "stock": 10},
    "C3": {"name": "Doritos", "price": 8.95, "stock": 3}
}

def show_menu(): # this is def function and it will displays all my items on the output
    print("\n====================== MENU ========================") # this is my header and ==== is for my design 
    for code, item in menu.items(): # this is a loop for each item in my dictionary
        print(f"{code}: {item['name']} - ${item['price']} (Stock: {item['stock']})") # this will be displayed for my cose, name, price and how many stock I have in my vending machine
    print("===================================================") # this is the footer line and ===== is for my design 

def pay(total): # this is a function name pay and total is my parameter
    while True: # this will work if the payment is successful 
        method = input("Do you want to pay by Card or Cash? ").strip().lower() #this is for asking for payment method I used .strip() to remove extra spaces and .lowe() to make the input lowercase
        if method == "card": # this will check if the user input card payment
            print(f"Processing card payment of ${total:.2f}...") # this will be displayed the amount of the total
            time.sleep(1) # this will add an effect and delay 1 second 
            print("Payment successful!") # this will confirming the payment and will exit the function
            return True
        elif method == "cash":#this will check if the user is paying by cash 
            while True: # this will be checking if the user inserted the cash 
                try:
                    cash = float(input(f"Insert cash (total ${total:.2f}): ")) # this will ask the user to input the payment and it will convert input to decimal
                    if cash < total: # this will check if the cash is insufficient 
                        print(f"Not enough. You need ${total - cash:.2f} more.") # this will be displayed to tell the user the reamining balance he needed
                    else: # this will run i the cash is enough
                        change = cash - total # this will calculate how much is the change
                        print("Payment successful!") # this will be shown if the payment is confirmed
                        if change > 0: # this will be show if change exists
                            print(f"Here is your change: ${change:.2f}") # this will be displayed if you have a chnage
                        return True # this will be the end of payment process successfully
                except ValueError: # this will be show if the input of the user is wrong 
                    print("Please enter a valid number.") # this will displayed 
        else:
            print("Invalid choice. Please type 'Card' or 'Cash'.") # this will run if the user input a something else

def order(): # this will define a order function
    cart = [] # this is to store a selected item
    total = 0 # this will track the total cost 

    show_menu() # this is display menu
    while True: # this will allow a multiple item to select
        code = input("Select an item code like (A1) or type 'Done' to cancel: ").strip().capitalize() # this to get the item code I used .capitalize() and .strip() to remove space
        if code == "Done": # if the user input done then it will exit the item selection
            break
        if code not in menu: # this will check if the user input code is exists.
            print("Invalid code. Please select a correct code.") # this will be displayed an error and it will restart the loop
            continue
        if menu[code]["stock"] <= 0: # this will check if the item stock is out of stock 
            print("Sorry, the item you selected is out of stock.") #this will be displayed
            continue

        quantity = input(f"How many {menu[code]['name']} would you like? ") # this will ask how many item you want to purchase
        if not quantity.isdigit() or int(quantity) <= 0: # it will validates the quantity input
            print("Enter a valid number.") # this will be displayed 
            continue
        quantity = int(quantity) # this will convert the quantity to ineteger
        if quantity > menu[code]["stock"]: # this will prevents a buying more than a available
            quantity = menu[code]["stock"] 
            print(f"Only {quantity} available. Quantity adjusted.") # this will be displayed

        cart.append({     # this will add an item details to the cart 
            "code": code,
            "name": menu[code]["name"],
            "price": menu[code]["price"],
            "quantity": quantity
        })
        total += menu[code]["price"] * quantity # this will update the total cost 
        print(f"Added {quantity} x {menu[code]['name']} - Current total: ${total:.2f}") # this will be displayed 

       
        more = input("Do you want to add more items? (yes/no): ").strip().lower() #this will be asking the user if he/she wants to add more items
        if more != "yes": # if the answer is not yes then it will stop adding items
            break 

    if not cart: #this will check if the cart is empty 
        print("No items selected.") # this will be displayed 
        return

    print(f"\nTotal to pay: ${total:.2f}") #this will be displayed the total amount
    if pay(total): # this will call the payment function
        print("\n--- Receipt ---") # this will be displayed for receipt 
        for item in cart: # this will loop through the purchased items that the user bought
            print(f"{item['quantity']} x {item['name']} - ${item['price']*item['quantity']:.2f}")#this will print the receipt
            menu[item['code']]["stock"] -= item["quantity"] #it will deduct the puchased items from stocks
        print("Payment completed.") # this will be displayed after the processed is being done 
        print("Thank you for shopping!\n") # and this will be shown as well to appreciate the user for buying in my vending machine 

    cont = input("Would you like to buy more? (yes/no): ").strip().lower() #this will ask the user if he/she wants to buy more
    if cont == "yes": # and the user input yes then the order process will restarts
        order() 
    else: #this will run if the user input no 
        print("Thank you for purchasing in James Vending Machine and have a nice day ahead!") # and this will be displayed on the screen 



order() # this will be the start of my vending my machine 






