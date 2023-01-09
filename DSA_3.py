a=[11,13,21,3]
l=len(a)

def printNGD(a,l):
    
    for i in range(l):
        next=-1
        for j in range(i+1,l):
            if a[i]<a[j]:
                next=a[j]
                break
        print(a[i]," -- ",next)
        
        
        
#
s1="aabca"
s2="acaba"

def areanagaram(s1,s2):
    if len(s1)!=len(s2):
        return False
    count=[0]*256
    for i in range (len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= -1
    for x in count:
        if x!=0:
            return False
    return True



s=[20,20,18]
a=s[0]
b=0           
for i in range(1,len(s)):
    if a<s[i]:
        b=a
        a=s[i]
# s=[5,4,7,8,1]        
print(b)
a=len(s)

if a%2==0:
    l=a/2
if a%2!=0:
    l=(a//2)+1
# print(l)
for i in range(int(l)):
    # print(s[i],s[a-i-1])
    s[i],s[a-i-1]=s[a-i-1],s[i]
    
# print(s)


s=[5,4,7,8,1]  
for i in range (0,len(s)-1):
    s[i],s[i+1]=s[i+1],s[i]

# print(s)
    
def minimumCost(n: int, x: list[int]) -> int:
    meet=(n//2)
    count=0
    
    if x[meet]%2!=0:
        for i in range(len(x)):
            if x[i]%2==0:
                count += 1
    if x[meet]%2==0:
        for i in range(len(x)):
            if x[i]%2!=0:
                count += 1
    return count

t=int(input())
for j in range(t):
    n=int(input())
    # x=[]
    x=list(map(int,input().split(" ")))
    y=minimumCost(n,x)
    print(y)
    #print(y)

