class ElectronicsShop:
    def __init__(self) -> None:
        self.products = {
            "Laptop": (
                ("Lenovo IdeaPad", 65000),
                ("HP Pavilion", 70000),
                ("Dell Inspiron", 75000),
            ),
            "Phone": (
                ("Samsung Galaxy S24", 75000),
                ("iPhone 16", 80000),
                ("OnePlus 13", 70000),
            ),
            "Keyboard": (
                ("Logitech Mechanical Keyboard", 5000),
                ("HP Wireless Keyboard", 2500),
                ("Redgear Gaming Keyboard", 3000),
            ),
            "Mouse": (
                ("Logitech G102", 2000),
                ("Logitech Superlight", 12000),
                ("HP Wireless Mouse", 1500),
            ),
            "TV": (
                ("Samsung 43 inch Smart TV", 35000),
                ("LG 55 inch Smart TV", 60000),
                ("Sony 65 inch Smart TV", 90000),
            ),
            "Fridge": (
                ("Samsung 256L Refrigerator", 30000),
                ("LG 260L Refrigerator", 35000),
                ("Whirlpool 300L Refrigerator", 40000),
            ),
        }

    def get_number(self, number):
        try:
            return int(input(number))
        except ValueError:
            print("Please enter a valid number.")
            return None

    def print_bill(
        self, cart: list[tuple[str, tuple[str, int], int]]
    ) -> None:
        total = sum(product[1] * quantity for _, product, quantity in cart)
        print("\n" + "=" * 50)
        print("          ATHARVA'S ELECTRONIC SHOP")
        print("                 CUSTOMER BILL")
        print("=" * 50)
        for category, (name, price), quantity in cart:
            print(f"Product Category : {category}")
            print(f"Product Name     : {name}")
            print(f"Price            : Rs. {price:,}")
            print(f"Quantity         : {quantity}")
            print(f"Item Total       : Rs. {price * quantity:,}")
            print("-" * 50)
        print(f"TOTAL AMOUNT     : Rs. {total:,}")
        print("=" * 50)
        print("\nThank you for shopping with us!")
        print("Please visit Atharva's Electronic Shop again!")
        print("=" * 50)

    def run(self) -> None:
        print("=" * 50)
        print("   WELCOME TO ATHARVA'S ELECTRONIC SHOP")
        print("=" * 50)
        print("We are happy to have you here!\n")
        categories = tuple(self.products)
        cart: list[tuple[str, tuple[str, int], int]] = []

        while True:
            print("What would you like to purchase?\n")
            for number, category in enumerate(categories, start=1):
                print(f"{number}. {category}")

            category_choice = self.get_number(
                f"\nEnter your choice (1-{len(categories)}): "
            )
            if category_choice is None or not 1 <= category_choice <= len(categories):
                print("Invalid category choice!")
                return

            category = categories[category_choice - 1]
            category_products = self.products[category]

            print("\n" + "=" * 50)
            print(f"Available {category}s:")
            print("=" * 50)
            for number, (name, price) in enumerate(category_products, start=1):
                print(f"{number}. {name} - Rs. {price:,}")

            product_choice = self.get_number(
                "\nEnter the product number you want to purchase: "
            )
            if (
                product_choice is None
                or not 1 <= product_choice <= len(category_products)
            ):
                print("Invalid product choice!")
                return

            quantity = self.get_number("Enter quantity: ")
            if quantity is None or quantity <= 0:
                print("Quantity must be a positive number.")
                return

            product = category_products[product_choice - 1]
            cart.append((category, product, quantity))

            while True:
                answer = input(
                    "Would you like to buy another product? (yes/no): "
                ).strip().lower()
                if answer in ("yes", "y"):
                    break
                if answer in ("no", "n"):
                    self.print_bill(cart)
                    return
                print("Please answer yes or no.")


if __name__ == "__main__":
    ElectronicsShop().run()