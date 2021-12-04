def f():
    b = dict()
    while True:
        s1 = input().split()
        if len(s1) == 0:
            break
        else:
            b[s1[0] + ' ' + s1[1]] = int(s1[2])
    return b


k = int(input())
a = []
_set = set()
x = set()
for i in range(k):
    a.append(f())
    x.update(set(a[i].keys()))

for i in range(k):
    for items in a[i].keys():
        _set.add(items)
for t in a:
    print(t)

print(len(_set))
print(x)

