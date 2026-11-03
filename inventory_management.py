
inventory = [
    {"id": 101, "name": "Rice", "price": 60, "quantity": 20},
    {"id": 102, "name": "Milk", "price": 30, "quantity": 15},
    {"id": 103, "name": "Sugar", "price": 45, "quantity": 10}
]

cart = []


def add_product():
    product_id = int(input("Enter Product ID: "))

    for product in inventory:
        if product["id"] == product_id:
            print("Product ID already exists!")
            return

    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    quantity = int(input("Enter Quantity: "))

    if name == "" or price <= 0 or quantity < 0:
        print("Enter valid product details!")
        return

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)
    print("Product added successfully!")


def display_inventory():
    if len(inventory) == 0:
        print("Inventory is empty!")
        return

    print("\n----------- INVENTORY -----------")
    print("ID\tName\t\tPrice\tQuantity")

    for product in inventory:
        print(
            product["id"], "\t",
            product["name"], "\t\t",
            product["price"], "\t",
            product["quantity"]
        )


def search_product():
    product_id = int(input("Enter Product ID to search: "))

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found!")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])
            return

    print("Product not found!")


def update_product():
    product_id = int(input("Enter Product ID to update: "))

    for product in inventory:
        if product["id"] == product_id:
            print("1. Update Price")
            print("2. Update Quantity")

            choice = input("Enter choice: ")

            if choice == "1":
                price = float(input("Enter new price: "))

                if price > 0:
                    product["price"] = price
                    print("Price updated successfully!")
                else:
                    print("Invalid price!")

            elif choice == "2":
                quantity = int(input("Enter new quantity: "))

                if quantity >= 0:
                    product["quantity"] = quantity
                    print("Quantity updated successfully!")
                else:
                    print("Invalid quantity!")

            else:
                print("Invalid choice!")

            return

    print("Product not found!")


def add_to_cart():
    product_id = int(input("Enter Product ID: "))

    for product in inventory:
        if product["id"] == product_id:
            quantity = int(input("Enter required quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero!")
                return

            if quantity > product["quantity"]:
                print("Insufficient stock!")
                return

            for item in cart:
                if item["id"] == product_id:
                    item["quantity"] += quantity
                    product["quantity"] -= quantity
                    print("Cart updated successfully!")
                    return

            cart_item = {
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "quantity": quantity
            }

            cart.append(cart_item)
            product["quantity"] -= quantity
            print("Product added to cart successfully!")
            return

    print("Product not found!")


def view_cart():
    if len(cart) == 0:
        print("Cart is empty!")
        return

    total = 0

    print("\n----------- SHOPPING CART -----------")
    print("ID\tName\t\tPrice\tQty\tSubtotal")

    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal

        print(
            item["id"], "\t",
            item["name"], "\t\t",
            item["price"], "\t",
            item["quantity"], "\t",
            subtotal
        )

    print("-------------------------------------")
    print("Total Amount:", total)


def remove_from_cart():
    if len(cart) == 0:
        print("Cart is empty!")
        return

    product_id = int(input("Enter Product ID to remove: "))

    for item in cart:
        if item["id"] == product_id:

            for product in inventory:
                if product["id"] == product_id:
                    product["quantity"] += item["quantity"]
                    break

            cart.remove(item)
            print("Product removed from cart!")
            return

    print("Product not found in cart!")


def generate_bill():
    if len(cart) == 0:
        print("Cart is empty! Cannot generate bill.")
        return

    total = 0

    print("\n=========== FINAL BILL ===========")
    print("ID\tName\t\tPrice\tQty\tSubtotal")

    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal

        print(
            item["id"], "\t",
            item["name"], "\t\t",
            item["price"], "\t",
            item["quantity"], "\t",
            subtotal
        )

    print("----------------------------------")
    print("Total Amount Payable:", total)
    print("Thank you for shopping!")

    cart.clear()
    print("Bill generated successfully!")


while True:
    print("\n===== SUPERMARKET BILLING SYSTEM =====")
    print("1. Add Product")
    print("2. Display Inventory")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Add to Cart")
    print("6. View Cart")
    print("7. Remove from Cart")
    print("8. Generate Bill")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        display_inventory()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_product()

    elif choice == "5":
        add_to_cart()

    elif choice == "6":
        view_cart()

    elif choice == "7":
        remove_from_cart()

    elif choice == "8":
        generate_bill()

    elif choice == "9":
        print("Thank you for using Supermarket Billing System!")
        break

    else:
        print("Invalid choice! Please try again.")
