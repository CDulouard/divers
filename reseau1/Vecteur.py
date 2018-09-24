# coding: utf-8

class Vecteur:

    def __init__(self, *inputs):
        #crée un classe vecteur avec un nombre de parm. variables
        try:
            inputs = str(inputs)[1:-1].split(",")
            self.value = []
            for i in inputs:
                self.value.append(float(i))
        except:
            pass;

    def add_value(self, value):
        #ajoute une composante au bout du vecteur
        try:
            self.value.append(float(value))
        except:
            return 0

    def sum(self, v2):
        #somme une a une les composantes d'un vecteur
        try:
            temp = []
            ans = Vecteur()
            dimV1, dimV2 = len(self.value), len(v2._get_value())
            for i in range(max(dimV1, dimV2)):
                if i < dimV1:
                    V1i = self.value[i]
                else:
                    V1i = 0
                if i < dimV2:
                    V2i = v2._get_value()[i]
                else:
                    V2i = 0
                ans.add_value(V1i + V2i)
            return ans
        except:
            return 0

    def _get_value(self):
        return self.value

    def copy(self):
        return self.sum(Vecteur())

    def product(self, v2):
        #multiplie une a une les composantes d'un vecteur
        try:
            temp = []
            ans = Vecteur()
            dimV1, dimV2 = len(self.value), len(v2._get_value())
            for i in range(max(dimV1, dimV2)):
                if i < dimV1:
                    V1i = self.value[i]
                else:
                    V1i = 0
                if i < dimV2:
                    V2i = v2._get_value()[i]
                else:
                    V2i = 0
                ans.add_value(V1i * V2i)
            return ans
        except:
            return 0

    def sum_value(self):
        #somme les composantes d'un vecteur
        sum = 0
        for i in self.value:
            sum += i
        return sum
