#!/usr/bin/python3
"""N queens"""
import sys

number = sys.argv
if len(sys.argv) > 2 or len(sys.argv) < 2:
    print(f"Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

k = int(sys.argv[1])


def queens(k, i=0, a=[], b=[], c=[]):
    """discovering all possible positions"""
    if i < k:
        for j in range(k):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(k, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def NQueens(k):
    """a final solution"""
    buffer = []
    c = 0
    for n in queens(k, 0):
        for i in n:
            buffer.append([c, i])
            c += 1
        print(buffer)
        buffer = []
        c = 0

NQueens(k)
