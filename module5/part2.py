"""
Returns the number of points for the given number of books
"""
def get_points(books_purchased):
    if books_purchased >= 8:
        return 60
    elif books_purchased >= 6:
        return 30
    elif books_purchased >= 4:
        return 15
    elif books_purchased >= 2:
        return 5
    else:
        return 0
"""
Asks users for number of books that they have purchased this month and
displays the number of points awarded.
"""
def main():
    books_purchased = int(input('Enter number of books purchased this month: '))
    points = get_points(books_purchased)
    print(f'Points awarded: {points}')
if __name__ == '__main__':
    main()