#system module

import sys
'''
args = sys.argv # we get the list of arguments

if len(args) != 3:
    print("The script should be called with two arguments, the first and the second number to be multiplied")
else:
    first_num = float(args[1])
    second_num = float(args[2])

    product = first_num * second_num

    print(f"The product of {args[1]} times {args[2]} equals {product}")'''

args = sys.argv

numbers_list = [args[1], args[2], args[3], args[4]]
for num in numbers_list:
    print(int(num))