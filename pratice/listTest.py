list1 = [[1,2],[3,4],[5,6]]
print(list1)

i = 5
j = 3
k = 2

list2 = [[[0 for _ in range(i)] for _ in range(j)] for _ in range(k)]

value = 0

for x in range(k):
    for y in range(j):
        for z in range(i):
            list2[x][y][z] = value
            value += 1

print(list2)