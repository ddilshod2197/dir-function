class Obiect:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Arxitektor(Obiect):
    def __init__(self, name, age, experience):
        super().__init__(name, age)
        self.experience = experience

arxitektor = Arxitektor("John", 30, 10)

print(arxitektor.__dict__)
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. Python ni o'rnatib oling.
2. Kodni yozib ol va ishlab ko'ring.
3. `__dict__` attribute ni chiqarib ko'ring.
