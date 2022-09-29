def nthHighestNumber(n, arr):
    if len(arr)-n >= len(arr)//2:
        for i in range(1, n):
            arr.remove(max(arr))
        return max(arr)
    else:
        for i in range(len(arr)-n):
            arr.remove(min(arr))
        return min(arr)



n = int(input())                    #nth highest number to find

#assuming array element input is given in single line with space seperation 
arr = list(map(int, input().strip().split(" ")))

print(nthHighestNumber(n, arr))