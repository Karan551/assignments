# Que:-1
count_object = 0


class User:

    # Que:-4
    def __init__(self, name="User", age=None, email=None):
        # global count_object
        self.name = name
        self.age = age
        self.email = email

    # Que:2

    def greet(self):
        return f'Welcome {self.name}'

    def get_age(self):
        return self.age

    def num_objects(self):
        return self.count_object


ram = User("ram", 42, "someone@gmail.com")
ganesh = User("Ganesh", 25, "xyz@gmail.com")
master = User("Master", 50, "abc@gmail.com")

# Que:-5
# del ram.age
# print("Number of objects", User.num_objects())


# Que:-6


user1 = User("Ganesh", 18)
user2 = User("Mahesh", 39)
user3 = User("Mukesh", 45)
users_lst = (user1, user2, user3)
youngest_user = min(users_lst, key=lambda user: user.age)
elder_user = max(users_lst, key=lambda user: user.age)

print(f"Name: {youngest_user.name} and Age : {youngest_user.age}")
print(f"Name: {elder_user.name} and Age : {elder_user.age}")


# Que:-7
class Laptop:
    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def show_config(self):
        print("Laptop Brand is:", self.brand)
        print("Laptop RAM in GB:", self.ram)
        print("Laptop CPU is:", self.cpu)
        print("Laptop HDD is:", self.hdd)


laptop1 = Laptop("Dell", 8, "octa core", "350 GB")
laptop2 = Laptop("HCL", 4, "octa core", "250 GB")
laptop3 = Laptop("Toshiba", 12, "octa core", "500 GB")

# Laptop list
laptop_lst = [laptop1, laptop2, laptop3]

# Que:8
laptop_lst.sort(key=lambda self: self.ram)

for laptop in laptop_lst:
    print(laptop.show_config())


# Que:9

class School:
    principal = "Master"

    def __init__(self, name, classes, address):
        self.name = name
        self.classes = classes
        self.address = address


# Que:10
class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def emp_info(self):
        print("Employee ID :", self.empid)
        print("Employee Name :", self.name)
        print("Employee salary :", self.salary)

    pass
