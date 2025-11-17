class Hero:

    jumlah = 0
    
    _hero__privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        self.__private = 'private'
        self.__protected = 'protected' # ada error di nama selt = self

hero_1 = Hero('Atsu', 100)

print(hero_1.__dict__)
print(Hero.__dict__)
print(Hero._hero__privateJumlah) # harus melakukan name mangling