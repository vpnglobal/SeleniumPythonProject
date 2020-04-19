num = [1, 2, 3, 4]
add = 0
# For loop
for val in num:
    print ( val )  # 1 2 3 4
for val in num:
    add = add + val
print ( "Total is: ", sum )  # Total is: 10

# For Loop with If Else
fruits = ["apple", "orange", "grapes"]

for val in fruits:
    print ( val )
else:
    print ( "No fruits Left" )  # apple orange grapes No fruits left

# While loop
num = 10
sum = 0
i = 1
while i < num:
    sum = sum + i
    i = i + 1
print ("Total is: ", sum)  # Total is 45
