s="malm"

def minDeletions(str):
    n=len(str)
    f=[0]*26
    c=[]
    for i in range(n):
        
        f[ord(str[i])-ord("a")]+=1
    
    for j in range(26):
        c.append(f[j]%2)
    
    sum_extra=sum(c)
    
    if sum_extra==0 or sum_extra==1:
        return 0
    return sum_extra-1
        
print(minDeletions(s))       

def mincutstr(s):
    l=len(s)
    if minDeletions(s)==0:
        return 0
    
    a=[]
    b=[]
    
    for i in range(l):
        for j in range(i+1,l+1):
            a.append(s[i:j])
            e=s[0:i]+s[j:]
            if minDeletions(e)==0:
                b.append(len(e))
    t=max(b)
    return l-t
    
print(mincutstr(s))            
            




# Python3 program for
# the above approach
 
# Function to find the number of deletions
# required such that characters of the
# string can be rearranged to form a palindrome
def minDeletions(str):
     
    # Stores frequency of characters
    fre = [0]*26
     
    # memset(fre, 0, sizeof(fre));
    n = len(str)
 
    # Store the frequency of each
    # character in frequency array
    for i in range(n):
        fre[ord(str[i]) - ord('a')] += 1
 
    count = 0
 
    # Count number of characters
    # with odd frequency
    for i in range(26):
        if (fre[i] % 2):
            count += 1
 
    # If count is 1 or 0, return 0
    if (count == 0 or count == 1):
        return 0
 
    # Otherwise, return count - 1
    else:
        return count - 1
 
# # Driver Code
# if __name__ == '__main__':
#     str = "ababbccca"
 
#     # Function call to find minimum
#     # number of deletions required
#     print (minDeletions(str))
    
    
    
    
s="malay"

def cutstr(s):
    
    l=len(s)
    res=[]
    check=[]
    v=[]
    
    e=minDeletions(s)
    if e==0:
        return 0
    
    lth=[]
    for i in range(l):
        for j in range(i+1,l+1):
            res.append(s[i:j])
            a=s[0:i]+s[j:]
                       
            e=minDeletions(a)
            if e==0:
                check.append(a)
                lth.append(len(a))
                v.append(e)
            print(i,j)
            
            
    print(res)
    print(check)  
    print(v)
    print(lth)
    return(max(lth))
    

print(cutstr(s))       
        
        
        
        
        
        
        
        
    