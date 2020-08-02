import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True

#list comprehension
print([len(str(math.factorial(i))) for i in range(20)]) #No. of digits in factorial from 0 to 19

print([x for x in range(2, 101)if is_prime(x)])

#set comprehension
print({len(str(math.factorial(i))) for i in range(20)})

#dictionary comprehension
from pprint import pprint as pp

countryToCapital = {"India":"Delhi",
                    "United Kingdom":"London",
                    "Pakistan":"Islamabad",
                    "Bangladesh":"Dhaka"}

pp(countryToCapital)

capitalToCountry = {capital : country for country, capital in countryToCapital.items()}

pp(capitalToCountry)

pp({x: (x, x**2, x**3) for x in range(2, 101) if is_prime(x)})