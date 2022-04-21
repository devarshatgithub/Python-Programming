from itertools import *
def cntCombinations(arr,k):
    cnt = 0
    for i in range(len(arr)):
        for C in combinations(arr, i):
            if sum(C) == k:
                cnt+=1
    return cnt
array = list(map(int,input().split()))
K = int(input())
cntCombinations(array,K)