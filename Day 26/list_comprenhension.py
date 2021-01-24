#List Comprehension
numbers = [1,2,3]
new_list = [n*2 for n in numbers]
print(new_list)

name = "Ismael"
new_list = [letter for letter in name]
print(new_list)

new_list = [i*2 for i in range(1,5)]
print(new_list)

list1 = [1,2,3,4,5,6,7,8,9,10]
new_list = [i for i in list1 if i%2==0]
print(new_list)

names = ["Alex", "Beth", "Caroline"]
new_list = [name.upper() for name in names]
print(new_list)