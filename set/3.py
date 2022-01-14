#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program prints an intersection, Union, difference and symmetric difference of sets.
set1 = {
    'math',
    'physics',
    'chemistry',
    'biology',
    'english',
    'hindi',
    'computer'
    }
set2 = {
    'accounts',
    'stats',
    'business studies',
    'economic',
    'english',
    'hindi',
    'computer'
    }
print("A =",set1)
print("B =",set2)
print("\nAuB =",set1.union(set2))                           # union of both the sets
print("AnB =",set1.intersection(set2))                      # intersection from both the sets
print("A-B =",set1.difference(set2))                        # difference = A - AnB
print("B-A =",set2.difference(set1))                        #            = B - AnB
print("A"+chr(916)+"B =",set1.symmetric_difference(set2))   # symmetric difference = AuB - AnB