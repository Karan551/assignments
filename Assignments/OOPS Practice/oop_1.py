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
ram.showMe()
print(ram)
# print(dir(ram))