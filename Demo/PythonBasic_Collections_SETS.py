# Sets is created using curly brackets {} , Unordered ,unindexed,unchangeable,no duplicates
my_sets = {"banana", "apples", "oranges"}
print ( my_sets )  # {'banana', 'apples', 'oranges'}
# length of set
print ( len ( my_sets ) )  # 3

for val in my_sets:
    print ( val )  # banana apples oranges

print ( "banana" in my_sets )  # True
# add
my_sets.add ( "grapes" )
print ( my_sets )  # {'banana', 'grapes', 'apples', 'oranges'}

# update : to add elements
my_sets.update ( ["cheery", "watermelon"] )
print ( my_sets )  # {'apples', 'grapes', 'oranges', 'banana', 'watermelon', 'cheery'}

# remove element
my_sets.remove ( "apples" )
print ( my_sets )  # {'oranges', 'watermelon', 'grapes', 'cheery', 'banana'}

# discard is used if we are not sure if the element exist or not. If element not present it will not throw error while remove will through error
my_sets.discard ( "grapes" )
print ( my_sets )  # {'oranges', 'cheery', 'watermelon', 'banana'}

# pop: this will remove element randomly
my_sets.pop ()
print ( my_sets )  # {'cheery', 'oranges', 'watermelon'}
# clear: this will clear the elements

my_sets.clear ()
print ( my_sets )  # set()

# Multiple data type
my_sets_1 = {"banana", 1, 2, (3, 4, 5)}  # {1, 2, 'banana', (3, 4, 5)}
print ( my_sets_1 )

# convert list to set
my_list = [1, 2, 3]  # [1, 2, 3]
print ( my_list )

my_sets_2 = set ( my_list )  # {1, 2, 3}
print ( my_sets_2 )

# UNION INTERSECTION DIFF SYMMETRIC DIFF

A = {'A', 'B', 'C', 'D'}
B = {'A', 'B', 'E', 'F'}

print ( A.union ( B ) )  # {'E', 'D', 'B', 'A', 'F', 'C'}
print ( A.intersection ( B ) )  # {'A', 'B'}
print ( A.difference ( B ) )  # {'C', 'D'}
print ( B.difference ( A ) )  # {'F', 'E'}
print ( A.symmetric_difference ( B ) )  # {'F', 'D', 'C', 'E'}
