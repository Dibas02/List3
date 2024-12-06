lst = [1, 2, 3, 4, 5]

sum = 0

for c in lst:
    sum = sum+c
print("The sum of the elements of the list is: ", sum)


avg = sum/len(lst)
print("The average of the elements is: ", avg)

print("The highest value of the elements is: ", max(lst))
print("The lowest value of the elements is: ", min(lst))
