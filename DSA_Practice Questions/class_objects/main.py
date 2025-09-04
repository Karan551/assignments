from math import pi


class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def show(self):
        print(f"Hello {self.name} How are you and Your age is {self.age}")


class Circle:
    def __init__(self, radius):
        self.r = radius
        self._r = radius
        self.__radius = radius

    # a getter function
    @property
    def radius(self):
        return self.__radius

    # a setter function
    @radius.setter
    def radius(self, r):
        if r >= 0:
            self.__radius = r

    def getArea(self):
        return "{:.4f}".format(pi * self.__radius ** 2)

    def getCircumference(self):
        return "{:.4f}".format(2 * pi * self.__radius)


class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def setDimensions(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def getArea(self):
        return self.__length * self.__breadth

    def getPerimeter(self):
        return 2 * (self.__length + self.__breadth)


class Book:
    def __init__(self, book_id, title, price):
        self.book_id = book_id
        self.title = title
        self.price = price

    def book_info(self):
        return f"Book id :{self.book_id} and Book title is {self.title} and Book price is {self.price}"


class Team:
    def __init__(self, name):
        self.name_list = [name]

    def input_member_name(self):
        while True:
            member_name = input("Enter a member name:: ").lower()

            if member_name in self.name_list:
                print(f"{member_name} is already exists. Please enter a new name.")
                continue
            else:
                self.name_list.append(member_name)

            choice = input("Do you want to enter more name (y/n): ").lower()

            if choice == "n":
                self.display_member_name()
                break

    def display_member_name(self):
        print(", ".join(self.name_list))
        # for name in self.name_list:
        #     print(str(name).title(), end=" ")


# -------------------------- Testing Code-----------

c = Circle(10)

# print('radius value c.r ::', c.r)
# print('radius value c._r ::', c._r)
# print('radius value:: c.__r', c.__radius)
# print("this the value of radius of a circle::", c.radius)
c.radius = 15

# print("this the value of radius of a circle::", c.radius)
# print("area of the circle::", c.getArea())
# print("circumference of the circle::", c.getCircumference())

# ----------
team = Team("Ganesh")
# print(team.display_member_name())
team.display_member_name()
print()
team.input_member_name()
