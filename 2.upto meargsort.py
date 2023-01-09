list1=[1,3,5,7]
list2=list1
 
#y= list1==list2
#print(y)
z= list1 is list2
#print(z)

list3=list2[:]
#print(list3)
a= list1==list3
#print(a)
b= list1 is list3
#print(b)

list7=[2,4,6,8]
list8=[1,3,5,7]
#list7.append(list8)  #check it intresting
list7.extend(list8)


list7.remove(2)
#print(list7)

list7= list7+list8
#print(list7)

while 3 in list7:
    list7.remove(3)

#print(list7)

list7.reverse()
#print(list7)

list7.sort()
#print(list7)

#print(list7)
e=list7.index(8)
#print(e)

#z=list7.rindex(4)
#print(z)
list10=[5,2,7,6,4]
#print(list10)

#Binary search for sorted list


def bsearch(seq,v,l,r):
    if r-l==0:
        return(False)
    mid=(l+r)//2
    if v==seq[mid]:
        return(True)
    if (v<seq[mid]):
        return(bsearch(seq,v,l,mid))
    else:
        return(bsearch(seq,v,mid,r))
    
#seq1=list(range(0,500,1))
#print(seq1)
    
#d=bsearch(seq1,75,1,495)
#print(d)

def selectionsort(l):
    for i in range(0,len(l)):
        for k in range(i,len(l)):
            if(l[i]>=l[k]):
                (l[i],l[k])=(l[k],l[i])


            
def insertionsort(seq):
    for i in range(len(seq)):
        pos=i
        print(pos)
        print(seq)
        while pos>0 and seq[pos]<seq[pos-1]:
            (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
            pos=pos-1
            
            
#e=list(range(1000,1,-50))
#print(e)
#insertionsort(e)
#print(e)        
    
def factorial(n):
    if n==0:
        return(1)
    if n>0:
        return(n*factorial(n-1))
    
#print(factorial(5))

def multiply(m,n):
    if n==1:
        return(m)
    else:
        return(m+multiply(m,n-1))

#print(multiply(5,7))


def sumlist(l):
    if l==[]:
        return(0)
    else:
        return(l[0]+l[1:])

#e=list(range(1000,1,-50))
#print(e)
#s=sum(e)
#print(s)


import sys
sys.setrecursionlimit(10000)


def merge(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)
    while i+j<m+n:
        if i==m:
            C.append(B[j])
            j=j+1
        elif j==n:
            C.append(A[i])
            i=i+1
        elif A[i]<=B[j]:
            C.append(A[i])
            i=i+1
        elif A[i]>B[j]:
            C.append(B[j])
            j=j+1
    return (C)
            
#a=list(range(0,30,2))
#print(a)
#b=list(range(1,40,2))
#print(b)
a=[1,3,5,5,7,9]
b=[2,4,5,5,8,10]

#print("here is the merged list")
#c=merge(a,b)
#print(c)  


def mergesort(A,left,right):
    if right-left <=1:
        #print[A[left:right]]
        return(A[left:right])
    
    if right-left>1:
        mid=(left+right)//2
        L=mergesort(A,left,mid)
        #print(L)
        R=mergesort(A,mid,right)
        #print(R)
        w=merge(L,R)
        return(w)
  
    
v=list(range(1,10,2))+list(range(0,10,2))
w=mergesort(v,0,len(v))
#print(w)


def quicksort(A,l,r):
    if r-l<=1:
        return()
    yellow=l+1
    for green in range(l+1,r):
        if A[green]<=A[l]:
            (A[green],A[yellow])=(A[yellow],A[green])
            yellow=yellow+1
    (A[l],A[yellow-1])=(A[yellow-1],A[l])
    
    quicksort(A,l,yellow-1)
    quicksort(A,yellow,r)
    return(A)
    
a=list(range(500,0,-1))
#print(a)
#q=quicksort(a,0,len(a))
#print(q)
        
import random

# def randomize(l):
#     n=len(l)
#     for i in range(len(l)//2):
#         j=random.randrange(0,n,l)
#         k=random.randrange(0,n,l)
#         (l[j],l[k])=(l[k],l[j])

a=list(range(500,0,-1))
# w=randomize(a)
# print(w)


###Dictonaries

score={}
score["Test1"]={}
score["Test2"]={}
score["Test1"]["Dhawan"]=76
score["Test2"]["Dhawan"]=27
score["Test1"]["Kohili"]=200

#print(score)

#print(score.keys())

d={}
for l in "aergdfraerd":
    d[l]=l

#print(d.keys())

l=[1,2,3]
n=3

dct={}
new_l= l[:]
for i in range(1,n+1):
    for j in range(len(l)):
        new_l[j]=new_l[j]+1
    dct[i]=new_l[:]
        
        
#print(dct)   


lst=[]
#n=int(input("Enter no of elements:"))

# for i in range(n):
#     ele= int(input())
#     lst.append(ele)
#print(lst)


def  select(property,l):
    sublist=[]
    for x in l:
        if property(x):
            sublist.append(x)
    return(sublist)

a=[5,6,7,8,-1,6,-25]

y=select(property,a)
print(y)


def square(x):
    return(x*x)

def iseven(x):
    return(x%2==0)

#a=list(map(square,filter(iseven,range(100))))

#print(a)

"""a= [(x,y,z) for x in range(100)
                for y in range(100)
                    for z in range(100)
                        if x*x+y*y==z*z]"""
    
t=[[0 for i in range(3)] for j in range(4)]
print(t)

zerolist = [0 for i in range(3)]
# print(zerolist)
k=[zerolist for j in range(4)]
#print(k)
k[1][1]=7
#print(k)

#y={(x,y,z)| 1<=x,y,z<=n, x*x+y*y=z*z}


# q=[square(i) for i in range(100) if iseven(i)]
# print(q)


# while(True):
#     try:
#         userdata = input("Enter a number:")
#         usernum = int(userdata)
#     except ValueError:
#         print("Not a number. Try again")
#     else:
#         break
   
# print(userdata)

(x,y)=(1,2)
# print("values are x:",x,"y:",y)


# print("Continue on the", end="...")
# print("one line", end=",\n")
# print("next line")        

# (x,y)=(7,10)
# print("x is ",x," and y is ",y,".",sep="")


# n= int(input().strip())
# print(n)

#arr= list(map(int,input().rstrip().split()))
# a=arr[::-1]
# for i in range(0,len(a)):
#     print(a[i],end=" ")
      







        














          
            
    
    
    




            











     

    