import testfile as test
from row import ROW
from cols import COLS

class DATA:
    def __init__(self, src, x):
        self.rows = []
        self.cols = None
        fun = self.add(x)
        if type(src) == "str":
            test.csv(src, fun)
        else:
            map(src or {}, fun)

    def add(self, t):
        if self.cols:
            t = t.cells and t or ROW(t)
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
            return col
        return test.kap(cols or self.cols.y, fun)
