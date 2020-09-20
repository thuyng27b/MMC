import math

def prob(n,p,r):
  def giaiThua(x):
    if x == 0:
        return 1
    return x * giaiThua(x - 1)
  pr = (giaiThua(n)/(giaiThua(n-r+1)*giaiThua(r-1)))*pow(p,r)*pow((1-p),(n-r))
  return pr;


def infoMeasure(n,p,r):
     return(-math.log2(prob(n,p,r)));
print(infoMeasure(3,2,2))

def sumProb(n, p,r):
    i = n
    sum = 0
    while i > 0:
        sum = sum+prob(i, p, r)
        i=i-1
    return sum
'''
khi N tiến tới vô cùng thì sumProb(N,p) là tổng sác xuất tất cả các biến cố của phân phối nhị thức âm
giá trị này phải tiến tới 1
'''

def approxEntropy(n, p,r):
    i=n
    entropy=0
    while i > 0:
        entropy=entropy+prob(i, p, r)*infoMeasure(i, p, r)
        i=i-1
    return entropy

print(approxEntropy(100, 0.5,1))
