import testfile as test
from row import ROW
from cols import COLS

class DATA:
    def __init__(self, src):
        print(type(src))
        self.rows = []
        self.cols = None
        # fun = self.add(x)
        print("Inside DATA Cons ", src)
        fun = lambda x: self.add(x)
        print("Executed fun")
        if type(src) == str:
            print("Inside str condition")
            test.readCSV(src, fun)
        else:
            map(src or {}, fun)

    def add(self, t):
        if self.cols:
            t = t.cells if hasattr(t, "cells") else ROW(t)
            self.rows.append(t)
            self.cols.add(t)
        else:
            self.cols = COLS(t)

    def clone(self, init, x):
        data = DATA({self.cols.names})
        map(init or {}, data.add(x))
        return data

    def stats(self, what, cols, nPlaces):
        def fun(k, col):
            mid = getattr(col, "mid")
            rounded = round(mid(), nPlaces)
            return (rounded, col.txt)
        return test.kap(cols or self.cols.y, fun)
