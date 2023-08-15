#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ("x", "y")
    if len(sentence) == 0:
        return tup(0, None)
    tup = (len(sentence), sentence[0])
    return tup
