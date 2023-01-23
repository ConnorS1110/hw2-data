import math

class SYM:
    def __init__(self):
        self.n = 0
        self.has = {}
        self.most = 0
        self.mode = None

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = 1 + self.has.get(x, 0)  # Return to later for dictionary
            if self.has[x] > self.most:
                self.most = self.has[x]
                self.mode = x

    def mid(self):
        return self.mode

    def div(self):  # Removed all parameters
        def fun(p):
            return p * math.log(p, 2)

        e = 0
        for _, value in self.has.items():
            e += fun(value / self.n)
        return -e
