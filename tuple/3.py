#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program adds items in predefined tuple.
newTup = (
    'CRUD',
    14,
    20.22,
)
while (True):
    add = input("ADD item to Tuple: ")
    if (add == ""):
        print(newTup,"\n\texiting ...")
        break;
    temp = list(newTup)
    temp.append(add)
    newTup = tuple(temp)
    print(newTup)