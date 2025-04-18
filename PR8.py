l1 = ["Avdhut","Sneha","Avhaa"]
l2 = ["Avdhut","Sagale","Youtube"]

cm = set(l1) & set(l2)
print(cm)

l1.reverse()
print(l1)
leng = len(l1)
print(l1[leng-1])
print(l1[len(l1)-1])
l1.insert(2,"Bayko")
l1.remove("Avdhut")
print(l1)

l3 = l1 + l2

print(l3)

