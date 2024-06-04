class BBS:
    def __init__(self, seed, p, q):
        self.p = p
        self.q = q
        self.m = p * q
        self.state = seed % self.m

    def next(self):
        self.state = (self.state ** 2) % self.m
        return self.state
