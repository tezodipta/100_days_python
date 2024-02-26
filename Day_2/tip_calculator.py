#this prog is going to calculate the tip on a bill and will help to split the bill
total_bill = eval(input("Enter the total bill\n"))
t_person = int(input("Enter the no of person to split the bill\n"))
tip_per = int(input("Enter the tip persentange like 12,10,15:\n"))
print("Each one have to pay",round((total_bill+(total_bill*(tip_per/100)))/t_person,2))