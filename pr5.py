#reverse
'''
n = int(input("Enter a no. to reverse:"))
rev=0
while n>0:
    rem = n%10
    rev = rev * 10 + rem
    n = n//10

print("Reversed no is:",rev)
'''
#factorial
n = int(input("Enter A number "))
fact = 1
while(n>0):
    fact = fact * n
    n = n-1
print("Factorial is : ",fact)
