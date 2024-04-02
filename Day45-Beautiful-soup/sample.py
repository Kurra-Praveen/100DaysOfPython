# a = [[0, 0, 1], [4, 3, 7], [1, 0, 3]]
x = []
n = int(input("enter "))
for i in range(n):
    q = []
    for _ in range(n):
        q.append(int(input()))
    x .append(q)
b = []
for each_matrix in x:
    s_m = 0
    count = 0
    for i in each_matrix:
        if i > 0:
            count += 1
        s_m += i
    strength = s_m % (1 + count)
    b.append(strength)
b.sort()
print(b)
