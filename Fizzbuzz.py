# Write a program that prints the numbers from 1 to 100.
# For multiples of three, print "Fizz" instead of the number.
# For multiples of five, print "Buzz"
# For multiples of both, print "FizzBuzz"

data = []
n = 0
while n < 100:
    n = n + 1
    data.append(n)
print data

multiple_of_three = []
for b in data:
    if b % 3 == 0:
        multiple_of_three.append(b)
print multiple_of_three

multiple_of_five = []
for d in data:
    if d % 5 == 0:
        multiple_of_five.append(d)
print multiple_of_five

new = []

for c in data:
    if c in multiple_of_three and c in multiple_of_five:
        new.append("FizzBuzz")
    elif c in multiple_of_three:
        new.append('Fizz')
    elif c in multiple_of_five:
        new.append('Buzz')
    else:
        new.append(c)

print new
