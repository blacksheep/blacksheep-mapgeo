#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def calc_distances_of(a, b, r =3443.9):
    # 3963.1 statute miles
    # 3443.9 nautical miles
    # 6378 km
    return math.acos(
           math.cos(a[0]) * math.cos(b[0]) * math.cos(a[1]) * math.cos(b[1])
        +  math.cos(a[0])* math.sin(b[0]) * math.cos(a[1]) * math.sin(b[1])
        +  math.sin(a[0])* math.sin(a[1])) * r

def main():
    # a = input()
    # b = input()
    a = (33.606379,  -86.50249)
    b = (33.346817,  -86.95252)
    print calc_distances_of(a,b), ' Miles'

if __name__ == "__main__":
    main()
