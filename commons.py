

class KPitem:

    def __init__(self, w, v, i):
        self.w = w
        self.v = v
        self.profit = v/w
        self.i = i

    def __lt__(self, other):
        return self.profit > other.profit

    def __str__(self):
        return "({}, {})".format(self.v, self.w)

    def __eq__(self, other):
        return self.i == other.i and self.w == other.w and self.v == other.v

def printable_items(items):
    return list(map(lambda item: str(item), items))

def sum_items_v(items):
    return sum(list(map(lambda item: item.v, items)))

def sum_items_w(items):
    return sum(list(map(lambda item: item.w, items)))
