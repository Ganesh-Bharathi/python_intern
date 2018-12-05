import re
line = int(input())
st=[]

for i in range(line):
    st.append(str(input()))

test=re.compile(
    r'(?!.*(\d)(-?\1){3})'
    r'[4|5|6]([\d]{3})-?[\d]{4}(-?)[\d]{4}(-?)[\d]{4}$'
)
for i in st:
    a=test.match(i)
    #b=re.match(r'[4|5|6]([\d])-?(\1\1)([\1\d])-?(\3\3)([\3\d])-?(\5\5)([\5\d])$',line)
    #print(a)
    if a:
        print("Valid")
    else:
        print("Invalid")