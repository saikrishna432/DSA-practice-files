## Binary Search

def binarysearch(seq,v,l,r):
    if r-l==0:
        return False
    mid=(l+r)//2
    if seq[mid]==v:
        return True
    if (seq[mid]>v):
        return binarysearch(seq,v,l,mid)
    else:
        return binarysearch(seq,v,mid+1,r)
        



a=[1,32,4,20,111,15,20]
r=len(a)
v=5

print(binarysearch(a, v, 0,len(a)) ) 
    
## Eculidian method

def gcd(m,n) :
    if n>m:
        m,n=n,m
    if (m%n==0):
        return n
    else:
        return gcd(max(n,m%n),min(n,m%n))
    
print(gcd(75,100))


## Selection sort

def selectionsort(seq):
    
    for start in range(len(seq)):
        minpos=start
        for i in range(start,len(seq)):
            if seq[i]<seq[minpos]:
                minpos=i
        seq[start],seq[minpos]=seq[minpos],seq[start]
    return a

# print(selectionsort(a))
print(a)
def insertionsort(seq):
    for i in range(1,len(seq)):
        j=i-1
        while seq[i]<seq[j] and j>=0:
            seq[j],seq[i]=seq[i],seq[j]
            j=j-1
            i=i-1
    return seq
l=list(range(10,0,-1))
# print(insertionsort(l))          
        
def factorial(n):
    if n==0:
        return 1
    else:
        return n*(factorial(n-1))
              
print(factorial(10))
    
def sumlist(l):
    if l==[]:
        return 0
    else:
        return (l[0]+sumlist(l[1:]))
    
print(sumlist(l))

## Recersive insertive sort
print(l)
# def Recersive_insertion_sort(seq):
    
#     isort(seq,10)

# def isort(seq,k):
#     if k>1:
#         isort(seq,k-1)
#         insert(seq,k-1)

# def insert(seq,k):
#     pos=k
#     while pos>0 and seq[pos]<seq[pos-1]:
#         (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
#         pos=pos-1

# print(Recersive_insertion_sort(l)) 


def mergesort(l):
    n=len(l)
    a=l[0:n//2]
    b=l[n//2:]
    c=[]
    if len(a)==0:
        return c.extend(b)
    if len(b)==0:
        return c.extend(a)
    if len(a)==1 and len(b)==0:
        if a[0]>b[0]:
            return (c=b[0]+a[0])
        else:
            return (c=a[0]+b[0])
    else:
        
        
        
    
    
    
    
    


