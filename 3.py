#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program finds Captain Room Number from given list
recurring = int(input())                    # number of rooms with same room numbers
rooms = list(map(int, input().split()))     # rooom numbers in list

for i in range(len(rooms)):
    # checks non-repeative room numbers for the 'Captain`s Room Number'
    if (rooms.count(i) != recurring and rooms.count(i) != 0):
        print(i)