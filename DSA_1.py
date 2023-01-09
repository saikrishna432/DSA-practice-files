

# Prints sums of all subsets of array
def subsetSums(arr, n):
    # There are total 2^n subsets
    total = 1 << n
    print(total)
 
    # Consider all numbers from 0 to 2^n - 1
    for i in range(total):
       Sum = 0
 
       # Consider binary representation of
       # current i to decide which elements
       # to pick.
       for j in range(n):
          if ((i & (1 << j)) != 0):
              Sum += arr[j]
 
       # Print sum of picked elements.
       print(Sum, "", end = "")
 
# arr = [ 5, 4, 3,5]
# n = len(arr)
 
# subsetSums(arr, n)



##search an element in 4x4 matrix

mat = [[10, 20, 30, 40], [15, 25, 35, 45],
           [27, 29, 37, 48], [32, 33, 39, 50]]

def searchinmatrix(mat,n,x):
    if n==0:
        return-1
    for i in range(n):
        for j in range(n):
            if mat[i][j]==x:
                # print("Elements are in",i,"th row and",j,"th column")
                return 1
    print("Element was not found")
    return(0)

a=searchinmatrix(mat,4,39)
# print(a)


##sum of all sub sets in a array

# def sumoflist(l,n):
#     sumlist=0
#     if n==0:
#         return("List is empty")
#     total=1<<n
#     for i in range(total):
#         for j in range(n):
#             if((i &(1<<j))!=0):
#                 sumlist += l[1]
#     print(sumlist, "",end= "")
    
    
# s=[2,5,6]
# q=sumoflist(a,3)
# print(q)
            
s="brown fox graw dog brown fox"
s=s.replace("brown","black")

print(s)


date = "16"
month="08"
year="2016"
today='-'.join([date,month,year])
print(today)


s=s.capitalize()
print(s)

s=s.lower()
print(s)

s=s.upper()
print(s)

s=s.title()
print(s)

s=s.swapcase()
print(s)

# s=s.center(50)
# print(s)

# s=s.center(s,"-")
# print(s)

a="Hello"
# a=a.center(40)
# print(a)

# a=a.center(50,'-')
# print(a)

# a=a.rjust(50,'-')
# print(a)


b=a.isalpha()
print(b)

c=a.isnumeric()
print(c)

z="One: {f}, two: {s}".format(f=47,s=11)
print(z)

a="Frist:{1}, second:{0}".format(47,11)
print(a)

g="Value:{0:3d}".format(4)
print(g)

h="Value:{0:6.2f}".format(47.523)
print(h)

l=list(range(10))
del(l[4])
print(l)








                 