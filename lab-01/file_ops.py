#!/usr/bin/python


# Open the license file, read the content into the buffer 
# then close the file descriptor

# f = open('conditions.py')
# f.seek(15)
# lines10 = f.read(5)
# # line11_20 = f.read(10)
# #alllines = f.read()
# # lines10 = f.read(10)
# print (lines10)
# f.close()

# Open the license file, read the content as "lines" into the 
# buffer and close it.

f = open('conditions.py')
file_content = f.read()
print file_content
f.close()

for i in file_content:
    print i

# f = open('conditions.py')
# file_content = f.readlines()
# print file_content
# f.close()