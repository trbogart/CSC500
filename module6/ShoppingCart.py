DefaultItemName = "none"
DefaultItemDescription = 'none'
DefaultItemPrice = 0.0
DefaultItemQuantity = 0

"""
An item to purchase.
Attributes:
- item_name: item name (string, default "none")
- item_price: item price (float, default 0.0)
- item_quantity: item quantity (int, default 0)
- item_description: item description (string, default "none")
Methods:
- get_item_cost(): returns total cost (item_price * item_quantity)
- print_item_cost(): print description including total cost as a float, e.g. "Bottled Water 10 @ $1 = $10"
"""
class ItemToPurchase:
    """
    Construct a new item to purchase.
    - item_name: item name (string, default "none")
    - item_price: item price (float, default 0.0)
    - item_quantity: item quantity (int, default 0)
    - item_description: item description (string, default "none")
    """
    def __init__(self,
                 item_name = DefaultItemName,
                 item_price = DefaultItemPrice,
                 item_quantity = DefaultItemQuantity,
                 item_description = DefaultItemDescription
                 ):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    """Return the total cost as a float (item_price * item_quantity)."""
    def get_item_cost(self):
        return self.item_price * self.item_quantity

    """Print the item name, quantity, price, and total cost, e.g. 'Bottled Water 10 @ $1 = $10..'"""
    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.get_item_cost():.2f}')

    """Print item name and description, e.g. 'Nike Romaleos: Volt color, Weightlifting shoes'"""
    def print_description(self):
        print(f'{self.item_name}: {self.item_description}')

    """Modify item from another item, except for name and attributes with default values."""
    def modify_from_item(self, other):
        if other.item_price != DefaultItemPrice:
            self.item_price = other.item_price
        if other.item_quantity != DefaultItemQuantity:
            self.item_quantity = other.item_quantity
        if other.item_description != DefaultItemDescription:
            self.item_description = other.item_description

"""Prints a list of items including the total cost."""
def print_total_cost(*items):
    total_cost = 0.0
    for item in items:
        item.print_item_cost()
        total_cost += item.get_item_cost()
    print(f"Total: ${total_cost:.2f}")


"""Prompts the user to input an item to purchase."""
def input_item():
    item = ItemToPurchase()
    item.item_name = input("Enter the item name: ")
    item.item_price = float(input("Enter the item price: "))
    item.item_quantity = int(input("Enter the item quantity: "))
    return item

"""
Shopping cart
Attributes:
- customer_name (string) - Initialized in default constructor to "none"
- current_date (string) - Initialized in default constructor to "January 1, 2020"
- cart_items (list of ItemToPurchase) - Cart items
"""
class ShoppingCart:
    """
    List of cart items (ItemToPurchase).
    """
    cart_items = []

    """
    Construct a new shopping cart.
    - customer_name: customer name (string, default "none")
    - item_price: item price (float, default 0.0)
    - item_quantity: item quantity (int, default 0)
    - item_description: item description (string, default "none")
    """
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date

    """
    Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    """
    def add_item(self, item):
        self.cart_items.append(item)

    """
    Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    """
    def remove_item(self, item_name):
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                self.cart_items.pop(i)
                break
        else:
            print('Item not found in cart. Nothing removed.')

    """
    Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity.
    If not, modify item in cart.
    If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    """
    def modify_item(self, item):
        for next_item in self.cart_items:
            if next_item.item_name == item.item_name:
                next_item.modify_from_item(item)
                break
        else:
            print('Item not found in cart. Nothing modified.')

    """
    Returns quantity of all items in cart. Has no parameters.
    """
    def get_num_items_in_cart(self):
        return sum(map(lambda item: item.item_quantity, self.cart_items))

    """
    Determines and returns the total cost of items in cart. Has no parameters.
    """
    def get_cost_of_cart(self):
        return sum(map(lambda item: item.get_item_cost(), self.cart_items))

    """
    Outputs total of objects in cart.
    If cart is empty, output this message: SHOPPING CART IS EMPTY
    """
    def print_total(self):
        if len(self.cart_items) > 0:
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print(f'Number of Items: {self.get_num_items_in_cart()}')
            for item in self.cart_items:
                item.print_item_cost()
            print(f'Total: ${self.get_cost_of_cart():.2f}')
        else:
            print('SHOPPING CART IS EMPTY')

    """"
    Outputs each item's description.
    """
    def print_descriptions(self):
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print('Item Descriptions')
        for item in self.cart_items:
            item.print_description()

"""
Populate shopping cart with some default items for testing.
"""
def add_default_items(shopping_cart):
    shopping_cart.add_item(
        ItemToPurchase(
            item_name = 'Nike Romaleos',
            item_description = 'Volt color, Weightlifting shoes',
            item_price = 189,
            item_quantity = 2
        )
    )
    shopping_cart.add_item(
        ItemToPurchase(
            item_name = 'Chocolate Chips',
            item_description = 'Semi-sweet',
            item_price = 3,
            item_quantity = 5
        )
    )
    shopping_cart.add_item(
        ItemToPurchase(
            item_name = 'Powerbeats 2 Headphones',
            item_description = 'Bluetooth headphones',
            item_price = 128,
            item_quantity = 1
        )
    )

"""
Prints a menu of commands for the user to manipulate the given shopping cart until the user quits.
"""
def print_menu(shopping_cart):
    while True:
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print("i - Output items' descriptions")
        print('o - Output shopping cart')
        print('q - Quit')
        option = input('Choose an option: ')
        if option == 'o':
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()
        elif option == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()
        elif option == 'a':
            print('ADD ITEM TO CART')
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            shopping_cart.add_item(ItemToPurchase(item_name, item_price, item_quantity, item_description))
        elif option == 'r':
            print('REMOVE ITEM FROM CART')
            item_name = input("Enter name of item to remove: ")
            shopping_cart.remove_item(item_name)
        elif option == 'c':
            print('CHANGE ITEM QUANTITY')
            item_name = input("Enter the item name: ")
            item_quantity = int(input("Enter the new quantity: "))
            shopping_cart.modify_item(ItemToPurchase(item_name=item_name, item_quantity=item_quantity))
        elif option == 'q':
            return

"""Creates a shopping cart and display menu for user to manipulate it until they quit."""
if __name__ == "__main__":
    # use hard-coded name and date for now
    shopping_cart = ShoppingCart('John Doe', 'January 1, 2020')
    # add default values for now
    add_default_items(shopping_cart)
    print_menu(shopping_cart)
