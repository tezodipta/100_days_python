#its a height calculalor

student_height =input("enter student height separated by space\n").split()
sum = 0
count = 0
for i in student_height:
    sum = sum+i
    count +=1

print(f"average heigh is : {round(sum/count)}")
