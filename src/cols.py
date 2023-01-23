from num import NUM
from sym import SYM

class COLS:
    def __init__(self, t):
        self.names = t
        self.all = []
        self.x = []
        self.y = []
        self.klass = []  # Originally was dictionary
        for n, s in enumerate(t):
            col = s.find("^[A-Z]+") and NUM(n, s) or SYM(n, s)  # Add regular expression here
            self.all.append(col)
            if not s.find("X$"): # Regular expression
                if s.find("!$"): self.klass = col # Regular expression
                if s.find("[!+-]$") and self.y:
                    self.y.append(col)
                elif self.x:
                    self.x.append(col)

    def add(self, row):
        for _, t in enumerate({self.x, self.y}):
            for _, col in enumerate(t):
                col.append(row.cells[col.at])
