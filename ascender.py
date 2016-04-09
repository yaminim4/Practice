# 5. Write a method that sorts a given list of numbers in ascending order.

ascending_p = []
def ascender(p):
    while p != []:  # Could use recursion instead of a while loop?
        a = min(p)
        ascending_p.append(a)
        p.remove(a)
    print p
    print ascending_p

purple = [1, 15, 0, -2, 3, 7] # => [-2, 0, 1, 3, 7, 15] 
ascender(purple)
