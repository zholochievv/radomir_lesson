class JunDev:
    def __init__(self, name, surname):
        self.n = name
        self.s = surname

    def __str__(self):
        return self.n and self.s

    def display_info(self):
        print(f'Name - {self.n}'
              f'Surname - {self.s}')

class MinDev(JunDev):
    def work(self):
        print(f'{self.n} - Name'
              f'{self.s} - Surname '
              f'this guy is works')

a = MinDev('Azim', "Hohloev")
print(MinDev)
a.display_info()
a.work()

