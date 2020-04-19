# Tuple is created using circular brackets (), Ordered ,Indexed,unchangeable,duplicates
my_tuple = ("Tokyo", "Lisbon", "New York")
print ( my_tuple )  # ('Tokyo', 'Lisbon', 'New York')
print ( my_tuple[2] )  # New York
print ( my_tuple[-1] )  # New York
print ( my_tuple[0:2] )  # ('Tokyo', 'Lisbon')

for val in my_tuple:
    print ( val )  # Tokyo Lisbon New York

# Unchangeable : cannot add or delete any object in Tuple
# my_tuple[1] = "Paris" # TypeError: 'tuple' object does not support item assignment

# length
print ( len ( my_tuple ) )  # 3

# Multiple data Type

my_tuple_2 = ("Paris", (1, 2, 3), ["banana", "apple"])
print ( my_tuple_2 )  # ('Paris', (1, 2, 3), ['banana', 'apple'])
print ( my_tuple_2[2][0] )  # banana
print ( my_tuple_2[2] )  # ['banana', 'apple']

my_tuple_2[2][1] = "grapes"
print ( my_tuple_2 )  # ('Paris', (1, 2, 3), ['banana', 'grapes'])

print ( "Paris" in my_tuple_2 )  # True
print ( "NewYork" in my_tuple_2 )  # False
