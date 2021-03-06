import numpy as np

class ActionState(object):

    def __init__(self, t, i, market={}):
        self.t = t
        self.i = i
        self.market = market

    def __hash__(self):
        return hash((self.t, self.i, frozenset(self.market.items())))

    def __eq__(self, other):
        return (self.t, self.i, frozenset(self.market.items())) == (other.t, other.i, frozenset(self.market.items()))

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)

    def __str__(self):
        return str((self.t, self.i, str(self.market)))

    def __repr__(self):
        return self.__str__()

    def toArray(self):
        # arr = [np.array([self.getT()]), np.array([self.getI()])]
        # for k, v in self.getMarket().items():
        #     arr.append(v)
        # return np.array([arr])
        features = self.market['bidask']
        return features.reshape((1, features.shape[0], features.shape[1], features.shape[2])) # required for custom DQN
        return features # (2*lookback, levels, count(features))


    def getT(self):
        return self.t

    def setT(self, t):
        self.t = t

    def getI(self):
        return self.i

    def setI(self, i):
        self.i = i

    def getMarket(self):
        return self.market
