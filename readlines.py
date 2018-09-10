f = open("/var/log/system.log")
str = f.read()
lines_list = str.split("\n")
for i in lines_list:
    counter = counter + 1
    print i
f.close()

#len = str.count("\n")
#print len

#print buf
#f1 = open("system.log")
#f1.write(buf)
#f1.close()

