#!/usr/bin/python3
"""It's still kinda funny to me just how widespread lorem ipsum is as a
placeholder for nonsense text, considering how absolutely deranged the latin
must seem to someone who just, doesn't know about that
"""


def text_indentation(text):
    """Prints a text with 2 new lines after detecting the following chars:
    '.', '?' and ':'. However, text must obviously be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
