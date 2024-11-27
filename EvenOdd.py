# num=int(input("enter the number: "))
# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd number")


# print("Even number") if num % 2 == 0 else print("Oddd number")

def isEven(num):
    # n&1 is 1, then odd, else even
    return not (num & 1)


num = int(input("Insert a number:"))
print("Even" if isEven(num) else "odd")
