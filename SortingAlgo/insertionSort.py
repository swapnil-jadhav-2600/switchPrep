arr = [12, 11, 13, 5, 6]


for i in range(1,len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key <arr[j]:
        # print(arr[j+1],arr[j])
        arr[j+1] = arr[j]
        print(arr)
        j -= 1
    # print(arr[j+1], key)
    arr[j+1] = key
    
print(arr)