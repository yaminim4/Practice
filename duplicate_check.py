# 4. Write a method that returns `true` if a given list has duplicated values in
# it, and `false` if it does not. (That is, check if all elements of the list are unique.)
# Do this without using the `set()` method.

l = ['1', '2', '3']
unique = []
for item in l:
    if item not in unique:
        unique.append(item)
if len(unique) == len(l):
    print "false"
else:
    print "true" # should be false

# Creating a function

def duplicate_check(l):
    unique = []
    for item in l:
        if item not in unique:
            unique.append(item)
    if len(unique) == len(l):
        print "false"
    else:
        print "true"

m = ['n', 'n', 'n']
n = ['w', 'x', 'y']
p = [0,1,2,3]
q = [0, 0, 0, 1]

duplicate_check(m) # true
duplicate_check(n) # false
duplicate_check(p) # false
duplicate_check(q) # true
