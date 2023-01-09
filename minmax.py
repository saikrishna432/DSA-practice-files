
# tuples
a=(2,5,6,40)
b=(20,50,45,60)
c=(2,5,6,40)+(20,50,45,60)
#print(c)

#get minimum and maximum with minimum comparision

def maxmin(l):
    n=len(l)
    if n%2==0:
        max_arr=max(l[0],l[1])
        min_arr=min(l[0],l[1])
        i=2
    else:
        max_arr=min_arr=l[0]
        i=1
    while (i<n-1):
        if l[i]<l[i+1]:
            max_arr=max(max_arr,l[i+1])
            min_arr=min(min_arr,l[i])
        else:
            max_arr=max(max_arr,l[i])
            min_arr=min(min_arr,l[i+1])
        i =i+2
    return(max_arr,min_arr)

h=[25,32,45,85,65,47,53]
a=maxmin(h)
#print(a)


#reverse the list

def reverselist(l):
    return(l[::-1])

d=[2,5,65,75,98,99,45,32]
a=reverselist(d)
#print(a)
#print(d[4:])

nums=[-2,1,-3]


# max of sublist

def maxSubArray(nums) -> int:
    max_sum=nums[0]
    sum_sublist=nums[0]
    for i in range(0,len(nums)):
        max_sum=max(max_sum,sum_sublist)
        sum_sublist=nums[i]
        sub_max=nums[i]
        for j in range(i,len(nums)):
            sum_sublist=sum_sublist+nums[j]
            sub_max=max(sub_max,sum_sublist)
    return(max_sum)


a=maxSubArray(nums)
#print(a)


#dublicats are available

def containsdublicate(l):
    count=0
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            if l[i]==l[j] and i!=j:
                count=count+1   
    if count==0:
        return(False)
    else:
        return(True)

s=[3,1]
#print(sorted(s))
b=set(s)
#print(b)
c=list(b)
#print(sorted(c))

# if (s==b):
#     print("yes")



def containsdublicate2(l):
    b=list(set(l))
    if (l==b):
        return(False)
    else:
        return(True)
        
s=[3,1]
e=containsdublicate2(s)
#print(e)



def containsNearbyDuplicate(nums:[int], k: int) -> bool:
    n=len(nums)
    count=0
    for i in range (0,n):
        for j in range (i+1,n):
            if (nums[i]==nums[j]):
                if (abs(i-j)<=k):
                    count=count+1
                    print(count)
                    print(i,j,k)
                
    if count==0:
        return(False)
    else:
        return(True)
        
s=[1,2,3,1,2,3]
w=containsNearbyDuplicate(s,2)
print(w)

# def isPalindrome(s: str) -> bool:
#     s1=s.lower()
#     s2=s1.isalnum()
#     s3=s2[::-1]
#     if(s2==s3):
#         return(True)
#     else:
#         return(False)
    
a= "A man, a plan, a canal: Panama"
a="0P"
s1=a.lower()

#s =''.join(filter(str.isalnum, s1))
print(s)
# b=list(a)
# print(b)
# c=b[::-1]




class student:
    height="6ft"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def talk(self):
        return "Hi"
        
a=student("sai","27")
b=student("dipanjan","25")

# print(b.height)
# print(b.talk())
# print(a.age)
# print(a.name)

s="()"


def isValid(s: str) -> bool:
    for x in range(len(s)):
        if s[x]=='(':
            if s[x+1]==')':
                x=x+2
            else:
                return False  
        elif s[x]=='{':
            if s[x+1]=='}':
                x=x+2
            else:
                return False
        elif s[x]=='[':
            if s[x+1]== ']':
                x=x+2
            else:
                return False
    print(True)

v=isValid(s)


def f():
    y=x
    print(y)
    x=22
    
x=7
print(f())

def isPalindrome(s: str) -> bool:
    s=isalnumnum(s)
    s =''.join(filter(str.isalnum, s))
    s1=list(a)
    s2=s1[::-1]
    if(s1==s2):
        return(True)
    else:
        return(False)
        
k=isPalindrome(a)
print(k)





