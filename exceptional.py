"""
Some common errors:

1.)ValueError
2.)TypeError
3.)IndexError
4.)KeyError
5.)OSError (import os)
6.)ImportError (failure in modules import like import sys etc.)
"""

import sys

def convertToInt(val):
    try:
        x = int(val)
        print("Conversion successful", x)
    except ValueError:
        x=-1
        print("Conversion Un-successful - ValueError", x)
    except TypeError:
        x = -1
        print( "Conversion Un-successful - TypeError", x )
    return x

def convertToFloat(val):
    try:
        return float(val)
    except (ValueError, TypeError) as e:
        print("Conversion Error! -- {}".format(e), file=sys.stderr)
        return -1
    
    
def computeRoot(num):
    try:
        if num < 0:
            raise ValueError( "Can not calcuate square root of negative num")
        return num**0.5
    except (ValueError, TypeError) as e:
        print(e)
        return -1

def processFile(file):
    try:
        with open( file, "r" ) as f:
            for line in f.readlines():
                print( line )

    except OSError as e:
        print("Unable to Process File! because of {}".format(e))

def getKey():
    try:
        import msvcrt
        return msvcrt.getch()
    except ImportError as e:
        print("Import Error: {}".format(e))
        return -1


def understandingErrorHandling(num):
    try:
        print("Outer Try")
        try:
            print("Inner Try")
            return num/0
        except ZeroDivisionError as e:
            print("Inner Except Block", e)
            return -1
        finally:
            print("Inner Finally")
    except (ZeroDivisionError, ValueError, TypeError) as e:
        print("Outer Except block", e)
        return -1
    finally:
        print("Outer Finally")

def understandingErrorHandlingwithRaise(num):
    try:
        print("Outer Try")
        try:
            print("Inner Try")
            return num/0
        except ZeroDivisionError as e:
            print("Inner Except Block", e)
            raise
            return -1
        finally:
            print("Inner Finally")
    except (ZeroDivisionError, ValueError, TypeError) as e:
        print("Outer Except block", e)
        return -1
    finally:
        print("Outer Finally")


def understandingErrorHandlingwithRaiseInOuterAlso(num):
    try:
        print("Outer Try")
        try:
            print("Inner Try")
            return num/0
        except ZeroDivisionError as e:
            print("Inner Except Block", e)
            raise
            return -1
        finally:
            print("Inner Finally")
    except (ZeroDivisionError, ValueError, TypeError) as e:
        print("Outer Except block", e)
        raise
        return -1
    finally:
        print("Outer Finally")


if (__name__ == "__main__"):
    print("-"*50)
    print(convertToInt(12))
    print(convertToInt("grtf"))
    print( convertToInt([1,2,34]))

    print(convertToFloat(12))
    print(convertToFloat([1,2,5]))
    print(convertToFloat("cdf"))
    
    print(computeRoot(2))
    print(computeRoot(3.2))
    print( computeRoot(-5))
    print(computeRoot([1,2,3]))
    print(computeRoot("cat"))

    processFile('sample.txt')
    processFile('sample1.txt')

    print("="*75)

    print(understandingErrorHandling(5))
    print( "." * 75 )
    print(understandingErrorHandlingwithRaise(10))
    print( "." * 75 )
    print(understandingErrorHandlingwithRaiseInOuterAlso(13))


    print(getKey())

