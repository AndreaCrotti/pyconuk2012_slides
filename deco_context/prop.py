class MyObject:
    @property
    def value(self):
        return 100

    @value.setter
    def value(self, value):
        pass

    @classmethod
    def func(cls):
        pass


my = MyObject()
my.value
my.value = 200

print(my.value)
