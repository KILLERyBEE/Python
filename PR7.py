#Fibonacci Series
"""
a =0
b =1
c = 0
n = 6
while n>0:
    print(c)
    c = a +b
    a = b
    b = c
    n = n -1
"""

#Sum of Five digits

n = 12345
sum1 = 0
rem = 0
while n>0:
    rem = n % 10
    sum1 = rem + sum1
    n = n//10
print("Sum = ",sum1)
