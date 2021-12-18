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
print(len(f | e | d)) #1 задание
print()
prn = []
prn1 = []
prn2 = []
for i in range(1,len(a)+1):
    prn.append(str(i) + '_' + x[i-1][0] + '_' + str(y[i-1]))
print(*prn)
for i in range(1,len(b)+1):
    prn1.append(str(i) + '_' + x1[i-1][0] + '_' + str(y1[i-1]))
print(*prn1)
for i in range(1,len(c)+1):
    prn2.append(str(i) + '_' + x2[i-1][0] + '_' + str(y2[i-1]))
print(*prn2) #2 задание
print()
st = []
for i in x:
    if i in x1:
        if i in x2:
            st.append(i)
print(*st) #3 задание
n = 0
n1 = ''
for name in st:
    if n < (a[name] + b[name] + c[name]) :
        n = a[name] + b[name] + c[name]
        n1 = name
print(n1) #3 задание
print()
m = 0
for i in x:
    m = 1
    if i in x1:
        m = m + 1
        if i in x2:
            m = m + 1
    elif i in x2:
        m = m + 1
    print(i + ' ' + str(m)) #4 задание
for i in x1:
    if not (i in x):
        m = 1
        if i in x2:
            m = m + 1
        print(i + ' ' + str(m)) #4 задание
for i in x2:
    if not (i in x1) and not (i in x):
        print(i + ' ' + '1') #4 задание
