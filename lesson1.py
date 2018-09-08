# coding: utf8

def isPrime(number):
    """
    definition: A prime number is a natural number that has exactly 2 
    distinct natural number divisors: 1 and itself
    """
    i = 2
    while i <= number/2:
        if number % i == 0:
            # number is a composite number
            return False
        i = i + 1
    return True


def isPrimeByEst(number):
    return True


def test_isPrime():
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(79) == True
    assert isPrime(101) == True


def test_isPrimeByEst():
    assert isPrimeByEst(79) == True


if __name__ == '__main__':
    while True:
        try:
            user_input = raw_input("\n Please enter a natural number between 1 and 99 or 'q' to quit: ")
            number = int(user_input)
            isPrime(number)
            continue

        except ValueError:
            if user_input == 'q':
                break
            print("\n %s is not a valid natural number. Please try another" % (user_input))
            continue

        else:
            break
