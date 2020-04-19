# Dictionary is created using curly brackets with key and value  {K:V} , Unordered ,indexed,changeable,no duplicates
my_dic = {"class": "Employee", "name": "Vinay", "age": 40}
print ( my_dic )  # {'class': 'Employee', 'name': 'Vinay', 'age': 40}
print ( my_dic["name"] )  # Vinay
print ( my_dic.get ( "name" ) )  # Vinay
print ( my_dic.values () )  # dict_values(['Employee', 'Vinay', 40])
for val in my_dic:
    print ( val )  # class name age

for val in my_dic:
    print ( my_dic[val] )  # Employee Vinay 40
for val, val_1 in my_dic.items ():
    print ( val, val_1 )  # class Employee  #name Vinay #age 40
# update
my_dic["name"] = "Mundra"
print ( my_dic )  # {'class': 'Employee', 'name': 'Mundra', 'age': 40}
# Add new key or value
my_dic["sex"] = "Male"
print ( my_dic )  # {'class': 'Employee', 'name': 'Mundra', 'age': 40, 'Sex': 'Male'}

# pop : Remove any key and value
my_dic.pop ( "sex" )
print ( my_dic )  # {'class': 'Employee', 'name': 'Mundra', 'age': 40}
# popitem() : it will remove the last item
my_dic.popitem ()
print ( my_dic )  # {'class': 'Employee', 'name': 'Mundra'}
# del : to dele
del my_dic["class"]
print ( my_dic )  # {'name': 'Mundra'}
my_dic.clear ()
print ( my_dic )  # {}
del my_dic  # {}
