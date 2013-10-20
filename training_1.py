#!/usr/bin/env python2
# -*- coding: utf-8 -*-
u"""
Write a program that prints the temperature closest to 0 among input data.

INPUT:
Line 1: N, the number of temperatures to analyse
Line 2: The N temperatures expressed as integers ranging from -273 to 5526

OUTPUT:

Display 0 (zero) if no temperature is provided
Otherwise, display the temperature closest to 0, knowing that if two numbers are
  equally close to zero, positive integer has to be considered closest to zero
  (for instance, if the temperatures are -5 to 5, then display 5)


CONSTRAINTS:
0 ≤ N < 10000
"""
if int(raw_input()):
    temp_list = sorted([[int(x), abs(0-int(x))] for x in raw_input().split()], key=lambda x: x[1])
    min_distance = temp_list[0][1]
    candidates = filter(lambda x: x[1] == min_distance, temp_list)
    if len(candidates) == 1:
        print(candidates[0][0])
    else:
        positive_temp = filter(lambda x: x[0] > 0, candidates)
        if positive_temp == []:
            print(candidates[0][0])
        else:
            print(positive_temp[0][0])
else:
    print(0)
