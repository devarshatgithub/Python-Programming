#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program checks whether a given key already exists in a dictionary.
newDictionary = {
    'name': 'example',
    'email': 'example@gmail.com',
    'division': 1
    }
while (True):
    getKey = str(input("Search for KEY: "))
    if (getKey == ""):
        print("\texiting ...")
        break;
    if getKey in newDictionary.keys():
        print(getKey," exists,")
        print(getKey,":",newDictionary[getKey],"\n")
    else:
        print(getKey+" doesn\'t exists.\n")