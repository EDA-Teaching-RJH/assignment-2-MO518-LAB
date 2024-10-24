### Part Three -- your code goes here. 
listNum = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
listNum.sort()
value = 1

while value in listNum:
    listNum.remove(value)

listNum.extend([7,8])
print(listNum)