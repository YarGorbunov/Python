def func1(l1,l2): return len(set(l1).intersection(set(l2)))

l1 = input().split()
l2 = input().split()
print(func1(l1,l2))