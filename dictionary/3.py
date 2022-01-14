#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program adds all the items of a dictionary.
numerics = {
    'w': 475.237,
    'x': -324.297,
    'y': 958.421,
    'z': -109.361
    }
for key, values in numerics.items():
    print(key+" =", values)
print("---------------")
print("  =",'%.3f'%sum(numerics.values()))