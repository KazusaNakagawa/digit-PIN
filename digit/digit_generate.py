""" 2020/01/02
Generate a digit PIN number

"""

import random
import sys


def random_num():
    """ create digit number """
    return random.randint(1, 9)


def create_digit_num(digit_num):
    """ Generate number of specified times """
    return [random_num() for _ in range(digit_num)]


def continue_run(digit_num):
    while True:
        print('continue "Enter", or "(Q)uit"')
        choice = input().upper()
        if choice == 'Q' or choice == 'QUIT':
            print('Thanks!')
            sys.exit()
        if choice == '':
            run(digit_num)
        if not choice.isdecimal():
            continue  # If the player didn't enter a number, ask again.


def run(digit_num):
    digit = create_digit_num(digit_num)
    print(str(digit) + '\n')
    continue_run(digit_num)


def main():
    print(''' Generate any number of digits.
    ''')

    while True:
        print('Enter the number of digits to generate.')
        digit_num = input()
        if not digit_num.isdecimal():
            continue
        run(int(digit_num))


if __name__ == "__main__":
    main()
