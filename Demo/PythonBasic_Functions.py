# Syntax of Functions
# def func_name(paramaeter):

def printHello():
    print ( "Hello World" )

printHello ()  # Hello World

def printHi(name="DefaultName"):
    print ( "Hi, " + name )

printHi ( "Vinay" )  # Hi,Vinay
printHi ()  # Hi, DefaultName

def sum1(a=5, b=5, c=5):
    print ( a + b + c )

sum1 ( 10, 15, 20 )  # 45
sum1 ()  # 15

# adding return type
def returnSum(a, b):
    """This is function to calculate sum of 2 numbers"""
    return a + b
x = returnSum ( 5, 6 )
print ( x )             #11
