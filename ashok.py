# -*- coding: utf-8 -*-
"""ashok.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cy7ipdD5mfz3ZhGUU004TRByjhpJVnX2
"""

a=7
b=5
if a>b:
  print("a is gratest")
else:
  ("b is gratest")

n=int(input("enter the range"))
for i in range(1,n+1):
  if i%2==0:
    print(i)

n=int(input("enter the range"))
for i in range(1,n+1):
  if i%2!=0:
    print(i)

import numpy as np
x=([1,2,3,4])
print(x)

import numpy as np
x=np.array([1,2,3,4])
print(x)
print(type(x))

import numpy as np
y=np.linspace(start=1,stop=5)
print(y)

import numpy as np
x=np.arange(start=1,stop=5,step=2)
print(x)

import numpy as np
x=np.ones((3,3))
print(x)

import numpy as np
x=np.zeros((3,3))
print(x)

import numpy as np
x=10*np.random.rand(10)
x=x.astype(int)
print(x)
