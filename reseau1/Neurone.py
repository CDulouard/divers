# coding: utf-8
from reseau1.Vecteur import Vecteur
from math import exp


class Neurone:

    def __init__(self):
        self.weight = Vecteur(1, 1)
        self.bias = -1

    def _set_weight(self, vecteur):
        self.weight = vecteur.copy()

    def _get_weight(self):
        return self.weight._get_value()

    def sigma(self, inputs):
        temp = self.weight.product(inputs)
        print(temp._get_value())
        return (temp.sum_value() - self.bias)

    def seuil(self, seuil, value):
        if value > seuil:
            return value
        else:
            return 0

    def sigmoid(self, value):
        return 1 / (1 + (exp(value)))

    def compute(self, inputs):
        return self.sigmoid(self.sigma(inputs))

