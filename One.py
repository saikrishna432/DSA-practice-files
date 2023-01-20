

## GCD navie approach

def gcd1(m,n):
    if n>m:
        m,n=n,m
    fn=[]
    for i in range(1,n+1):
        if n%i==0:
            fn.append(i)
    fm=[]
    for i in range(1,m+1):
        if m%i==0:
            fm.append(i)
    cf=[]
    for f in fn:
        if f in fm:
            cf.append(f)
    #print(cf)
    return (cf[-1])

def gcd2(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if (m%i==0 & n%i==0):
            cf.append(i)
    return cf[-1]

def gcd3(m,n):
    l=min(m,n)
    i=l
    while i>0:
        if m%i==0 & n%i==0:
            return i
        else:
            i-=1   

print(gcd3(35,21))


## Euclid approach to find gcd

def gcd4(m,n):
    if n>m:
        m,n=n,m
    if m%n==0:
        return n
    return (gcd4(max(n,m-n),min(n,m-n)))



def gcd5(m,n):
    if n>m:
        m,n=n,m
    while m%n!=0:
        diff=m-n
        (m,n)=(max(n,diff),min(n,diff))
    return n

def gcd6(m,n):
    if n>m:
        m,n=n,m
    if m%n==0:
        return n
    return (gcd6(n,m%n))
    


print(gcd6(80,25))
    










