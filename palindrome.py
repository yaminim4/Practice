# Write a method that takes a string and returns true if it is a
# palindrome. A palindrome is a string that is the same whether written
# backward or forward. Assume that there are no spaces; only lowercase
# letters will be given.
s = raw_input('Enter words to be reversed:\n')
def palindrome(s):
    i = - 1
    new_string = ''
    for letter in s:
        if i > len(s): break
        new_string = new_string + s[i]
        i = i - 1
    print new_string
    if s == new_string:  #can removes spaces or other punctuation and make uniformly lowercase, to test palindromic sentences
        print 'True'
    else:
        print 'False'

palindrome(s)
