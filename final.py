
from tabulate import tabulate
import qrcode
import time
import subprocess

data = 'https://media.tenor.com/a3CVBpfzIPAAAAAd/phir-hera-pheri-ye-kaafi-difficult-course-hai.gif'
img = qrcode.make(data)
img.save('MyQRCode1.jpg')

menu = {
    "Burgers": {
        "Veg Burger": 199.00,
        "Cheese Veg Burger": 249.00,
        "Chicken Burger": 299.00,
        "Cheese Chicken Burger": 349.00,
    },
    "Pizzas": {
        "Margherita": 299.00,
        "Pepperoni": 349.00,
        "Hawaiian": 349.00,
        "Italian": 349.00,
    },
    "Fries": {
        "Regular Fries": 149.00,
        "Cheese Fries": 179.00,
        "Peri-Peri Fries": 179.00,
        "Cheese Peri-Peri Fries": 199.00,
    },
    "Drinks": {
        "Cola": 99.00,
        "Lemonade": 119.00,
        "Iced Tea": 119.00,
        "Cold Coffee": 129.00,
    },
}


def display_menu():
    print("\n======================= MENU ========================")
    
    menu_table = []
    for category, items in menu.items():
        for item, price in items.items():
            menu_table.append([category, item, "Rs. {:.2f}".format(price)])
    print(tabulate(menu_table, headers=["CATEGORIES", "ITEMS", "PRICE"], tablefmt="grid"))


def generate_bill(order):
    total = 0
    bill_table = []
    print('\n==================== BILL ====================')
    
    bill_table.append(["Item", "Quantity", "Price", "Subtotal"])
    for item, quantity in order.items():
        found = False
        for category, items in menu.items():
            if item in items:
                price = items[item]
                subtotal = price * quantity
                total += subtotal
                bill_table.append([item, quantity, "Rs. {:.2f}".format(price), "Rs. {:.2f}".format(subtotal)])
                found = True
                break
        if not found:
            print(f"Error: '{item}' not found in the menu.")
    bill_table.append(["Total", "", "", "Rs. {:.2f}".format(total)])
    print(tabulate(bill_table, headers="firstrow", tablefmt="grid"))


def main():
    order = {}
    print('''          
              WELCOME TO MEGABYTE CAFE!
                   ''')
    display_menu()
    while True:
        item_input = input("\nEnter the item you want to order (or 'done' to finish): ").lower()
        if item_input == "done":
            break
        item_found = False
        for category, items in menu.items():
            if item_input in [i.lower() for i in items.keys()]:
                item = next((k for k in items if k.lower() == item_input), None)
                quantity = int(input(f"How many {item} do you want to order? "))
                if item in order:
                    order[item] += quantity
                else:
                    order[item] = quantity
                item_found = True
                break
        if not item_found:
            print("Invalid item. Please choose from the menu.")

    generate_bill(order)
    print("\nThank you for ordering!")

main()

while True:
    pchoi = input("Do you wish to pay by cash/UPI? ")
    if pchoi.lower() == 'cash':
        print('Thank you! Visit again.')
        break
    elif pchoi.lower() == 'upi':
        subprocess.run(['start', 'MyQRCode1.jpg'], shell=True)
        rawtsk = subprocess.run(['tasklist'], capture_output=True, text=True)
        rawtsk2 = rawtsk.stdout.split('\n')
        rawtsk3 = rawtsk2[1:]
        for i in rawtsk3:
            if i.startswith('PhotosApp'):
                target = i
        mitotar = target.split()
        pfknid = int(mitotar[1])
        cmmd = 'taskkill /pid ' + str(pfknid) + ' /t /f'
        def countdown(time_sec):
            while time_sec>0:
                mins, secs = divmod(time_sec, 60)
                print('{:02d}:{:02d}'.format(mins, secs),end='\t')
                time.sleep(1)
                time_sec -= 1                
            subprocess.run(cmmd, shell=True)
            print()
        countdown(20)
        print('\n Payment Succesful')
        break
    else:
        print('please choose a valid option.'.upper())
        print('\n')
