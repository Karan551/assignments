class MyClass:
    """
    This intro method to help user find their value.
    """

    def __init__(self, value):
        self.value = value

    def showMe(self):
        print(f'I have {self.value} rupees.')

    def __str__(self):
        return f"MyClass instance with value: {self.value}"


# Create An object
# print(MyClass.__doc__)
# print(dir(MyClass))
ram = MyClass(20)


# ram.showMe()
# print(ram)


# print(dir(ram))

class Person:
    def __init__(self, name, age, contact):
        self.name = name
        self.__age = age
        self._contact = contact

    def _get_age(self):
        return self.__age

    def __showInfo(self):
        return f'User name is {self.name} and age is {self.__age} contact is {self._contact}'


class Employee(Person):
    def get_contact(self):
        return self._contact


person1 = Person("Mahesh", 21, "UK")
print("Person name is ", person1.name)
print(person1._get_age())
# print(person1.__showInfo())
# print("Person age is ", person1.__age)
# print("Address is :", person1._contact)
# ram = Employee("Ganesh", 21, "Germany")
# print(ram.name)
# # print(ram.age)
# print(ram.get_contact())
