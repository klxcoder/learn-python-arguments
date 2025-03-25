def modify_tuple(t):
    t[1].append(5)

my_tuple = (1, [2, 3], "apple")
my_tuple[1].append(4)
print(my_tuple) # (1, [2, 3, 4], 'apple')

modify_tuple(my_tuple)
print(my_tuple) # (1, [2, 3, 4, 5], 'apple')