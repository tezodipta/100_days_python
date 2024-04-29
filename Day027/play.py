def add(*num):
    #known as *args
    #it can hold unlimited arguments
    total=0
    for digit in num:
        total += digit
    return total

print(add(5,6,7,8))

#**kwargs
#it can hold unlimited keywords
#it works as a dict
def cal(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)

cal(3,add=2,mul=5)