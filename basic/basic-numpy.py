# 수학 파이썬 라이브러리
import numpy as np
ar=np.array([1,2,3])
print("타입", type(ar), "Data Type:", ar.dtype)

ar=ar*2
arlist=[]
for a in ar:
    arlist.append(a*2)
print(arlist)
arlist=arlist*2
print("ar:", ar, "arlist:", arlist)
