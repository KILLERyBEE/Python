import PR14Module as pm
'''
str1= pm.ask_input()
pm.display(str1)
'''

a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))

Y = pm.fs(a) + pm.fs(b) + pm.fs(c)

print("EQ = a^2 + b^2 + c^2 = ",Y)
