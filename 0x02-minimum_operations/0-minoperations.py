#!/usr/bin/python3
'''0. Minimum Operations'''


def minOperations(n):
    '''a method that calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    pastedChars = 1  # how many chars in the file
    inCopy = 0  # how many H's copied
    counter = 0  # operations counter

    while pastedChars < n:
        if inClipBoard == 0:
            inClipBoard = pastedChars
            counter += 1

        if pastedChars == 1:
            # paste
            pastedChars += inClipBoard
            # increment operations counter
            counter += 1
            # continue to next loop
            continue

        notInClipBoard = n - pastedChars  # remaining chars to Paste
        # check if impossible by checking if clipboard
        # has more than needed to reach the number desired
        # which also means num of chars in file is equal
        # or more than in the clipboard.
        # in both situations it's impossible to achieve n of chars
        if notInClipBoard < inClipBoard:
            return 0

        # if can't be devided
        if notInClipBoard % pastedChars != 0:
            # paste current clipboard
            pastedChars += inClipBoard
            # increment operations counter
            counter += 1
        else:
            # copyall
            inClipBoard = pastedChars
            # paste
            pastedChars += inClipBoard
            # increment operations counter
            counter += 2

    # if got the desired result
    if pastedChars == n:
        return counter
    else:
        return 0