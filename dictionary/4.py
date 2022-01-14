#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program adds key and its value to predefined dictionary.
dictionary = {
    'name': 'example',
    'email': 'example@gmail.com',
    'division': 1
    }
while (True):
    key = input("ADD Key_Name: ")
    value = input(">   Key_Value: ")
    if (key == ""):
        print(dictionary.copy(),"\n\texiting ...")
        break;
    dictionary.update({key: value})
    print(dictionary.copy(),"\n")