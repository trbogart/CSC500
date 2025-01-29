a = [1, 2, 3, 4]

# all work as list, where each item is a dictionary
# we don't want a uniqueness check (for example, there could be 2 payments on the same date), so a set isn't appropriate
ledger = [
    {
        "date": '01/21/2025',
        'description': 'crown',
        'tooth': 4,
        'patient': 'Thomas',
        'charge': 1000.0,
    },
    {
        "date": '01/21/2025',
        'description': 'buildup',
        'tooth': 4,
        'patient': 'Thomas',
        'charge': 200.0,
    },
    {
        "date": '01/12/2025',
        'description': 'cavity',
        'tooth': 3,
        'patient': 'Thomas',
        'charge': 200.0,
    },
    {
        'date': '01/12/2025',
        'description': 'payment',
        'patient': 'Thomas',
        'payment': -500.0,
    },
    {
        'date': '01/12/2025',
        'description': 'insurance payment',
        'patient': 'Thomas',
        'payment': -500.0,
    }
]

def get_charge(e):
    return e.get('charge', 0)
def get_payment(e):
    return e.get('payment', 0)
#  add up charge and payment for each entry
total_charges = sum(map(get_charge, ledger))
total_payments = sum(map(get_payment, ledger))
balance = total_charges + total_payments
print(f'Balance: ${balance:.2f}')

ledger_by_tooth = {}
for item in ledger:
    tooth = item.get('tooth')
    if tooth:
        items_by_teeth = ledger_by_tooth.get(tooth)
        if items_by_teeth:
            # append new item for tooth
            items_by_teeth.append(item)
        else:
            # no existing items, add list containing this item
            ledger_by_tooth[tooth] = [item]

def print_tooth_item_count(tooth):
    print(f'There are {len(ledger_by_tooth.get(tooth, []))} items for tooth {tooth}')

print_tooth_item_count(2) # expect 0
print_tooth_item_count(3) # expect 1
print_tooth_item_count(4) # expect 2

