from statistics import *
data = list(map(int,input().split()))
print(min(data),max(data),mean(data),stdev(data),variance(data))