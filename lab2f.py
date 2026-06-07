#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    sys.exit(1)

count = int(sys.argv[1])

while count > 0:
    print(count)
    count -= 1

print("blast off!")
