#!/usr/bin/env python3

String = []
with open('/tmp/String.txt') as fobj:
    for line in fobj:
        for x in line:
            if x.isdigit():
                String.append(x)
print(''.join(String))
