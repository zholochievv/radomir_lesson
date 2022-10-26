class Animal:
    def __init__(self, млекопитающие, премыкающиеся):
        self.a = млекопитающие
        self.b = премыкающиеся

    def body(self):
        return f'они живые организмы'

    def __str__(self):
        return f'Млекопитающие - {self.a}\n' \
               f'Пресмыкающиеся - {self.b}'


an1 = Animal(млекопитающие= "Кошка", премыкающиеся="Крокодиль")

print(f' Это {an1}\n')
print(an1.body())
print(" *_* "*10)

class Bird(Animal):
    def __init__(self,млекопитающие, премыкающиеся, летяют, не_летяют):
        super().__init__(млекопитающие, премыкающиеся)
        self.fly = летяют
        self.nonfly = не_летяют

    def size(self, size):
        return f' Они обычно {size}'

    def __str__(self):
        return super(Bird, self).__str__()+ f'Умеют летать - {self.fly}\n' \
                                            f'Не умеют летать - {self.nonfly}'
b1 = Bird(млекопитающие = "Собака", премыкающиеся = "Черепаха", летяют = "Аист", не_летяют= "Курица")
print(f'А это {b1}')
print(b1.body())
print(f' Они {b1.size("огромные")}')
print(" *-* "*10)


