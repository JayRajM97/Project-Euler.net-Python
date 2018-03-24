#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

mini=100
maxo=999
mul=0
arr=[]
for i in range(mini,maxo+1):
    for j in range(mini,maxo+1):
        mul=i*j
        rev=int(str(mul)[::-1])
        if(mul==rev):
            arr.append(mul)
print(max(arr))

#Answer: 906609
