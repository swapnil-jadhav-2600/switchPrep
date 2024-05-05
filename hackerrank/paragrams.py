import string
s = "We promptly judged antique ivory buckles for the prize"
a  = string.ascii_lowercase+string.ascii_uppercase

flag = True 

for i in a : 
    if i not in a :
        flag =  False
    
print(flag)