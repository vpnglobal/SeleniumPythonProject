# collections - List / Tuple / Set / Dictionary
# list is created using square brackets [] , Ordered ,Indexed,changeable,duplicates
# Tuple is created using circular brackets (), Ordered ,Indexed,unchangeable,duplicates
# Set is created using curly brackets {} , Unordered ,unindexed,unchangeable,no duplicates
# Dictionary is created using curly brackets with key and value  {K:V} , Unordered ,indexed,changeable,no duplicates

my_list = ["Tokyo", "Lisbon", "New York"]
print ( my_list )  # ['Tokyo', 'Lisbon', 'New York']
# just use index position to print particular element
print ( my_list[1] )  # Lisbon
# element can be changed or updated

my_list[2] = "New Delhi"
print ( my_list )  # ['Tokyo', 'Lisbon', 'New Delhi']

for val in my_list:
    print ( val )  # Tokyo  Lisbon  New Delhi

# length of list
print ( len ( my_list ) )  # 3

# append
my_list.append ( "Boston" )
print ( my_list )  # ['Tokyo', 'Lisbon', 'New Delhi', 'Boston']

# insert: will insert at the index position
my_list.insert ( 3, "Mumbai" )
print ( my_list )  # ['Tokyo', 'Lisbon', 'New Delhi', 'Mumbai', 'Boston']

# remove: will remove the object
my_list.remove ( "Tokyo" )
print ( my_list )  # ['Lisbon', 'New Delhi', 'Mumbai', 'Boston']

# pop : pop() : will remove last element
my_list.pop ()
print ( my_list )  # ['Lisbon', 'New Delhi', 'Mumbai']

# pop : pop(index) : will remove element based on index
my_list.pop ( 2 )
print ( my_list )  # ['Lisbon', 'New Delhi']

# del: with index position it will del the particular element else it will delete entire list
del my_list[1]
print ( my_list )   #['Lisbon']

#clear : will clear entire list
my_list.clear()

fruits = ["apple" ,"oranges" , "cherries"]
print(fruits)
#reverse
fruits.reverse()        #['apple', 'oranges', 'cherries']
print(fruits)           #['cherries', 'oranges', 'apple']
#list can be created with multiple datatypes
my_list_2 = ["apples", 1,2,3,4.5]
print(my_list_2)        #['apples', 1, 2, 3, 4.5]

# Nested list
my_list_3 = ["apples",[1,2,3],['a','b','c']]
print(my_list_3)            #['apples', [1, 2, 3], ['a', 'b', 'c']]
print(my_list_3[1])         #[1, 2, 3]
print(my_list_3[2][1])      #b
