# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import close
from typing import Counter


def read_file_content(filename):
    # [assignment] Add your code here
    f = open('story.txt', 'r')
    filename = f.read()
    filename = filename.lower()
    # print(filename)
    return filename
    f.close()


read_file_content("./story.txt")


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words = text.split()
    count_words = Counter(words)
    # print(words)
    print(count_words)


count_words()
