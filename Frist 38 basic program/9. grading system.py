mark=int(input("Enter The Mark:"))
if (mark>=80 and mark<=100):
    grade="A+"
elif (mark>=70 and mark<=79):
    grade="A"
elif (mark>=60 and mark<=69):
    grade="A-"
elif (mark>=50 and mark<=59):
    grade="B"
elif (mark>=45 and mark<=49):
    grade="C"
elif (mark>=40 and mark<=44):
    grade="D"
else:
    grade="Fail"
print(grade)