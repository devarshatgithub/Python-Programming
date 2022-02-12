#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program check for lapindrome string from the input strings
ls = []
def lapindrome(B,E):
    beg = ls[i][:B]
    end = ls[i][E:]
    rend = end[::-1]
    if beg == end or beg == rend:
        print('YES')
    else:
        print('NO')
t = int(input())
while (t!=0):
    st = input()
    ls.append(st)
    t-=1
for i in range(len(ls)):
    s = len(ls[i])//2
    if len(ls[i])%2 != 0:
        lapindrome(s, s+1)
    else:
        lapindrome(s, s)
