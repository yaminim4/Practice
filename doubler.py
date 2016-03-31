#2. Write a `doubler(list)` method that takes a list of integers and returns a
# list with the original elements multiplied by two.

# input_list = raw_input('Enter 5 numbers'%d,) figure out input later.

our_list = [1,2,3,4,5]
def doubler(some_list):
    for i in range(len(some_list)):
        some_list[i] = some_list[i] * 2
    print some_list

doubler(our_list)

# for taking input:

input_list = []
while True:
    input_data = raw_input('Enter numbers. Enter "done" when finished')
    if input_data == 'done': break
    input_data_number = float(input_data)
    input_list.append(input_data_number)

def doubler(some_list):
    for i in range(len(some_list)):
        some_list[i] = some_list[i] * 2
    print some_list

doubler(input_list) 
