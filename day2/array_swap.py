
def swap_array(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]


my_array = [1, 2, 3, 4, 5, 6]
swap_array(my_array)
# print(my_array)
my_string = "who is jim"
word_to_check = "jim"

if word_to_check in my_string:
    print(f"The word '{word_to_check}' is present in the string.")
else:
    print(f"The word '{word_to_check}' is not present in the string.")

sum = 0
for i in range(50):
    sum = sum+i
print(sum)
