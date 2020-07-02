class MeuContainer:
    def __contains__(self):
        return True


obj = MeuContainer()
print(1 in obj)