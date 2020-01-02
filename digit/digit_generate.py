""" 2020/01/02
Generate a digit PIN number

"""

import random


def random_num():
    """ create digit number """
    return random.randint(1, 9)


def create_digit_num(digit_num):
    """ Generate number of specified times """
    return [random_num() for _ in range(digit_num)]


def sample_run():
    digit_4 = create_digit_num(4)
    print(digit_4)

    digit_6 = create_digit_num(6)
    print(digit_6)


if __name__ == "__main__":
    sample_run()
