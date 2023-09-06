#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for char in text:
        if char in ['.', '?', ':']:
            print(f'{char}\n\n')
        else:
            print(char, end='')
