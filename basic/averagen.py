#!/usr/bin/env python3
N = 10
sum = 0
count = 0
print("Please input 10 number:")
while count < 10:
    number = float(input())
    sum = sum + number
    count += 1
average = sum / N
print("N = {}, Sum = {}".format(N, sum))
print("Average = {:.2f}".format(average))
