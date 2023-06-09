'''Given 2 sets of integers, M and N, print their symmetric difference in ascending
order. The term symmetric difference indicates those values that exist in either
M or N but do not exist in both.
'''

n = int(input("enter:"))
set1 = set(map(int, input("enter:").split()))

m = int(input("enter:"))
set2 = set(map(int, input("enter:").split()))

ans = list(set1 ^ set2)
ans.sort()
for i in ans:
    print(i)

