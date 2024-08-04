#!/usr/bin/python3
"""
reads stdin line by line and computes metrix
"""
import sys


status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
full_file_size = 0
lines = 0


def print_op():
    """
    prints all
    """
    print("File size:", full_file_size)
    for key, value in status_codes.items():
        if value:
            print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        lines += 1
        line = line.split()
        try:
            file_size = int(line[-1])
            full_file_size += file_size
        except (IndexError, ValueError, TypeError):
            continue
        try:
            status_code = int(line[-2])
            if status_code in status_codes.keys():
                status_codes[status_code] += 1
        except (IndexError, ValueError, TypeError):
            continue
        if lines == 10:
            print_op()
            lines = 0
    print_op()
except KeyboardInterrupt:
        print_op()
