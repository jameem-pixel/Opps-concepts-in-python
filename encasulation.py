class MyClass:
    def __init__(self):
        self.public_member = "I'm a public member"
        self._protected_member = "I'm a protected member"
        self.__private_member = "I'm a private member"
        


obj = MyClass()
print(obj.public_member)
print(obj._protected_member)
# it will throw error because we cant access the private from aoutside the class
# print(obj.__private_member)
# but we can access the private by Mangling
print(obj._MyClass__private_member)

