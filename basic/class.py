class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f'{self.name}は歩きました。')

    def run(self):
        print(f'{self.name}は歩きました。')

    def drink(self, age=20):
        if self.age < 20:
            print(f'お酒は{age}歳を超えてからです。')
        else:
            print(f'{self.name}はお酒を飲みました。: Age({self.age})')


class Pirate(Person):
    def __init__(self, name, age, power):
        super().__init__(name, age)
        self.power = power

    def drink(self, age=20):
        print(f'{self.name}はお酒を飲みました。')

    def robbery(self):
        if self.power < 100:
            print(f'{self.name}は何も奪えませんでした。POWER({self.power})')
        elif 100 <= self.power < 1000:
            point = 150
            before = self.power
            self.power += point
            print(f'{self.name}は家畜を奪いました。\nPOWER: {before} -> {self.power}')
        else:
            print(f'{self.name}は宝石を奪いました。')


aki = Person('Aki', 30)
tom = Person('Tom', 18)
luffy = Pirate('Luffy', 19, 700)
nami = Pirate('Nami', 18, 50)
print(f'{aki.name}, {aki.age}')
print(f'{tom.name}, {tom.age}')
print(f'{luffy.name}, {luffy.age}, {luffy.power}')
print(f'{nami.name}, {nami.age}, {nami.power}')
print('*'*20)
aki.run()
aki.drink()
tom.drink()
print('*'*20)
nami.drink()
luffy.drink()
nami.robbery()
luffy.robbery()
luffy.robbery()
luffy.robbery()
