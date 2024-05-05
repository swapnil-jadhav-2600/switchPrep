arr = [1,1,1,5,3,4]

'''
count Array = [0,0,0,0,0] =  [3,0,1,1,1]
sorted Array = [1,1,1,3,4,5]

Time Complexity  = O(n+k)
Space Comp = k
'''
# l = max(arr)

ind_arr = [0 for  i in range(len(arr))]

for nums in arr : 
    ind_arr[nums] += 1

sort_lis = []
for i in range(len(ind_arr)):
    if ind_arr[i] != 0 :
        for j in range(ind_arr[i]):
            sort_lis.append(i)

print("og arr:", arr)
print("ind arr:", ind_arr)
print("sprted arr : ", sort_lis)