from portfolio.ItemToPurchase import ItemToPurchase

class ShoppingCart:
    cart_items = []

    def __init__(self, customer_name: str = "none", current_date: str = 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date

    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)

    def remove_item(self, item_name: str):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item_name:
                self.cart_items.pop(i)
                break
        else:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, item: ItemToPurchase):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                self.cart_items[i].modify_from_item(item)
                break
        else:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        # TODO sum, map, and lambda
        return sum(map(lambda x: x.item_quantity, self.cart_items))

    def get_cost_of_cart(self):
        # TODO sum and map
        return sum(map(lambda item: item.get_item_cost(), self.cart_items))

    def print_total(self):
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print(f'Number of Items: {self.get_num_items_in_cart()}')
        total = 0
        for item in self.cart_items:
            item.print_item_cost()
            total += item.get_item_cost()
        print(f'Total: ${total:.2f}')

    def print_descriptions(self):
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print('Item Descriptions')
        for item in self.cart_items:
            item.print_description()

def print_menu(shopping_cart: ShoppingCart):
    while True:
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        print('Choose an option:')
        option = input()
        if option == 'a':
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
        elif option == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()
        elif option == 'o':
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()
        elif option == 'q':
            return

"""Prompt user for two items, create two objects of the ItemToPurchase class, and output summary with total cost."""
if __name__ == "__main__":
    customer_name = 'John Doe' # input("Enter customer's name:")
    current_date = 'January 1, 2020' # input("Enter today's date:")
    shopping_cart = ShoppingCart(customer_name, current_date)
    # add default values for module 6 milestone
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
    print_menu(shopping_cart)

