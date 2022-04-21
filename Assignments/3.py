def maxVol(values):
    a = 0
    for i in range(len(values)):
        for j in range(i+1,len(values)):
            a = max(a,min(values[j],values[i])*(j-i))
    return a
heights = list(map(int,input().split()))
maxVol(heights)