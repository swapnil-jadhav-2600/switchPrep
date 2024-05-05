s =  "SOSSOSSSO"
l  = len(s)
check = "SOS"*int(len(s)/3)
count = 0

for i in range(len(s)):
    if s[i] != check[i]:
        count += 1
    
print(count)