#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program finds the most common elements and their counts from list, tuple, dictionary.
lt = [45, 54.65, 32, 65.6, 45, 84.3, 32, 654, 54.65, -32.4, 32, 24.05, 89, -374]
tup = (45, 54.65, 32, 65.6, 45, 84.3, 32, 654, 54.65, -32.4, 32, 24.05, 89, -374)
dic = {45, 54.65, 32, 65.6, 45, 84.3, 32, 654, 54.65, -32.4, 32, 24.05, 89, -374}
print(lt)
print(tup)
print(dic)
print("Number of '32' present in the list:",lt.count(32))       # counts number of times the specific member exist in list
print("Number of '32' present in the tuple:",tup.count(32))     # counts number of times the specific member exist in tup
print("'32' is Present in dictionary? :",32 in dic)               # set and dictionary restricts duplication of members,
                                                                # as they has one and only one identity member(element)