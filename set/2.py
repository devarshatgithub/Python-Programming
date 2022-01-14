#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program removes items from a set if it is present in the set.
newSet = {
    'name',
    'email',
    'email',
    'userid',
    'phone',
    'location',
    'hobbies'
    }
while (True):
    rd = input("Remove element from Set: ")
    if (rd == ""):
        print(newSet,"\n\texiting ...")
        break;
    # we can even use remove() method,
    # as it's throws error if element does not exist in the set.    
    newSet.discard(rd)
    print(newSet)