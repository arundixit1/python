import os
file = open("C:/Users/arund/Documents/django tutorial/text/tamilmatrimony/urls.py")
for line in file:
    print(file.readline(), end="")
file.close()