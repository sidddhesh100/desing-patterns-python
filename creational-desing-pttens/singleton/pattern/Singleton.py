from typing import Any
from copy import copy

class Singleton(object):
    value = []
    def __new__(cls) -> Any:
        print("cretate a class")
        return cls

    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        return cls.value

class Singleton2(Singleton):
    def __new__(cls) -> Any:
        super(Singleton, cls).__new__()
        return cls

obejct_1 = Singleton()
print(f"object 1' id {id(obejct_1)}")
obejct_2 = Singleton()
print(f"object 2' id {id(obejct_2)}")
obejct_3 = copy(obejct_2)
print(f"object 3' id {id(obejct_3)}")
obejct_4 = Singleton()
print(f"object 4' id {id(obejct_4)}")
