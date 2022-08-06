# ###########################################################
# author :
# name : generator.py
# version : 1.2
# Python version : 3
# syntax : python generator.py mywordlist.txt
# how to : create a text file named data.txt and write yours words then save and run the script
# ###########################################################
# modules
import os
import math
import sys
from itertools import islice
# fonctions utiles
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
def leet(text):
    getchar = lambda c: chars[c] if c in chars else c
    chars = {"a":"4","e":"3","l":"1","o":"0","s":"5"}
    return ''.join(getchar(c) for c in text)
# https://www.owasp.org/index.php/Password_special_characters
SpecialChars = ["@", "!", "#", "&", ")","(","+","-", "=", "?","/", "[", "]","{","}","_","$","*","%"]
print(" -------------------------- ")
print("!!! WORK IN PROGRESS !!!")
print(" -------------------------- ")
dic = open(sys.argv[1],"rt")
data = dic.read()
words = data.split()
print('Number of words in text file :', len(words))
listsize = int(len(words))
print(" -------------------------- ")
print("Approximative size is : " + str(listsize * 420) + "mb")
print(" -------------------------- ")
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        mot = line.strip()
        f = open("dico.txt", "a")
        # password
        f.write(mot + '\n')
        # Password
        f.write(mot.title() + '\n')
        # p4550rd
        f.write(leet(mot) + '\n')
        # P4550rd
        f.write(leet(mot.title() + '\n'))
        for value in SpecialChars:
        # password@, password!
            f.write(mot + value + '\n')
        # Password@, Password!
            f.write(mot.title() + value + '\n')
		# @password, !password
            f.write(value + mot + '\n')
        # @Password, !Password
            f.write(value + mot.title() + '\n')
            # ------------ 00000 to 99999 ------ #
        i = 0
        while i <= 99999:
            # password00000 à password99999
            f.write(mot + str(i) + '\n')
            # Password00000 à Password99999
            f.write(mot.title() + str(i) + '\n')
            # p4550rd00000 à p4550rd99999
            f.write(leet(mot + str(i)) + '\n')
            # P4550rd99999 à P4550rd99999
            f.write(leet(mot.title() + str(i)) + '\n')
            # 00000password à 99999password
            f.write(str(i) + mot +  '\n')
            # 00000Password à 99999Password
            f.write(str(i) + mot.title() + '\n')
            # 00000p4550rd à 99999p4550rd
            f.write(leet(str(i) + mot) + '\n')
            # 00000P4550rd à 99999P4550rd
            f.write(leet(str(i) + mot.title()) + '\n')
            i = i + 1
        i = 0
        while i <= 99999:
            for value in SpecialChars:
                # password00000@
                f.write(mot + str(i) + value + '\n')
                # Password00000@
                f.write(mot.title() + str(i) + value + '\n')
                # p4550rd00000@
                f.write(leet(mot) + str(i) + value + '\n')
                # P4550rd00000@
                f.write(leet(mot.title()) + str(i) + value + '\n')
                # password@00000
                f.write(mot + value + str(i) + '\n')
                # Password@00000
                f.write(mot.title() + value + str(i) + '\n')
                # @password00000
                f.write(value + mot + str(i) + '\n')
                # @Password00000
                f.write(value + mot.title() + str(i) + '\n')
                # 00000password@
                f.write(str(i) + mot +  value + '\n')
                # 00000Password@
                f.write(str(i) + mot.title() + value + '\n')
                # 00000p4550rd@
                f.write(str(i) + leet(mot) + value + '\n')
                # 00000P4550rd@
                f.write(str(i) + leet(mot.title()) + value + '\n')
                # 00000password@
                f.write(str(i) + mot + value + '\n')
                # 00000Password@
                f.write(str(i) + mot.title() + value + '\n')
                # 00000@password
                f.write(str(i) + value + mot + '\n')
                # 00000@Password
                f.write(str(i) + value + mot.title() + '\n')
            i = i + 1
f.close()
print("-------------------------------" + '\n')
file = 'dico.txt'
size_bytes = os.path.getsize(file)
print("size of the wordlist : " + convert_size(size_bytes) + '\n')
print("-------------------------------" + '\n')
