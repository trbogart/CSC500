"""
Ask user for number of years, then for inches of rainfall in each month.
Prints number of months, total inches of rainfall, and the average rainfall per month.
"""
def main():
    # list of months
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    num_years = int(input('Enter number of years: '))
    num_months = num_years * len(months)
    total_rainfall_inches = 0
    for year in range(num_years):
        for month in months:
            rainfall_inches = int(input(f'Enter rainfall in inches for {month} in year {year + 1}: '))
            total_rainfall_inches += rainfall_inches

    print(f'Number of months: {num_months}')
    print(f'Total rainfall in inches: {total_rainfall_inches}')
    print(f'Average rainfall per month in inches: {total_rainfall_inches / num_months:.2f}')
if __name__ == '__main__':
    main()