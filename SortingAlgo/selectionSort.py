# Python program for implementation of Selection
# Sort
a = [64, 25, 12, 22, 11]
print("arr:",a)

for i in range(len(a)-1):
    min_idx = i
    for j in range(i+1, len(a)):
        if a[min_idx] > a[j] :
            min_idx = j

    a[i], a[min_idx] = a[min_idx], a[i]


print("sorted arr: ",a)