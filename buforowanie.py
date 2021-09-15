#!/usr/bin/env python
import time

if __name__ == '__main__':
    for i in range(10):
        print("><>", end=" ")
        time.sleep(0.2)
    print()

"""
Żeby to dobrze zadziałało na aktualnym interpreterze na linux:
python3 -u buforowanie.py 
lub
PYTHONUNBUFFERED=True python3 buforowanie.py 
"""