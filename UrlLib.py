#! /usr/bin/env python3
"""
Print all the words in UTF-8 document in URL

Usage: python UrlLib.py <URL>
"""
from urllib.request import urlopen
import sys

def fetch_words(url):
    """Fetch all the words from URL

    Args:
        url: the URL of UTF-8 text document

    return:
        list of words
    """
    storyWords = list()
    with urlopen(url) as story:
        for line in story:
            for word in line.split():
                storyWords.append(word)

    return storyWords

def print_items(storyWords):
    """
    Print the words in UTF - 8 format
    :param
        storyWords: list of words
    :return
        void
    """
    for word in storyWords:
        print(word.decode("'utf-8"))

def main(url):
    """
    :param - URL as Input Argument to module

    :return - void
    """
    print_items(fetch_words(url))


print(__name__) # __name__ == __main__ it means module is being executed

if __name__ == "__main__":
    main(sys.argv[1])

    # convert bytes to string using decode(encoding) / convert string to bytes using encode(encodng)

    #print( [word.decode( 'utf-8' ) for word in fetch_words(url)])

