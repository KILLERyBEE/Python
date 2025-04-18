t1 = (1,1,1,6,9)
print(t1)
print(t1[::2])
count = 0
n=1
for i in t1:
    if n == i:
        count = count + 1

print("Number Occured ",count, " times.")

element = 8
index  = 0
for i in t1:
    if i == element:
        break
    index = index + 1
l = len(t1)-1
if index > l:
    print("Num not found")
else:
    print("Index = ",index)
