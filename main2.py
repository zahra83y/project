# تمرین1
sen =int(input("inter your age:"))
sanie = sen *365*24*60*60
daghighe = sen *365*24*60
sat = sen *360*24
print("your age in hours:", sat)
print("your age in minutes:", daghighe)
print("your age in seconds:", sanie)
# تمرین2
number = int(input("enter your number:"))
ten = number // 10
one = number % 10
r_num = one *10 + ten
print("number reverse:",r_num)
# تمرین3
num = int(input("enter a tow-digit number:"))
ten = num // 10
one = num % 10
r1 = ten ** one
r2 = one ** ten
print(ten , "به توان",one,"=",r1)
print(one , "به توان",ten,"=",r2)