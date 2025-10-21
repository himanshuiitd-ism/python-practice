#Making a secret language for communication

#Rule 1: take 1st letter and append it in end of its word , replace each space with a special character.

import math 
import random

x= input("enter the message:").split(" ")
s= 0
combinations_1 = ['abc', 'xyz', 'qwe', 'rty', 'uio', 'pas', 'dfg', 'hjk', 'lmn', 'cvb','jkl', 'mno', 'pqr', 'stu', 'vwx', 'yzq', 'wrt', 'tpy', 'ghl', 'bnm']
basic_special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
j=[]
for i in x:
  s=combinations_1[random.randint(0,len(combinations_1)-1)]+i[1:]+i[0]+combinations_1[random.randint(0,len(combinations_1)-1)]
  j.append(s)

m=""
for i in range(len(j)):
  m = m+j[i]+basic_special[random.randint(0,len(basic_special)-1)]

print(m)
y=[]
w=0
for z in range(len(m)):
  if m[z]  in basic_special:
    y.append(m[w+3:z-3])
    w=z+1
for  o in range(len(y)):
  print(y[o][-1]+y[o][:-1])
