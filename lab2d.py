#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("Usage: ./lab2d.py name age")
else:
    print(f"Hi {sys.argv[1]}, you are {sys.argv[2]} years old.")
