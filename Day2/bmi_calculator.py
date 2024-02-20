#its is a BMI calculator
weight = eval(input("Enter Your Weight(kg):\n"))
height = eval(input("enter your height(meter)\n"))
my_bmi = int(weight/(height**2))
print("Your BMI is: {}".format(my_bmi))

#its day 3 and and modifying it
if (my_bmi <= 18.5):
    print("You are underweight")
elif (my_bmi < 25):
    print("you have normal weight")
elif (my_bmi < 30):
    print("you are overweight")
elif (my_bmi <35):
    print("you are obese")
else:
    print("you are clinically obese")