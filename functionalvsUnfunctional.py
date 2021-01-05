# Inspiration https://www.youtube.com/watch?v=e-5obm1G_FY
# https://codewords.recurse.com/issues/one/an-introduction-to-functional-programming

import argparse

a = 0


def increment1() -> int:
    global a
    while a < 5:
        a += 1
        print(a)


def increment2(b) -> int:
    while b < 5:
        b += 1
        print(b)


parser = argparse.ArgumentParser()
parser.add_argument('f', type=str,
                    help='increase value of a variable by 1 until it reaches 5')
parser.add_argument('-f', '--functional', action='store_true',
                    help='Switch to functional code')
args = parser.parse_args()

if args.f == 'increment1':
    increment1()
elif args.f == 'increment2':
    b = int(input('Please input an integer: '))
    increment2(b)
