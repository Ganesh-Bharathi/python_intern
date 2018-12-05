import re
a=[]
a.extend((re.split(r'[,.]+', input())))
#a=a[0]
for i in a:
    print(i)