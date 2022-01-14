#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program merges two Python dictionaries.
dict1 = {
    'name': 'example',
    'email': 'example@gmail.com',
    'location': 'somewhere on earth', 
    }
dict2 = {
    'employed': True,
    'id': 123456,
    'salary': '$40K'
    }
print(dict1.copy())
print(dict2.copy())
dict1.update(dict2)
print("\n",dict1.copy())
