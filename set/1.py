#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program adds elements in a set and clear a set
newSet = {
    'collection',
    2,
    1.1,
    range(9),
    }
while (True):
    add = input("ADD elements to Set: ")
    if (add == ""):
        newSet.clear()
        print(newSet,"Set is cleared\n\texiting ...")
        break;
    newSet.add(add)
    print(newSet)