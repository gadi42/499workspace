#!/usr/bin/env python3
from string import punctuation
import sys


def load_score_dict(dict_file='sentiment.txt'):
    """
    C'mon over here and give me a file, boi
    :param dict_file: A file from which to parse
    :return: A parsed file
    """
    if type(dict_file) is dict:
        return dict_file  # This is assuming the dictionary is properly formatted

    else:
        with open(dict_file, 'r') as given:
            dict_score = {}
            for line in given:
                if line.strip():  # Ignores blank lines
                    word, value = line.split(None, 1)  # Splits lines into desired vars
                    dict_score[word] = value.split()  # Updates dict_score to follow the word [value] format
                    if word == '#':
                        del dict_score['#']  # Gets rid of those nasty sharp bois
        return dict_score


def get_words(sentence):
    """
    This should return an iterable of unique words in string
    :param sentence: A string representing a sentence
    :return: An iterable of the unique words in a string
    """
    # Cut those puncs out of your life, they're a bad influence.
    no_puncs = sentence.translate(str.maketrans('', '', punctuation))
    return set(no_puncs.split())  # Makes a set of the original sentence, sans puncs.


def score_sentence(sentence, score_dict):
    """
    Takes two args and returns the total score?
    :param sentence: A string representing a sentence
    :param score_dict: A "score dictionary"
    :return: A sum of the corresponding scores from each unique word
    """
    checksent = get_words(sentence)
    dict_boi = load_score_dict(score_dict)
    score = []
    for i in checksent:
        if i in dict_boi:
            score.append(dict_boi.get(i))
        # elif i in dict_boi:
        #     pass
    sentscore = sum(score)
    return sentscore


if __name__ == '__main__':

    try:
        comm_int = score_sentence(sys.argv[1], ())
        if comm_int >> 0:
            print('Positive')
        elif comm_int << 0:
            print('Negative')
        elif comm_int == 0:
            print('Neutral')
    except FileNotFoundError:
        print('Please give me a filename to play with next time')
