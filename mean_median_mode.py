# Enter your code here. Read input from STDIN. Print output to STDOUT


n = input()
x = input()

n_length = int(n)
x_array = x.split (" ")
array = [int(num) for num in x_array]

#MEAN
mean = sum(array) / n_length
final_mean = round(mean, 1)
print(final_mean)

#MEDIAN
sort_array = sorted(array)
if len(sort_array) % 2 == 0:
    position = len(sort_array) / 2
    num1 = sort_array[(int(position)) - 1]
    num2 = sort_array[-(int(position))]
    median = (num1 + num2) / 2
    print(round(median, 1))
else:
    position = len(sort_array) / 2
    median = sort_array[(int(position)) - 1]
    print(round(median, 1))

#MODE
dict_count = {}

for num in array:
    if num in dict_count:
        dict_count[num] += 1
    else:
        dict_count[num] = 1
        
# Find the largest value in the dictionary
max_value = max(dict_count.values())

# Find the key(s) with the largest value(s)
max_keys = [key for key, value in dict_count.items() if value == max_value]

print(min(max_keys))