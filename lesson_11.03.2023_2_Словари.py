dlist = []
dlist.append({1: 'один', 3: 'три', 5: 'пять'})
dlist.append(dict())
dlist[1][1] = 'one'
dlist[1][2] = 'two'
dlist[1][4] = 'four'
dlist.append(dict([(1, 'uno'), (3, 'tres'), (4, 'quatro')]))
dlist.append(dict(zip([1, 2, 5], ['yi', 'er', 'wu'])))
print(dlist)

res = {}
for d in dlist:
    for k in d:
        if k in res:
            res[k] = max(res[k], d[k])
        else:
            res[k] = d[k]
print(res)

for key in sorted(res):
    print(f'{key}:{res[key]}', end=' ')
