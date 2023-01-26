#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        char = None
        return (0, char)
    else:
        char = sentence[0]
        return (len(sentence), char)
