no_inp = eval(input("Enter a number: "))
def is_prime(number):
    result = True
    for i in range(2,number):
        if number % i == 0:
            result = False
    if result:
        print("Its is a prime number")
    else:
        print("its not a prime number")
is_prime(no_inp)
    