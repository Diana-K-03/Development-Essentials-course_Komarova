from module1 import find_two_smallest
from module2 import list_a, list_b, list_c, list_d

res1 = find_two_smallest(list_a)
res2 = find_two_smallest(list_b)
res3 = find_two_smallest(list_c)
res4 = find_two_smallest(list_d)

f = open("result.txt", "w")

print("list_a:", res1, file=f)
print("list_b:", res2, file=f)
print("list_c:", res3, file=f)
print("list_d:", res4, file=f)

f.close()