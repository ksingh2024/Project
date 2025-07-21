# -----------------------------------------------------------------
# Assignment Name:      Rental Skis and Snowboards
# Name:                 Kultegh Singh
# -----------------------------------------------------------------
from datetime import datetime

# ------------------------------------------------------------------
# CustomerClass
# ------------------------------------------------------------------
class Customer:
    # ####################################################################
    # Name: __init__
    # Abstract: Initializes a new Customer with basic info and rental data
    # ####################################################################
    def __init__(self, first_name, last_name, id_number, phone_number, coupon_code, rental_period):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.phone_number = phone_number
        self.coupon_code = coupon_code
        self.rental_period = rental_period
        self.rented_skis = 0
        self.rented_snowboards = 0
        self.rental_time = None
        self.return_time = None

    # ####################################################################
    # Name: RentItems
    # Abstract: Rents skis and snowboards to the customer
    # ####################################################################
    def RentItems(self, skis, snowboards):
        self.rented_skis = skis
        self.rented_snowboards = snowboards
        self.rental_time = datetime.now()
        return True

    # ####################################################################
    # Name: ReturnItems
    # Abstract: Returns all rented items and resets rental counts
    # ####################################################################
    def ReturnItems(self):
        self.return_time = datetime.now()
        skis = self.rented_skis
        snowboards = self.rented_snowboards
        self.rented_skis = 0
        self.rented_snowboards = 0
        return skis, snowboards

    # ####################################################################
    # Name: __str__
    # Abstract: Returns string representation of the customer
    # ####################################################################
    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.id_number})"


# ------------------------------------------------------------------
# ShopClass
# ------------------------------------------------------------------
class RentalShop:
    # ####################################################################
    # Name: __init__
    # Abstract: Initializes inventory and tracking counters
    # ####################################################################
    def __init__(self, total_skis, total_snowboards):
        self.total_skis = int(total_skis)
        self.total_snowboards = int(total_snowboards)
        self.available_skis = self.total_skis
        self.available_snowboards = self.total_snowboards
        self.daily_revenue = 0
        self.daily_skis_rented = 0
        self.daily_snowboards_rented = 0

    def GetAvailableSkis(self):
        return self.available_skis

    def GetAvailableSnowboards(self):
        return self.available_snowboards

    def GetDailyRevenue(self):
        return self.daily_revenue

    def GetDailySkisRented(self):
        return self.daily_skis_rented

    def GetDailySnowboardsRented(self):
        return self.daily_snowboards_rented

    # ####################################################################
    # Name: CalculateEstimate
    # Abstract: Calculates rental cost with optional discount
    # ####################################################################
    def CalculateEstimate(self, rental_period, skis, snowboards, time, coupon_code):
        base = 0
        if rental_period.lower() == "hourly":
            base = skis * 15 + snowboards * 10
        elif rental_period.lower() == "daily":
            base = skis * 50 + snowboards * 40
        elif rental_period.lower() == "weekly":
            base = skis * 200 + snowboards * 160
        total = base * time
        if coupon_code.endswith("BBP"):
            total *= 0.9  # 10% discount
        return round(total, 2)


# ------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------

# ####################################################################
# Name: SetUp_ShopInventory
# Abstract: Displays opening inventory of the shop
# ####################################################################
def SetUp_ShopInventory(shop):
    print("\nBob's Skis and Snowboards Shop is now open.")
    print("There are", shop.GetAvailableSkis(), "skis and", shop.GetAvailableSnowboards(), "snowboards in the inventory.")


# ####################################################################
# Name: Menu
# Abstract: Displays navigation menu and gets user input
# ####################################################################
def Menu():
    while True:
        try:
            print("\nMenu:")
            print("1. New Customer Rental")
            print("2. Return Rental")
            print("3. Display Inventory")
            print("4. Close Shop")
            choice = int(input("Enter choice: "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Please enter a number from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# ####################################################################
# Name: NewCustomerRental
# Abstract: Collects customer info and processes new rental
# ####################################################################
def NewCustomerRental(shop, customers):
    print("\nEnter Customer Rental Details")
    first = input("First Name: ")
    last = input("Last Name: ")
    id_num = input("ID Number: ")
    phone = input("Phone Number: ")
    coupon = input("Coupon Code: ")
    period = input("Rental Period (Hourly, Daily, Weekly): ")
    time = int(input("Rental Time: "))
    skis = int(input("Number of Skis: "))
    snowboards = int(input("Number of Snowboards: "))

    customer = Customer(first, last, id_num, phone, coupon, period)
    customers.append(customer)

    estimate = shop.CalculateEstimate(period, skis, snowboards, time, coupon)
    print("Rental Price Estimate: $", estimate)

    confirm = input("Start Rental? Y/N: ").upper()
    if confirm == "Y":
        if shop.GetAvailableSkis() >= skis and shop.GetAvailableSnowboards() >= snowboards:
            customer.RentItems(skis, snowboards)
            shop.available_skis -= skis
            shop.available_snowboards -= snowboards
            shop.daily_skis_rented += skis
            shop.daily_snowboards_rented += snowboards
            shop.daily_revenue += estimate
            print("Rental started at:", customer.rental_time.strftime("%m/%d/%Y %H:%M"))
        else:
            print("Not enough equipment available.")
    else:
        print("Rental cancelled.")


# ####################################################################
# Name: ReturnRental
# Abstract: Returns items from customer and updates inventory
# ####################################################################
def ReturnRental(shop, customers):
    print("\nReturn Rental")
    id_lookup = input("Enter Customer ID: ")
    found = False

    for customer in customers:
        if customer.id_number == id_lookup:
            found = True
            skis, snowboards = customer.ReturnItems()
            shop.available_skis += skis
            shop.available_snowboards += snowboards
            print(f"Returned {skis} skis and {snowboards} snowboards.")
            print("Return Time:", customer.return_time.strftime("%m/%d/%Y %H:%M"))
            break

    if not found:
        print("Customer not found.")


# ####################################################################
# Name: DisplayInventory
# Abstract: Shows current availability of skis and snowboards
# ####################################################################
def DisplayInventory(shop):
    print("\nCurrent Inventory:")
    print("Skis Available:", shop.GetAvailableSkis())
    print("Snowboards Available:", shop.GetAvailableSnowboards())


# ####################################################################
# Name: CloseShop
# Abstract: Summarizes daily rental statistics and closes the shop
# ####################################################################
def CloseShop(shop):
    print("\nShop Closing Summary")
    print("Total Revenue: $", shop.GetDailyRevenue())
    print("Total Skis Rented:", shop.GetDailySkisRented())
    print("Total Snowboards Rented:", shop.GetDailySnowboardsRented())
    print("Shop is now closed.")


# ####################################################################
# Name: main
# Abstract: Controls program execution flow
# ####################################################################
def main():
    skis = int(input("Enter number of skis in inventory: "))
    boards = int(input("Enter number of snowboards in inventory: "))
    shop = RentalShop(skis, boards)
    customers = []

    SetUp_ShopInventory(shop)

    while True:
        action = Menu()
        if action == 1:
            NewCustomerRental(shop, customers)
        elif action == 2:
            ReturnRental(shop, customers)
        elif action == 3:
            DisplayInventory(shop)
        elif action == 4:
            CloseShop(shop)
            break

if __name__ == "__main__":
    main()
