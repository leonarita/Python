class Quadrado:
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim

    def __iter__(self):
        return self

    def __next__(self):
        if self.com < self.fim:
            self.com += 1
            return self.com ** 2
        else:
            raise StopIteration


class Quadrado_Iteravel:
    def __init__(self, com, fim):
        self.com = com
        self.fim = fim

    def __iter__(self):
        for i in range(self.com+1, self.fim+1):
            yield i ** 2


x = Quadrado(0, 5)
print(x)
print(list(x))

y = Quadrado_Iteravel(0, 5)
print(y)
print(list(y))