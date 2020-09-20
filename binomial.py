import math

def prob(n,p,N):
  def giaiThua(x):
    if x == 0:
        return 1
    return x * giaiThua(x - 1)
  pr = (giaiThua(N)/(giaiThua(n)*giaiThua(N-n)))*pow(p,n)*pow((1-p),(N-n))
  return pr;

def infoMeasure(n,p,N):
     return(-math.log2(prob(n,p,N)));

def sumProb(N, p):
    i = N
    sum = 0
    while i > 0:
        sum = sum+prob(i, p, N)
        i=i-1
    return sum

'''
khi N tiến tới vô cùng thì sumProb(N,p) là tổng sác xuất tất cả các biến cố của phân phối nhị thức
giá trị này phải tiến tới 1
'''
def approxEntropy(N, p):
    i=N
    ent=0
    while i > 0:
        ent=ent+prob(i, p, N)*infoMeasure(i, p, N)
        i=i-1
    return ent
print(approxEntropy(100, 0.5))
