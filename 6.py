#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program finds distinct number of word from the input array
ls = []
diy = {}
t = int(input())
while (t!=0):
    arr = input()
    ls.append(arr)
    t-=1
print(len(dict.fromkeys(ls)))
for i in range(len(ls)):
    diy.update({ls[i]:ls.count(ls[i])})
for ls in diy:
    print(diy.get(ls))