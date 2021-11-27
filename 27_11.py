a = dict()
b = dict()
c = dict()
while True:
    s = input().split()
    if len(s) == 0:
        break
    else:
        a[s[0] + ' ' + s[1]] = int(s[2])
while True:
    s1 = input().split()
    if len(s1) == 0:
        break
    else:
        b[s1[0] + ' ' + s1[1]] = int(s1[2])
while True:
    s2 = input().split()
    if len(s2) == 0:
        break
    else:
        c[s2[0] + ' ' + s2[1]] = int(s2[2])
d = set(a.keys())
e = set(b.keys())
f = set(c.keys())
x = list(a)
print(x[0][0])
'''for i in range(len(a)):
    prn = i + '_' + x[i][0] + '_' + len(x[i][])
    print(prn)
print(f | e | d)'''