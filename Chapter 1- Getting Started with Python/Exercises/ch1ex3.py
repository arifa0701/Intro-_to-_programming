##NEW PROJECT
#import datetime
#now = datetime.datetime.now()
#print ("current date and time:")
#print (now.strftime("%d-%m-%y"))
#print(now.strftime("%H:%M:%S"))
class Item:
    def _init_(self, name, category, price, stock):
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def is_available(self):
        return self.stock > 0

    def dispense(self):
        if self.is_available():
            self.stock -= 1
            return True
        return False


class VendingMachine:
    def _init_(self):
        self.items = {}
        self.balance = 0.0

    def add_item(self, code, item):
        self.items[code] = item

    def display_menu(self):
        print("\n--- Vending Machine Menu ---")
        categories = {}
        for code, item in self.items.items():
            if item.category not in categories:
                categories[item.category] = []
            categories[item.category].append((code, item))

        for category, items in categories.items():
            print(f"\n{category}:")
            for code, item in items:
                status = "(Out of stock)" if not item.is_available() else ""
                print(f"  {code}: {item.name} - $ {item.price:.2f} {status}")

    def insert_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You inserted $ {amount:.2f}. Current balance: $ {self.balance:.2f}")
        else:
            print("Please insert a valid amount.")

    def purchase_item(self, code):
        if code not in self.items:
            print("Invalid selection. Please try again.")
            return

        item = self.items[code]
        if not item.is_available():
            print(f"Sorry, {item.name} is out of stock.")
            return

        while self.balance < item.price:
            print(f"Insufficient balance. {item.name} costs $ {item.price:.2f}, but you have $ {self.balance:.2f}.")
            try:
                additional_amount = float(input("Enter additional amount or 0 to cancel: $ "))
                if additional_amount == 0:
                    print("Transaction canceled.")
                    return
                elif additional_amount > 0:
                    self.balance += additional_amount
                    print(f"New balance: $ {self.balance:.2f}")
                else:
                    print("Invalid amount. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if item.dispense():
            self.balance -= item.price
            print(f"Dispensing {item.name}. Enjoy your snack!")
            print(f"Remaining balance: $ {self.balance:.2f}")
            print("Thank you for using the vending machine. Goodbye!")
            exit()  # Exit the program after dispensing the item
        else:
            print(f"Failed to dispense {item.name}. Please try again.")

    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: $ {self.balance:.2f}")
            self.balance = 0.0
        else:
            print("No balance to return.")


# Initialize Vending Machine
vending_machine = VendingMachine()

# Add items to the vending machine
vending_machine.add_item("A1", Item("Coca-Cola", "Drinks", 1.50, 10))
vending_machine.add_item("A2", Item("Pepsi", "Drinks", 1.50, 8))
vending_machine.add_item("B1", Item("Chips", "Snacks", 1.00, 5))
vending_machine.add_item("B2", Item("Chocolate Bar", "Snacks", 1.25, 2))
vending_machine.add_item("C1", Item("Coffee", "Hot Drinks", 2.00, 6))
vending_machine.add_item("C2", Item("Tea", "Hot Drinks", 1.75, 4))

# Simulate Vending Machine
while True:
    vending_machine.display_menu()
    print("\nOptions: ")
    print(" 1. Insert money")
    print(" 2. Purchase item")
    print(" 3. Return change")
    print(" 4. Exit")

    choice = input("Please select an option: ")

    if choice == "1":
        try:
            amount = float(input("Enter the amount to insert: $ "))
            vending_machine.insert_money(amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif choice == "2":
        code = input("Enter the code of the item you wish to purchase: ")
        vending_machine.purchase_item(code)

    elif choice == "3":
        vending_machine.return_change()

    elif choice == "4":
        print("Thank you for using the vending machine. Goodbye!")
        vending_machine.return_change()
        break

    else:
        print("Invalid option. Please try again.")