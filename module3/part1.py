def main():
    tip_pct = .18
    sales_tax_pct = .07
    charge = float(input('Enter the price of the meal to calculate tip and sales tax: '))
    tip = charge * tip_pct
    sales_tax = charge * sales_tax_pct
    total = charge + tip + sales_tax
    print(f'Tip: ${tip:.2f}')
    print(f'Sales tax: ${sales_tax:.2f}')
    print(f'Total: ${total:.2f}')

if __name__ == '__main__':
    main()