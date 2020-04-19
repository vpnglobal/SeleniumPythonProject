class MyClass:
    name = 'Vinay'

    # create function with keyword def . Argument Self is a variable in python which is used as a very
    # first argument for any function. Any name can be given
    def sum(self, a, b):
        print ( a + b )

    # every class has a in built function called __init__
    # very first function to be called when object is called
    # Always present  and can be explicitly defined as below
    # Can be parameterised
    # whenever we need to assign some value to some variable or properties then can be deifned in this function

    def __init__(self, name, age):
        self.name = name
        self.age = age


x = MyClass("John", 40)
print(x.name +" "+ "is " + str(x.age))
x.sum(4, 5)
# reference of the object can be deleted in python
del x
# individual property or refernce can also be deleted
del x.name