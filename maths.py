class Maths:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    @property
    def divide(self):
        if self.b == 0:
            return "ErrorDivisionZero"
        return self.a / self.b
    
    @property
    def mull(self):
        return self.a * self.b
    
    @property
    def add(self):
        return self.a + self.b
    
    @property
    def sub(self):
        return self.a - self.b
