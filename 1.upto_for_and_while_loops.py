
# iuaerbdskfe     can be done by countrol+1
# e;orirnrf
# ;urbrkdn
# laeuigdb
# ];uwrsbdn
# d=101010
# e=type(d)
# print(e)
# print(d)

print("""Hellow \" world""")

i=6+5j
print(i)

m=5
n=10

def gcda(m,n):
    fm=[]
    for i in range(1,m+1):
        if(m%i)==0:
            fm.append(i)
    fn=[]
    for i in range(1,n+1):
        if(n%i)==0:
            fn.append(i)
    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)
    return(cf[-1])

y=gcda(10000,2000)

print(y)
            
    

def gcd(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            cf.append(i)
    return(cf[-1])

#y=gcd(10,20)
#print(y)

def gcd2(m,n):
    i=min(m,n)
    while i>0:
        if (m%i)==0 and (n%i)==0:
            return(i)
        else:
            i=i-1
        
#x= gcd2(25,45)
#print(x)

def gcd3(m,n):
    if m<n:
        (m,n)=(n,m)
    if(m%n)==0:
        return(n)
    else:
        diff=m-n
    return(gcd3(max(diff,n),min(diff,n)))    

#z=gcd3(45,80)
#print(z)

def gcd4(m,n):
    if m<n:
        (m,n)=(n,m)
    while (m%n)!= 0:
        diff =m-n
        (m,n)= (max(n,diff),min(n,diff))
    return(n)

#t=gcd4(20,30)
#print(t)


def gcd5(m,n):
    if m<n:
        (m,n)=(n,m)
    if(m%n)==0:
        return(n)
    else:
        return(gcd(n,m%n))

#v=gcd5(2000000000,65000000)
#print(v)

def gcd6(m,n):
    if m<n:
        (m,n)=(n,m)
    while (m%n)!=0:
        (m,n)=(n,m%n)
    return(n)

#m=gcd6(30000,450)
#print(m)

s=7**1
r=int(s)
#print(s)

def divides(m,n):
    if n%m==0:
        return(True)
    else:
        return(False)
def even(n):
    return(divides(2,n))
def odd(n):
    return(not divides(2,n))

#t=divides(2,32)
#print(t)


def torf(m,n):
    if m%n:
        return(True)
    else:
        return(False)
#y= torf(6,8)
#print(y)

def power(x,n):
    ans=1
    for i in range(0,n):
        ans=ans*x
    return(ans)

#y=power(5,7)
#print(y)

def power2(x,n):
    i=0
    ans=1
    while i<n:
        ans=ans*x
        i=i+1
    return(ans)

#z=power2(5,7)
#print(z)

def update(l,i,v):
    if(i>0 and i<len(l)):
        l[i]=v
        return(True)
    else:
        v=v+1
        return(False)
    
#ns =[3,11,12]
z=8
#res= update(ns,2,z)
#print(res)

def factorial(n):
    val=1
    for n in range(1,n+1):
        val=val*n
    return(val)

#y=factorial(5)
#print(y)

def factorial2(n):
    if n<=0:
        return(1)
    else:
        val=n*factorial2(n-1)
        return(val)

    
#s=factorial2(4)
#print(s)
    
def factors(n):
    fn=[]
    for i in range(1,n+1):
        if(n%i)==0:
            fn.append(i)
    return(fn)

#j=factors(1)
#print(j)

def isprime(n):
    if factors(n)==[1,n]:
        return(True)
    else:
        return(False)


def isprime2(n):
    return(factors(n)==[1,n])

#a= isprime2(1)
#print(a)

def primesupto(n):
    primelist=[]
    for i in range(2,n+1):
        if isprime(i)==True:
            primelist.append(i)
    return(primelist)

#r=primesupto(100)
#print(r)

def first_n_primes(n):
    (count,i,plist)=(0,1,[])
    while count<n:
        if isprime(i)==True:
            count=count+1 
            plist.append(i)
        i=i+1
    return(count,i,plist)

#n=first_n_primes(10)
#print(n)
fi=[]
for i in range(12,1,-1):
    fi.append(i)
#print(fi)

y=list(range(0,5))
#print(y)

z=list(range(0,5))==[0, 1, 2, 3, 4]
#print(z)

list1=[1,3,5,7]
list2=[6,8,0,2]
list1.append(list2[2])
print(list1)
list1.extend(list2)
print(list1)





















    
        
        









        
    
        

    




    
    























        



        