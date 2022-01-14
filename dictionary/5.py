#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program concatenates following dictionaries.
dic1 = {
    1: 10,
    2: 20
    }
dic2 = {
    3: 30,
    4: 40
    }
dic3 = {
    5: 50,
    6: 60
}
print(dic1.copy())
print(dic2.copy())
print(dic3.copy())
dic2.update(dic3)
dic1.update(dic2)
print("After concatenation:\n",dic1.copy())