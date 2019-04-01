#!/usr/local/bin/python3.5

'''
Author: afend
Version: 1.1
'''

from collections import Counter
import argparse, string


def get_story(story):
    body = []
    dir = "corpus/"

    with open(dir+story, "r") as f:
        for line  in f:
            if line.strip():
                body.append(line.translate(str.maketrans("", "", string.punctuation)))

    return body

def get_tf(story):
    return Counter(" ".join(story).lower().split(" "))


def main():
    '''
    Given some text from an article, use the collections library to keep track of term frequency

    Example story:
    "To be, or not to be, that is the question."

    Dictionary:
    {"to": 2, "be": 2, "or": 1, "not": 1, "that": 1, "is": 1, "the": 1, "question": 1}
    '''

    parser = argparse.ArgumentParser(description="Retrieve the term frequency from a given story")
    parser.add_argument("--story", dest="story", required=True,  help="File name of the news article in corpus")
    args = parser.parse_args()

    story = get_story(args.story)
    count = get_tf(story)

    print (count)


if __name__ == "__main__":
    main()
