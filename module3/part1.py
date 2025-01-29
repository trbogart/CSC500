def main():
    # hard-coded constants
    tip_pct = .18
    sales_tax_pct = .07
    # input price
    charge = float(input('Enter the price of the meal to calculate tip and sales tax: '))
    # calculate tip and sales tax
    tip = charge * tip_pct
    sales_tax = charge * sales_tax_pct
    # sum all 3 numbers to get the total
    total = charge + tip + sales_tax
    # print values
    print(f'Tip: ${tip:.2f}')
    print(f'Sales tax: ${sales_tax:.2f}')
    print(f'Total: ${total:.2f}')

if __name__ == '__main__':
    main()