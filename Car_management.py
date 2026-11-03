
cars = [
    {"id": 101, "brand": "Toyota", "model": "Fortuner", "price": 3500000, "year": 2024, "quantity": 3},
    {"id": 102, "brand": "Hyundai", "model": "Creta", "price": 1500000, "year": 2023, "quantity": 5},
    {"id": 103, "brand": "Tata", "model": "Nexon", "price": 1000000, "year": 2024, "quantity": 4}
]

cart = []


def add_car():
    car_id = int(input("Enter Car ID: "))

    for car in cars:
        if car["id"] == car_id:
            print("Car ID already exists!")
            return

    brand = input("Enter Car Brand: ")
    model = input("Enter Car Model: ")
    price = float(input("Enter Car Price: "))
    year = int(input("Enter Manufacturing Year: "))
    quantity = int(input("Enter Quantity: "))

    if brand == "" or model == "" or price <= 0 or year <= 0 or quantity < 0:
        print("Enter valid car details!")
        return

    car = {
        "id": car_id,
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "quantity": quantity
    }

    cars.append(car)
    print("Car added successfully!")


def display_cars():
    if len(cars) == 0:
        print("Car inventory is empty!")
        return

    print("\n---------------- CAR INVENTORY ----------------")
    print("ID\tBrand\tModel\t\tPrice\t\tYear\tQuantity")

    for car in cars:
        print(
            car["id"], "\t",
            car["brand"], "\t",
            car["model"], "\t\t",
            car["price"], "\t",
            car["year"], "\t",
            car["quantity"]
        )


def search_car():
    car_id = int(input("Enter Car ID to search: "))

    for car in cars:
        if car["id"] == car_id:
            print("\nCar Found!")
            print("ID:", car["id"])
            print("Brand:", car["brand"])
            print("Model:", car["model"])
            print("Price:", car["price"])
            print("Year:", car["year"])
            print("Quantity:", car["quantity"])
            return

    print("Car not found!")


def update_car():
    car_id = int(input("Enter Car ID to update: "))

    for car in cars:
        if car["id"] == car_id:

            print("\n1. Update Price")
            print("2. Update Year")
            print("3. Update Quantity")

            choice = input("Enter your choice: ")

            if choice == "1":
                price = float(input("Enter new price: "))

                if price > 0:
                    car["price"] = price
                    print("Car price updated successfully!")
                else:
                    print("Invalid price!")

            elif choice == "2":
                year = int(input("Enter new manufacturing year: "))

                if year > 0:
                    car["year"] = year
                    print("Car year updated successfully!")
                else:
                    print("Invalid year!")

            elif choice == "3":
                quantity = int(input("Enter new quantity: "))

                if quantity >= 0:
                    car["quantity"] = quantity
                    print("Car quantity updated successfully!")
                else:
                    print("Invalid quantity!")

            else:
                print("Invalid choice!")

            return

    print("Car not found!")


def add_to_cart():
    car_id = int(input("Enter Car ID: "))

    for car in cars:
        if car["id"] == car_id:

            quantity = int(input("Enter required quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero!")
                return

            if quantity > car["quantity"]:
                print("Insufficient car stock!")
                return

            for item in cart:
                if item["id"] == car_id:
                    item["quantity"] += quantity
                    car["quantity"] -= quantity
                    print("Cart updated successfully!")
                    return

            cart_item = {
                "id": car["id"],
                "brand": car["brand"],
                "model": car["model"],
                "price": car["price"],
                "quantity": quantity
            }

            cart.append(cart_item)
            car["quantity"] -= quantity

            print("Car added to cart successfully!")
            return

    print("Car not found!")


def view_cart():
    if len(cart) == 0:
        print("Cart is empty!")
        return

    total = 0

    print("\n---------------- SALES CART ----------------")
    print("ID\tBrand\tModel\t\tPrice\t\tQty\tSubtotal")

    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal

        print(
            item["id"], "\t",
            item["brand"], "\t",
            item["model"], "\t\t",
            item["price"], "\t",
            item["quantity"], "\t",
            subtotal
        )

    print("---------------------------------------------")
    print("Total Amount:", total)


def remove_from_cart():
    if len(cart) == 0:
        print("Cart is empty!")
        return

    car_id = int(input("Enter Car ID to remove: "))

    for item in cart:
        if item["id"] == car_id:

            for car in cars:
                if car["id"] == car_id:
                    car["quantity"] += item["quantity"]
                    break

            cart.remove(item)

            print("Car removed from cart successfully!")
            return

    print("Car not found in cart!")


def generate_bill():
    if len(cart) == 0:
        print("Cart is empty! Cannot generate bill.")
        return

    total = 0

    print("\n============= FINAL CAR SALES BILL =============")
    print("ID\tBrand\tModel\t\tPrice\t\tQty\tSubtotal")

    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal

        print(
            item["id"], "\t",
            item["brand"], "\t",
            item["model"], "\t\t",
            item["price"], "\t",
            item["quantity"], "\t",
            subtotal
        )

    print("------------------------------------------------")
    print("Total Amount Payable:", total)
    print("Thank you for purchasing!")
    
    cart.clear()

    print("Bill generated successfully!")


def total_inventory_value():
    total = 0

    for car in cars:
        total += car["price"] * car["quantity"]

    print("\nTotal Inventory Value:", total)


while True:

    print("\n========== CAR MANAGEMENT SYSTEM ==========")

    print("1. Add Car")
    print("2. Display All Cars")
    print("3. Search Car")
    print("4. Update Car")
    print("5. Add Car to Sales Cart")
    print("6. View Sales Cart")
    print("7. Remove Car from Sales Cart")
    print("8. Generate Sales Bill")
    print("9. Calculate Inventory Value")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_car()

    elif choice == "2":
        display_cars()

    elif choice == "3":
        search_car()

    elif choice == "4":
        update_car()

    elif choice == "5":
        add_to_cart()

    elif choice == "6":
        view_cart()

    elif choice == "7":
        remove_from_cart()

    elif choice == "8":
        generate_bill()

    elif choice == "9":
        total_inventory_value()

    elif choice == "10":
        print("Thank you for using Car Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
