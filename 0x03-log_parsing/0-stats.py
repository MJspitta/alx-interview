#!/usr/bin/python3

import sys


def print_message(sc_dic, total_size):
    """ reads stdin line by line and computes metrics """
    print('File size: {}'.format(total_size))
    for k, v in sorted(sc_dic.items()):
        if v != 0:
            print('{}: {}'.format(k, v))

total_size = 0
code = 0
count = 0
sc_dic = {"200": 0,
          "301": 0,
          "400": 0,
          "401": 0,
          "403": 0,
          "404": 0,
          "405": 0,
          "500": 0}

try:
    for line in sys.stdin:
        p_line = line.split()
        p_line = p_line[::-1]

        if len(p_line) > 2:
            count += 1

            if count <= 10:
                total_size += int(p_line[0])
                code = p_line[1]

                if (code in sc_dic.keys()):
                    sc_dic[code] += 1

            if (count == 10):
                print_message(sc_dic, total_size)
                count = 0
finally:
    print_message(sc_dic, total_size)
