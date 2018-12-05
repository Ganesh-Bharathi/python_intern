import re
def check(a):
    for i in a:
        m=re.match(r'(([-+]?)([\d]*)([.]{1})([\d]+)$)',i)
        if m:
            print(m)
            print("True")
        else:
            print("False")

n=int(input())
b=[]
for i in range(n):
    b.append((str(input())))

#print(b)
check(b)