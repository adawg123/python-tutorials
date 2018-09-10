#!/usr/bin/python

# if filename < 4:
#         return "error"

# with open('functions.py') as f:
#     lines = f.readlines()


# my_lines = lines[:nlines]

# with open()
import os
import multiprocessing
def print_os_info():

    print multiprocessing.cpu_count()
    print os.uname()[0]
    print os.system("uptime")
    print os.system("df -h")
print_os_info()
