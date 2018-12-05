import math
ab=float(input("hi"))
bc=float(input("ho"))

#print(ab,bc)
ac=math.sqrt((ab**2)+(bc**2))
mc=float(ac/2)
Ac=(((ac**2)+(bc**2)-(ab**2))/(2*ac*bc))
bm = math.sqrt((mc**2)+(bc**2)-(2*mc*bc*Ac))
res= (math.acos(((bm**2)+(bc**2)-(mc**2))/(2*bm*bc)))*(180/math.pi)
res = res+0.5
print(int(res))
