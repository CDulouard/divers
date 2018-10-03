# coding: utf-8
from reseau1.Vecteur import Vecteur
from reseau1.Neurone import Neurone

class Reseau:

    def __init__(self):
        self.structure = []
        pass

    def add_neurone(self, couche, neurone):
        try:
            if(couche >= 0) and type(neurone) is Neurone:
                if len(self.structure) <= couche:
                    for i in range((couche - len(self.structure)) + 1):
                        self.structure += [[]]

                self.structure[couche].append(neurone)
                print(self.structure)
        except:
            print("wrong inputs")



test = Reseau()
N1 = Neurone()
N2 = Neurone()

test.add_neurone(1, N1)
test.add_neurone(1, N2)
print("done")