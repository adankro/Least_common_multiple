from functools import reduce
from math import log, floor


def Least_common_multiple_loop(minor: int, mayor: int):
    """This method find the least common multiple
        using a loop or brutal force, is very slow when mayor > 12
        where range is init minor >=1 < mayor.
    """

    aux = minor
    # auxiliar to zigzag in the minor limit.
    result = 1
    while(aux < mayor):
        if result % aux == 0:
            aux += 1
        else:
            result += 1
            aux = minor
    return result


def get_primes_in_range(minor: int, mayor: int):
    '''
    Returns the primes numbers for the indicated range.
    where range is init minor >=1 < mayor.
    '''
    primes = []
    for possiblePrime in range(minor, mayor):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes


def Least_common_multiple_A003418(minor: int, mayor: int):
    '''
    This method follow the formulation exposed on https://oeis.org/A003418
    to obtain the 	Least common multiple (or LCM) of {1, 2, ..., n}
    for n >= 1, a(0) = 1.
    (Formerly M1590)
    where range is init minor >=1 < mayor.
    much better performance than the previus one.
    '''
    # step 1 get Primes list in range:
    primes = get_primes_in_range(minor, mayor)

    # Step 2 list compreencion to obtain the exponents.
    result = [prime ** (floor(log(mayor) / log(prime)))
              for prime in primes if prime != 1]
    return reduce((lambda x, y: x * y), result)
