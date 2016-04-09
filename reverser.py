# 3. Write a `reverse(str)` method that takes a string and returns a reversed version of the string.

s = "example"
new_string = ''
i = -1
for letter in s:
    if i > len(s): break
    new_string = new_string + s[i]
    i = i - 1
print new_string

# Creating a function

def reverser(s):
    i = -1
    new_string = ''
    for letter in s:
        if i > len(s): break
        new_string = new_string + s[i]
        i = i - 1
    print new_string
m = "trial"
reverser(m) # => "lairt" works.

# Accomodate user input
def reverser(s):
    s = raw_input('Enter words to be reversed:\n')
    i = -1
    new_string = ''
    for letter in s:
        if i > len(s): break
        new_string = new_string + s[i]
        i = i - 1
    print new_string

reverser(s)
