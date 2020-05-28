#!/usr/bin/env python3


def letter_count(user_text, user_letter):
    """

    :param user_text: This parameter is for a string of text
    :param user_letter: This parameter is to find the occurrences of a specific letter
    within the given string of text
    :return: The occurrences of that specific letter within the given text string
    """

    whoopsie = user_text.lower()
    doopsie = user_letter.lower()
    checkit = 0
    for char in whoopsie:
        if char == doopsie:
            checkit += 1
            # This loop took way longer than I'd like to admit.

    return checkit


if __name__ == '__main__':  # Use this for test code after defining your functions

    test_word = [("TOOTS", 'o'), ("foo", 'f'), ("incorrect", 'a'), ("bottle", 'l'), ("Hasselhoff", 'H'), ("hEy lIsTeN",
                                                                                                          'E')]

    for i in test_word:
        test = letter_count(i[0], i[1])
        print(test)
