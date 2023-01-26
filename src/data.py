import testfile as test
from row import ROW
from cols import COLS
from misc import *

class DATA:
    def __init__(self, src):
        self.rows = []
        self.cols = None
        fun = lambda x: self.add(x)
        if type(src) == str:
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
        def fun(col):
            mid = getattr(col, what or "mid")
            rounded = round(float(mid()), nPlaces)
            return (rounded, col.txt)
        return kap(cols or self.cols.y, fun)
