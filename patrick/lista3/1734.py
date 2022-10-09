# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

M = int(input())
N = M
X = 1
while(N > 1):
    X = X*N
    N = N-1
    
print("%i! = %i" %(M, X))

