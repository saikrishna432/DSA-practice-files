
from timeit import default_timer as timer

start=timer()

a1=input().strip()
b1=input().strip()
a=b=0
for i in range(len(a1)):
    if a1[i]<="9"and a1[i]>="0":
        a=a*10+i
for i in range(len(a1)):
    if b1[i]<="9"and b1[i]>="0":
        b=b*10+i
    
print(a,b)

def solution(a, b):
    c1=c2=c3=c4=c5=c6=0
    for i in range(int(a)):
        if (i*(i+1)/2)<=a:
            continue
        else:
            c1=i
            break
    for i in range(int(b)):
        if (i*(i+1)/2)<=a:
            continue
        else:
            c2=i
            break
    for i in range(a+b+1):
        if i%2==0:
            if a>0:
                a-=i
                c3+=1
        else:
            if b>0:
                b-=i
                c4+=1      
    for i in range(a+b+1):
        if i%2==0:
            if b>0:
                b-=i
                c5+=1
        else:


# x = 10
# y = 50
 
# # Swapping using xor
# x = x ^ y
# print(x)
# y = x ^ y
# print(y)
# x = x ^ y
# print(x)
 
# print("Value of x:", x)
# print("Value of y:", y)

# n=3

# def tower(n,a,b,c):
#     if n==1:
#         print("move",n,"disk from",a,"to",c,end=".\n")
#     else:
#         tower(n-1,a,c,b)
#         print("move",n,"disk from",a,"to",c,".")
#         tower(n-1,b,a,c)
    
# tower(3,"a","b","c")       
        
# end=timer()
    
# print(end-start)
string="Platform"
s='t' in string
print(s)