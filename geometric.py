import math

def prob(n,p):
      return(p*pow((1-p), (n-1)));
print(prob(3,2))

def infoMeasure(n,p):
     return(-math.log2(prob(n,p)));
print(infoMeasure(3,2))

def sumProb(n, p):
  sum = 0
  i = n
  while i > 0:
      sum = sum+prob(i, p)
      i=i-1
  return sum
'''
khi n tiến tới vô cùng thì sumProb(N,p) là tổng sác xuất tất cả các biến cố của phân phối hình học
giá trị này phải tiến tới 1
'''

def  approxEntropy(n,p):
  ent = 0
  i = n
  while i > 0:
       ent=ent+prob(i,p)*infoMeasure(i,p)
       i=i-1
  return ent
print(approxEntropy(1000,0.5))