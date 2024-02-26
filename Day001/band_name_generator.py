#DAY 1 First project
#band name generator 
#basically its a string manipulate prog
def main():
    print("This is a Band name generator\nit will help you to generate your band name based on your birth city\nand your pet name")

    #input for city and pet
    birth_city = input("Please Enter your Birth city: \n")
    pet_name = input("Please Enter your PET NAME: \n")

    #concatination of both strings and printing
    print("Your Band name is :"+birth_city+" "+pet_name)

#calling the main function    
main()
