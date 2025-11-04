#objects and reference
a = [12,13,14]
b = [12,13,14]

print(a is b)
print(a == b)

print(id(a))
print(id(b))


########################
name2 = "essoh"
name1 = "essoh"

print("Names: ",  name1 is name2)
print("Names: ",  name1 == name2)
print(id(name1))
print(id(name2))