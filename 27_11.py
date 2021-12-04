a = dict()
b = dict()
c = dict()
y = []
y1 = []
y2 = []
while True:
    s = input().split()
    if len(s) == 0:
        break
    else:
        y.append(len(s[1]))
        a[s[0] + ' ' + s[1]] = int(s[2])
while True:
    s1 = input().split()
    if len(s1) == 0:
        break
    else:
        y1.append(len(s1[1]))
        b[s1[0] + ' ' + s1[1]] = int(s1[2])
while True:
    s2 = input().split()
    if len(s2) == 0:
        break
    else:
        y2.append(len(s2[1]))
        c[s2[0] + ' ' + s2[1]] = int(s2[2])
d = set(a.keys())
e = set(b.keys())
f = set(c.keys())
x = list(a)
x1 = list(b)
x2 = list(c)
print(len(f | e | d))
for i in range(1,len(a)+1):
    prn = str(i) + '_' + x[i-1][0] + '_' + str(y[i-1])
    print(prn)
for i in range(1,len(b)+1):
    prn = str(i) + '_' + x1[i-1][0] + '_' + str(y1[i-1])
    print(prn)
for i in range(1,len(c)+1):
    prn = str(i) + '_' + x2[i-1][0] + '_' + str(y2[i-1])
    print(prn)