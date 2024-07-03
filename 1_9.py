s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

u = s1.union(s2)
print("Union:", u)

i = s1.intersection(s2)
print("Intersection:", i)

d1 = s1.difference(s2)
d2 = s2.difference(s1)
print("Difference (s1 - s2):", d1)
print("Difference (s2 - s1):", d2)

sd = s1.symmetric_difference(s2)
print("Symmetric Difference:", sd)

issub = s1.issubset(s2)
print("s1 is subset of s2:", issub)

issup = s1.issuperset(s2)
print("s1 is superset of s2:", issup)

isdj = s1.isdisjoint(s2)
print("s1 is disjoint with s2:", isdj)

s1.add(9)
print("s1 after adding 9:", s1)

s1.remove(9)
print("s1 after removing 9:", s1)

s1.clear()
print("s1 after clearing:", s1)