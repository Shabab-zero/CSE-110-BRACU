# Task-20(ungraded)

original_data = input("Enter data: ")[1: -1]
data_without_brackets = original_data.strip(' []')
data_in_string_format = data_without_brackets.split(',')
final_data = []

print("Original Data:", original_data)
print('After removing square brackets:', data_without_brackets)
print("Numbers in string format with extra white spaces:", data_in_string_format)

for i in data_in_string_format:
    final_data.append(int(i))

print("Final data (numbers in list format):", final_data)