
import sys


class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.orders = []

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def add_funds(self):
        amount = float(input("Enter the amount to add to your balance: "))
        self.balance += amount
        print(f"Added ${amount} to your balance. New balance: ${self.balance}")

    def place_order(self, menu):
        print("\n--- Menu ---")
        for item, price in menu.items():
            print(f"{item}: ${price}")
        print("------------------")
        order = input(
            "Enter the items you want to order (comma-separated): ").split(",")
        order = [item.strip() for item in order]

        total_cost = 0
        matched_order = []

        for item in order:
            if item in menu:
                matched_order.append(item)
                total_cost += menu[item]
            else:
                print(f"Item '{item}' does not exist in the menu.")

        if total_cost > self.balance:
            print(
                f"Insufficient balance! Your balance: ${self.balance}, Order cost: ${total_cost}")
        elif total_cost == 0:
            print("No valid items selected for the order.")
        else:
            self.balance -= total_cost
            self.orders.append((matched_order, total_cost))
            print(f"Order placed successfully! Total cost: ${total_cost}")

    def view_orders(self):
        print("\n--- Past Orders ---")
        if not self.orders:
            print("No orders yet.")
        else:
            for idx, (order, total_cost) in enumerate(self.orders, start=1):
                print(
                    f"Order {idx}: {', '.join(order)} - Total: ${total_cost}")
        print("-------------------")


class Admin:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def add_customer(self):
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        address = input("Enter customer address: ")
        customer = Customer(name, email, address)
        self.restaurant.add_customer(customer)
        print(f"Customer {name} added successfully.")

    def view_customers(self):
        print("\n--- Registered Customers ---")
        if not self.restaurant.customers:
            print("No customers registered yet.")
        else:
            for idx, customer in enumerate(self.restaurant.customers, start=1):
                print(f"{idx}. {customer.name} ({customer.email})")
        print("----------------------------")

    def remove_customer(self):
        self.view_customers()
        try:
            idx = int(input("Enter the customer number to remove: ")) - 1
            customer = self.restaurant.customers[idx]
            self.restaurant.remove_customer(customer)
            print(f"Customer {customer.name} removed successfully.")
        except (IndexError, ValueError):
            print("Invalid input. Please try again.")

    def manage_menu(self):
        while True:
            print("\n--- Manage Menu ---")
            print("1. Add/Update Item")
            print("2. Remove Item")
            print("3. View Menu")
            print("4. Back to Admin Menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                item = input("Enter item name: ")
                price = float(input("Enter item price: "))
                self.restaurant.manage_menu(item, price)
            elif choice == "2":
                item = input("Enter item name to remove: ")
                self.restaurant.manage_menu(item)
            elif choice == "3":
                self.restaurant.view_menu()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def view_all_orders(self):
        print("\n--- All Orders ---")
        if not self.restaurant.customers:
            print("No orders have been placed yet.")
        else:
            for customer in self.restaurant.customers:
                total_spent = sum(total_cost for _,
                                  total_cost in customer.orders)
                if total_spent > 0:
                    print(
                        f"{customer.email} {customer.name} - Total spent: ${total_spent}")
        print("-------------------")


class Restaurant:
    def __init__(self):
        self.menu = {}
        self.customers = []

    def manage_menu(self, item, price=None):
        if price is None:
            if item in self.menu:
                del self.menu[item]
                print(f"Item '{item}' removed from menu.")
            else:
                print(f"Item '{item}' not found in menu.")
        else:
            self.menu[item] = price
            print(f"Item '{item}' added/updated with price ${price}.")

    def view_menu(self):
        print("\n--- Restaurant Menu ---")
        if not self.menu:
            print("No items in the menu.")
        else:
            for item, price in self.menu.items():
                print(f"{item}: ${price}")
        print("------------------------")

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        self.customers.remove(customer)


def main_menu():
    restaurant = Restaurant()
    admin = Admin(restaurant)
    customer = None

    while True:
        print("\n--- Restaurant Management System ---")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Admin Login with credential check
            username = input("Enter Admin Username: ")
            if username == "Admin":
                print("Admin login successful!")
                while True:
                    print("\n--- Admin Menu ---")
                    print("1. Manage Menu")
                    print("2. Add Customer Account")
                    print("3. View Customers")
                    print("4. Remove Customer Account")
                    print("5. View All Orders")
                    print("6. Logout")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        admin.manage_menu()
                    elif admin_choice == "2":
                        admin.add_customer()
                    elif admin_choice == "3":
                        admin.view_customers()
                    elif admin_choice == "4":
                        admin.remove_customer()
                    elif admin_choice == "5":
                        admin.view_all_orders()
                    elif admin_choice == "6":
                        print("Logging out of Admin account...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid credentials. Access denied!")

        elif choice == "2":
            if not restaurant.customers:
                print("No customers registered. Please contact the admin.")
                continue

            username = input("\nEnter your username: ")
            email = input("Enter your email: ")

            customer = next(
                (c for c in restaurant.customers if c.name == username and c.email == email), None)

            if not customer:
                print("Invalid credentials. Login failed!")
                continue

            print(f"\nWelcome, {customer.name}!")
            while True:
                print(f"\n--- Welcome {customer.name} ---")
                print("1. View Menu")
                print("2. Place Order")
                print("3. Check Balance")
                print("4. Add Funds")
                print("5. View Past Orders")
                print("6. Logout")
                cust_choice = input("Enter your choice: ")

                if cust_choice == "1":
                    restaurant.view_menu()
                elif cust_choice == "2":
                    customer.place_order(restaurant.menu)
                elif cust_choice == "3":
                    customer.check_balance()
                elif cust_choice == "4":
                    customer.add_funds()
                elif cust_choice == "5":
                    customer.view_orders()
                elif cust_choice == "6":
                    print("Logging out of Customer account...")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Exiting the system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
