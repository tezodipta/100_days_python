# numbers = [1,1,2,3,5,8,13,21,34,55,89]
# squared_number = [number**2 for number in numbers]
# print(squared_number)
# even_numbers = [number for number in numbers if number %2 == 0]
# print(even_numbers)
f1 = open('Day026/file1.txt', 'r')
f1 = f1.readlines()
f2 = open('Day026/file2.txt', 'r')
f2 = f2.readlines()
common_num = [int(num) for num in f1 if num in f2]
print(common_num)