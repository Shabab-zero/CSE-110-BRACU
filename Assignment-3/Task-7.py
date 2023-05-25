# Task-7

input_string = input("Enter a string: ")
output_string = ''

for i in input_string:
    if i == 'z':
        output_string += 'a'
    else:
        output_string += chr(ord(i) + 1)

print(output_string)

#OR:
#for i in input_string:

#    if ord(i) < 122:
#        print(chr(ord(i) + 1), end = "")
#    else:
#        print(chr(ord(i) - 25), end = "")