# coding: utf-8

from random import uniform
#from math import cos

def generate(nb, file):

    db = open(file, "w")

    for i in range(nb):
        x, y = uniform(-1, 1), uniform(-1, 1)
        val = x / y
        db.write(str(x) + "/" + str(y) + "/" + str(val) + "\n")
    db.close


generate(10, "db.txt")