a = [1,2,2,1]
b = [3,3,3,4]
k = 5
ele = [k - i  for i in a]
print(ele)

ele = sorted(ele)
print(ele)

b = sorted(b)
print(b)
for i in range(len(ele)):
    if ele[i] > b[i] :   # b => k - a
        print("NO")
print("YES")


