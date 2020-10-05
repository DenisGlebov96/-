lst = [1,2,3,1,3]
for i in range(0,len(lst)):
    s = lst[i]
    c = lst.count(s)
    if c == 1:
        index = i
lst.pop(index)
print(lst)