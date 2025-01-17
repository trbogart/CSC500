def read_int(args):
    while True:
        try:
            return int(input(args))
        except ValueError:
            print('Enter valid integer')

def main():
    num1 = read_int('Enter num1: ')
    num2 = read_int('Enter num2: ')
    print(f'Product is {num1 * num2}')
    print(f'Quotient is {num1 / num2}')

if __name__ == '__main__':
    main()
