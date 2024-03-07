import random


class Individuo:
    def __init__(self, x, y, feature=4, traits=3):
        self.feature = []
        for i in range(feature):
            self.feature.append(random.randint(0, traits - 1))
        self.x = x
        self.y = y

    def showindividuo(self):
        print(f"->({self.x}, {self.y}): {self.feature}")

    def copy_trait(self, r):
        differentFeature_indexes = []
        for i in range(len(self.feature)):
            if self.feature[i] != r.feature[i]:
                differentFeature_indexes.append(i)
        if differentFeature_indexes:
            copiedFeature_index = random.choice(differentFeature_indexes)
            self.feature[copiedFeature_index] = r.feature[copiedFeature_index]
            return copiedFeature_index
        else:
            return -1  # è come None



