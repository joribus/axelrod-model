import random

class individuo:
    def __init__(self, feature=4, traits=3):
        self.feature = []
        for i in range(feature):
            self.feature.append(random.randint(0, traits - 1))

    def showindividuo(self):
        print(self.feature)