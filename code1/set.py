line1 = set(input("Enter line 1 "))
line2 = set(input("Enter line 2 "))
s=line1.union(line2)
print (s)
d= line1.intersection(line2)
print (d)
a=line1.difference(line2)
print (a)
aa=line1.discard(line2)
print(aa)
bb=line1.isdisjoint(line2)
print (bb)