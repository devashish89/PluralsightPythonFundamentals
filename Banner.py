"""
Prints message in banner
"""
import sys
def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)



if (__name__ == "__main__"):
    banner("hello Deva")
    print("@"*50)
    banner("hello Dev", "*")
    print("@"*50)
    banner(border='.', message="Hello Deva!")