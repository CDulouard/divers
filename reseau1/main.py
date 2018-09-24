# coding: utf-8
from reseau1.Vecteur import Vecteur
from reseau1.Neurone import Neurone
from random import uniform

def data_gene(nb):
    data = []
    for i in range(nb):
        x, y = uniform(-10, 10), uniform(-10, 10)
        value =  int((5 * x - y) >= 3)
        data += [x, y, value]
    return data

print(data_gene(10))


v1 = Vecteur(11, 2)

n1 = Neurone()
print(n1.compute(v1))