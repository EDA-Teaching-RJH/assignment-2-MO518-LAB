### Part Four -- your code goes here. 
import random

my_list = [random.randint(1,100) for _ in range(10)]
print("Old List", my_list)

i = 0
while i < len(my_list):
    if my_list[i] % 2 == 0:
        my_list.pop(i)
    else:
        i += 1

print("New List", my_list)