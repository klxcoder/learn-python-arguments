a = 1000
b = 1000

print(id(a)) # 140371435526448
print(id(b)) # 140371435526448
print(id(a) == id(b)) # True

s1 = "klx"
s2 = "klx"

print(id(s1)) # 139655328048944
print(id(s2)) # 139655328048944
print(id(s1) == id(s2)) # True