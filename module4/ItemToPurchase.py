"""
An item to purchase.
Attributes:
- item_name: item name (string, default "none")
- item_price: item price (float, default 0.0)
- item_quantity: item quantity (int, default 0)
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
    """
    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    """Return the human-readable string representation including total cost, e.g. "Bottled Water 10 @ $1 = $10."""
    def __str__(self):
        return f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.get_item_cost():.2f}'

    """Return the total cost as a float (item_price * item_quantity)."""
    def get_item_cost(self):
        return self.item_price * self.item_quantity

    """Print the string representation."""
    def print_item_cost(self):
        print(self) # see __str__

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

"""Prompt user for two items, create two objects of the ItemToPurchase class, and output summary with total cost."""
if __name__ == "__main__":
    print("Item 1")
    item1 = input_item()
    print("Item 2")
    item2 = input_item()
    print("TOTAL COST")
    print_total_cost(item1, item2)