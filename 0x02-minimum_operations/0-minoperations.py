#!/usr/bin/python3
'''0. Minimum Operations'''


def minOperations(n):
    '''a method that calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    pastedChars = 1  
    inClipBoard = 0  
    counter = 0  

    while pastedChars < n:
        if inClipBoard == 0:
            inClipBoard = pastedChars
            counter += 1

        if pastedChars == 1:
            pastedChars += inClipBoard
            counter += 1
            continue

        notInClipBoard = n - pastedChars
        if notInClipBoard < inClipBoard:
            return 0


        if notInClipBoard % pastedChars != 0:
            pastedChars += inClipBoard
            counter += 1
        else:
            inClipBoard = pastedChars
            pastedChars += inClipBoard
            counter += 2

    if pastedChars == n:
        return counter
    else:
        return 0