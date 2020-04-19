print("Hello World")

# Variable are case sensitive
# Letters (a-z),underscore, numbers(0,9)
x = 5
y = "Automation"
print(x)                    #5
print(y)                    #Automation
print("Hello" + " "+ y)     #Hello Automation

x = 10
y = 20
print(x+y)                  #50
if 10>5:
    print("10 is greater then 5") #10 is greater then 5
# functions

def sum(a,b):
    print(a+b)
x=sum(20,30)

# Numbers
# don not need to give data type as python can take by defualt
x=5
y=5.5
z=4j

# to see Type of variable
print(type(x))          #<class 'int'>
print(type(y))          #<class 'float'>
print(type(z))          #<class 'complex'>

#casting
x = int(2)
y = int(2.5)
z = float(1)
b = str(10)

print(x)                #2
print(y)                #2
print(z)                #1.0
print(b)                #10

# String operation
x = "  Hello,World  "
print (x)                           # Hello,World
print(x[4])                         #l
print(x[3:9])                       #ello,W
print(len(x))                       #15
print(x.lower())                    #  hello,world
print(x.upper())                    #  HELLO,WORLD
print(x.strip())                    #Hello,World
print(x.replace("o","v"))           #  Hellv Wvrld
print(x.split(","))                 #['  Hello', 'World  ']

# user input value
print("Enter your name")
x = input()
print("Hello" + " " +x)             #Enter your name
                                    #vinay
                                    #Hello vinay
