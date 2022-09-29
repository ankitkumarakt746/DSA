def singleMissingElement(n, arr):       #Will work on both ordered or unordered array elements
    return int(n*(n+1)/2-sum(arr))      #Using formula for sum of first n natural numbers i.e. n*(n+1)/2

def moreThanOneMissing(s, arr):
    miss = s-len(arr)
    return set(range(1, s+1))-set(arr)  #Using the concept of sets


#total expected size of array
n = int(input())

#assuming array element input is given in single line with space seperation 
arr = list(map(int, input().strip().split(" ")))

#print(singleMissingElement(n, arr))
print(moreThanOneMissing(n, arr))