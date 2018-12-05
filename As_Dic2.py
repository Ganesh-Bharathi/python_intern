a={}
s=input()
for i in s:
    n=s.count(i)
    a.update({i:n})

print(a)
del(a['a'])
print(a)