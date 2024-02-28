#day 13 learning how to debug
#1st code

# number = int(input("eneter the number to check if it is even or odd:"))
# #at the in the if condition there is only one = sign insted of == sign
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")




#2nd code
    
# #in this code the year is not int at first so we have to convert it to int by using int() function
# year = int(input("enter the year:"))

# if year %4 ==0:
#     if year %100 == 0 :
#         if year %400 == 0 :
#             print("leap")
#         else:
#             print("not")
#     else:
#         print("leap")
# else:
#     print("not")

# #fizzbuzz
# #in this code the 1st if condition is not currect because we put the or condition insted of and condition
# #and also at first we only have if statement on the place of elif statement
# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzbuzz")
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print("buzz")
#     else:
#         print(number)