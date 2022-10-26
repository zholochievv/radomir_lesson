class JunDev:
    def __init__(self, n, s):
        self.name = n
        self.surname = s

    def __str__(self):
        return f'this guy is {self.name} {self.surname}'
    def display_info(self):
        print(f'Name - {self.name}'
              f'Surname - {self.surname}')

class MinDev(JunDev):
    def person(self, n, s, h, w,):
        self.name = n
        self.surname = s
        self.height = h
        self.weight = w

    def __str__(self):
        return f'Name - {self.name}' \ 
               f'Surname - {self.surname}' \
               f'Height - {self.height}' \
               f'Weight - {self.weight}'

a = MinDev("Islam", "Zholochiev", 185, 65)
print(f'{a.name}'
      f'{a.surname}'
      f'{a.weight}'
      f'{a.height}')
a.display_info()
