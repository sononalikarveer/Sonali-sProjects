# Find the greatest of 2 and 3 numbers

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))


# For 2
# if a > b:
#     print(a, "is greatest")
# elif b > a:
#
#     print(b, "is greatest")
# else:
#     print("both are equal")



# ternary
# if a==b:
#     print("both are equal")
# else:
#     print(a,"is greatest") if a>b else print(b,"is greatest")

# max function
# if a==b:
#     print("both are equal")
# else:
#     print(max(a,b)+ "is Greatest")



# for 3

# if a>b and a>c:
#     print(a, "is greatest")
# elif b>c and b>a:
#     print(b, "is greatest")
# else:
#     print(c, "is greatest")


# temp=a if a>b else b
# result=temp if b>c else c
# print(result,"is gretest")

print(max(a,max(b,c)),"is greatest")
