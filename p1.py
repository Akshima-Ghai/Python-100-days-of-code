def fact(n):
    fact =1
    for i in range(1,n+1):
        fact = fact * i
    return fact

n = int(input())
r = int(input())
n_fact = fact(n)
r_fact = fact(r)
n_r_fact = fact(n-r)

nCr = n_fact//(r_fact*n_r_fact)
print(nCr)