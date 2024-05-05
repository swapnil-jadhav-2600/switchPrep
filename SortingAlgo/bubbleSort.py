arr = [64, 34, 25, 12, 22, 11, 90]
# arr = [1,2,3]

print('arr = ', arr)

l = len(arr)

for i in range(l):
    flag = False
    for j in range(l-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            flag = True
    if flag == False:
        break

print("sorted_arr =" ,arr )
