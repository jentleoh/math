# coding: utf8

from lesson1 import isPrime


if __name__ == '__main__':
    while True:
        user_input = raw_input("\n Please input a natural number less than 100: ")
        print "You entered ", user_input
        try:
            number = int(user_input)
        except ValueError:
            print "\n Please enter natural number"
            continue
        else:
            break

    isPrime(number)
