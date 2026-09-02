class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = {
            "P001": Product("P001", "Laptop", 55000, 8),
            "P002": Product("P002", "Wireless Mouse", 799, 25),
            "P003": Product("P003", "Keyboard", 1299, 15),
            "P004": Product("P004", "USB Cable", 299, 30),
            "P005": Product("P005", "Headphones", 1499, 12)
        }

    def add_product(self):
        print("\n--- Add New Product ---")

        product_id = input("Enter Product ID: ").strip()

        if product_id in self.products:
            print("Product ID already exists.")
            return

        name = input("Enter Product Name: ").strip()

        try:
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Quantity: "))

            if price < 0 or quantity < 0:
                print("Price and quantity cannot be negative.")
                return

        except ValueError:
            print("Please enter valid numbers.")
            return

        if not name:
            print("Product name is required.")
            return

        self.products[product_id] = Product(
            product_id,
            name,
            price,
            quantity
        )

        print("\nProduct added successfully.")

    def view_products(self):
        print("\n" + "=" * 75)
        print("                         INVENTORY")
        print("=" * 75)

        if not self.products:
            print("No products available.")
            return

        for product in self.products.values():
            total_value = product.price * product.quantity

            print(f"Product ID : {product.product_id}")
            print(f"Name       : {product.name}")
            print(f"Price      : ₹{product.price:.2f}")
            print(f"Quantity   : {product.quantity}")
            print(f"Stock Value: ₹{total_value:.2f}")
            print("-" * 75)

    def search_product(self):
        keyword = input(
            "\nEnter Product ID or Name to search: "
        ).strip().lower()

        found = False

        for product in self.products.values():
            if (
                keyword == product.product_id.lower()
                or keyword in product.name.lower()
            ):
                print("\nProduct Found")
                print(f"Product ID : {product.product_id}")
                print(f"Name       : {product.name}")
                print(f"Price      : ₹{product.price:.2f}")
                print(f"Quantity   : {product.quantity}")

                found = True

        if not found:
            print("\nNo matching product found.")

    def update_product(self):
        product_id = input(
            "\nEnter Product ID to update: "
        ).strip()

        if product_id not in self.products:
            print("Product not found.")
            return

        product = self.products[product_id]

        print("\nLeave a field blank to keep its current value.")

        new_name = input(
            f"Product Name [{product.name}]: "
        ).strip()

        new_price = input(
            f"Price [{product.price}]: "
        ).strip()

        new_quantity = input(
            f"Quantity [{product.quantity}]: "
        ).strip()

        if new_name:
            product.name = new_name

        if new_price:
            try:
                price = float(new_price)

                if price < 0:
                    print("Price cannot be negative.")
                    return

                product.price = price

            except ValueError:
                print("Invalid price.")
                return

        if new_quantity:
            try:
                quantity = int(new_quantity)

                if quantity < 0:
                    print("Quantity cannot be negative.")
                    return

                product.quantity = quantity

            except ValueError:
                print("Invalid quantity.")
                return

        print("\nProduct updated successfully.")

    def delete_product(self):
        product_id = input(
            "\nEnter Product ID to delete: "
        ).strip()

        if product_id not in self.products:
            print("Product not found.")
            return

        product = self.products[product_id]

        confirmation = input(
            f'Delete "{product.name}"? (y/n): '
        ).strip().lower()

        if confirmation == "y":
            del self.products[product_id]
            print("\nProduct deleted successfully.")
        else:
            print("\nDelete operation cancelled.")

    def low_stock_alert(self):
        print("\n" + "=" * 55)
        print("                    LOW STOCK ALERT")
        print("=" * 55)

        low_stock_found = False

        for product in self.products.values():
            if product.quantity <= 5:
                print(
                    f"{product.product_id} - "
                    f"{product.name} - "
                    f"{product.quantity} units"
                )
                low_stock_found = True

        if not low_stock_found:
            print("No products are currently low in stock.")

    def sell_product(self):
        product_id = input(
            "\nEnter Product ID to sell: "
        ).strip()

        if product_id not in self.products:
            print("Product not found.")
            return

        product = self.products[product_id]

        try:
            quantity = int(input("Enter quantity to sell: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

        except ValueError:
            print("Please enter a valid quantity.")
            return

        if quantity > product.quantity:
            print("Insufficient stock.")
            return

        product.quantity -= quantity

        total = quantity * product.price

        print("\nSale completed successfully.")
        print(f"Product  : {product.name}")
        print(f"Quantity : {quantity}")
        print(f"Total    : ₹{total:.2f}")
        print(f"Remaining Stock: {product.quantity}")


def main():
    inventory = Inventory()

    while True:
        print("\n" + "=" * 60)
        print("             INVENTORY MANAGEMENT SYSTEM")
        print("=" * 60)
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Low Stock Alert")
        print("7. Sell Product")
        print("8. Exit")
        print("=" * 60)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            inventory.add_product()

        elif choice == "2":
            inventory.view_products()

        elif choice == "3":
            inventory.search_product()

        elif choice == "4":
            inventory.update_product()

        elif choice == "5":
            inventory.delete_product()

        elif choice == "6":
            inventory.low_stock_alert()

        elif choice == "7":
            inventory.sell_product()

        elif choice == "8":
            print("\nThank you for using Inventory Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()