import re
def verschieben(v,c):
    for i in range(v):
        c.append(c[0])
        c.pop(0)
    return c
def key(ini,i):


    cd = re.findall("............", ini)
    c = re.findall(".", cd[0])
    d = re.findall(".", cd[1])
    if i == 0 or i == 2:
        v = 4
    else:
        if i == 1 or i == 3:
            v = 2
    print("Verschoben um", str(v) + ":")
    c = verschieben(v, c)
    d = verschieben(v, d)
    g = "".join(str(c) + str(d))
    ges = ''.join(c for c in g if c.isnumeric())
    print(ges)
    e = [d[9], d[6], c[4], d[2], c[9], c[5], c[2], d[8], d[3], c[8], c[3], d[7], c[11],
         d[10], c[7], c[0], d[5], d[0]]
    r = "".join(str(e))
    key = ''.join(c for c in r if c.isnumeric())
    print("k" + str(i + 1) + ":", key)
    key = hex(int(key, 2))
    print("k" + str(i + 1) + ":", key)
    for x in range(len(d)):
        c.append(d[x])
    cd = "".join(str(c))
    cd = ''.join(c for c in cd if c.isnumeric())
    return key,cd
in1="c92b57"
ini=in1
print("k0:",in1)
ini = str(bin(int(ini, 16)))
Void, ini = ini.split("b", 1)
while len(ini) < 24:
    ini = "0" + ini
r=[]
for i in range(4):
    k,ini = key(ini,i)
    r.append(k)
print("k0-k4:",r)
input()

