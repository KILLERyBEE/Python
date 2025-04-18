m1 = int(input("Enter marks for sub 1"))
m2 = int(input("Enter marks for sub 2"))
m3 = int(input("Enter marks for sub 3"))
m4 = int(input("Enter marks for sub 4"))
m5 = int(input("Enter marks for sub 5"))

grade = (m1+m2+m3+m4+m5)/5

if (grade>=90):
    print("A grade")
elif (grade>=80):
    print("B grade")
elif (grade >= 70):
    print("C grade")
elif (grade >= 60):
    print("D grade")
else:
    print("Losserrrrrrr")
