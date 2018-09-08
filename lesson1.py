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
    """
        To find all the prime numbers less than or equal to a given integer n
    by Eratosthenes' method:
        1. Create a list of consecutive integers
            from 2 through n: (2, 3, 4, ..., n).
        2. Initially, let p equal 2, the smallest prime number.
        3. Enumerate the multiples of p by counting to n from 2p
            in increments of p, and mark them in the list
            (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
        4, Find the first number greater than p in the list that is not marked.
            If there was no such number, stop. Otherwise,
            let p now equal this new number (which is the next prime),
            and repeat from step 3.
        5. When the algorithm terminates,
            the numbers remaining not marked in the list are
            all the primes below n.
    """
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
