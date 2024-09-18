class Coffee:
    def __init__(self, name, price):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string of at least 3 characters")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        self._name = name
        self._price = price
        self._orders = []

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def add_order(self, order):
        if not isinstance(order, Order):
            raise ValueError("order must be an instance of Order")
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)


class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters inclusive")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters inclusive")
        self._name = value

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be an instance of Coffee")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0 inclusive")
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))


class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("customer must be an instance of Customer")
        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be an instance of Coffee")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0 inclusive")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        coffee.add_order(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price


def print_menu(coffees):
    print("Coffee Menu:")
    for idx, coffee in enumerate(coffees):
        print(f"{idx + 1}. {coffee.name} - ${coffee.price:.2f}")


def place_order(customers, coffees):
    print_menu(coffees)
    coffee_choice = int(input("Select a coffee by number: ")) - 1
    if coffee_choice < 0 or coffee_choice >= len(coffees):
        print("Invalid coffee choice.")
        return

    customer_name = input("Enter your name: ")
    customer = next((c for c in customers if c.name == customer_name), None)
    if not customer:
        print("Customer not found. Creating new customer.")
        customer = Customer(customer_name)
        customers.append(customer)

    selected_coffee = coffees[coffee_choice]
    price = selected_coffee.price
    order = customer.create_order(selected_coffee, price)
    print(f"Order placed: {customer.name} ordered {selected_coffee.name} for ${price:.2f}")


def view_sales(coffees):
    print("Sales Summary:")
    total_sales = 0
    for coffee in coffees:
        num_orders = coffee.num_orders()
        avg_price = coffee.average_price()
        total_sales += num_orders * avg_price
        print(f"{coffee.name}: {num_orders} orders, Average price: ${avg_price:.2f}")
    print(f"Total Sales: ${total_sales:.2f}")


def view_inventory(coffees):
    print("Inventory Summary:")
    for coffee in coffees:
        print(f"{coffee.name}: ${coffee.price:.2f} per cup, Total orders: {coffee.num_orders()}")


def main():
    # Create sample data
    customers = []
    coffees = [
        Coffee("Latte", 5.0),
        Coffee("Espresso", 3.0),
        Coffee("Cappuccino", 4.5)
    ]

    while True:
        print("\nCoffee Shop Menu:")
        print("1. Place Order")
        print("2. View Sales")
        print("3. View Inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            place_order(customers, coffees)
        elif choice == "2":
            view_sales(coffees)
        elif choice == "3":
            view_inventory(coffees)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
