# You have 100 cats sitting in a line. None of them are wearing hats.

# You traverse this line 100 times.
# On the first pass, you stop at every cat.
# On the second pass, you stop at every second cat.
# On the third pass, you stop at every third cat, and so on.

# Each time you stop at a cat:
# If the cat has a hat on, take it off.
# If the cat does not have a hat on, put one on it.

# After you complete 100 passes through the line of 100 cats,
# which cats will have hats on?

# Step 1: Populate list with 100 hatless cats, represented by 0.
cats = [0]      # empty list did not work for some reason. Need to figure it out.
p = 2            # need to figure out how this happened in detail (did it using trial and error)
for c in cats:
    if p > 100: break
    cats.append(0)
    p += 1
print cats   # => list of 100 hatless cats.
print len(cats) # => 100

# Step 2: Traverse list 100 times.
for times in range(1, len(cats)):
    i = times
    for index in range(0, len(cats), i):   # range(start,stop,step)- Step 3, orchestrate stops.
        if cats[index] == 0:
            cats[index] = cats[index] + 1  # 0 (hatless cat) becomes hatted (1)
        else:
            cats[index] = cats[index] - 1 # 1(hatted cat) becomes hattless (0)
# Step 3: Figure out how many and which cats are hatted. 
print cats
hatted_cats = []
for iob, j in enumerate(cats): # iob = index of object, j = object in list "cats"
    if j == 1:                 # enumerate used to refer to both index and object
        hatted_cats.append(iob)
print len(hatted_cats)
print hatted_cats # => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
