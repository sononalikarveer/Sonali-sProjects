# Program to check the grades of the student
grd = int(input("Enter the grade: "))

# if grd == 0 or grd > 100:
#     print("Invalid")
# elif grd < 50:
#     print("Grade F")
# elif grd >= 50 and grd < 60:
#     print("Grade D")
# elif grd >= 60 and grd < 70:
#     print("Grade C")
# elif grd >= 70 and grd < 80:
#     print("Grade B")
# elif grd >= 80 and grd < 90:
#     print("Grade A")
# elif grd >= 90 and grd <= 100:
#     print("Grade A++")


# if grd > 0 and grd < 50:
#     print("Grade F")
# elif grd >= 50 and grd < 60:
#     print("Grade D")
# elif grd >= 60 and grd < 70:
#     print("Grade C")
# elif grd >= 70 and grd < 80:
#     print("Grade B")
# elif grd >= 80 and grd < 90:
#     print("Grade A")
# elif grd >= 90 and grd <= 100:
#     print("Grade A++")
# else:
#     print("Invalid")
#


if 0 < grd < 50:
    print("Grade F")
elif 50 <= grd < 60:
    print("Grade D")
elif 60 <= grd < 70:
    print("Grade C")
elif 70 <= grd < 80:
    print("Grade B")
elif 80 <= grd < 90:
    print("Grade A")
elif 90 <= grd <= 100:
    print("Grade A++")
else:
    print("Invalid")
