l=[2,16,27,4,55,9,100]
n=0
p=l[0]
for i in l:
    if i>n:
        n=i
    if i<p:
        p=i
print("Largest number is:",n)
print("Smallest number is:",p)
