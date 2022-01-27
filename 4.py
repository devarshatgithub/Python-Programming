#   Id:20CE014_Contractor_Devarsh,
#   Batch:CE-1, CSPIT

# About: Program finds runner-up from given list
size = int(input())
runner_ups = list(map(int, input().split()))
print(sorted(list(set(runner_ups)))[-2])    # prints second-last runner-up from the list