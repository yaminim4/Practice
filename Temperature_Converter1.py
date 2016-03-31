#1. Write a method that, given a temperature in C, returns the temperature in F.

input_temp = raw_input('Enter Temperature in C\n')
try:
    num_input = float(input_temp)
    far_input = (num_input * 1.8) + 32
    print input_temp + ' C is ' + str(far_input) + ' degrees F'
except:
    print "Please enter numeric data."
  
  
    
# By writing a function:

input_temp = raw_input('Enter temperature in Celsius using only numeric data:\n')
num_input = float(input_temp)

def temp_converter(num_input):
    far_input = (num_input * 1.8) + 32
    return far_input

converted_temp = temp_converter(num_input)
print converted_temp
    
