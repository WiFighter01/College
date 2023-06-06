def strings_construction(a, b):
    count = 0
    count_a = 0
    c = []
    d = []
    Flag = True
    for letter in a:
        d.append(letter)

    while Flag:
        Flag = False
        for i in range(100000):
            count_a += 1
            if count_a > len(a):
                count_a = 0
                i = count_a
            for j in range(len(b)):
                if a[i] == b[j]:
                    c.append(b[j])
                    b = b[:j] + '0' + b[j + 1:]
                    Flag = True
                    if c == d:
                        count += 1
                        c = []
                    break
                else:
                    continue
    return count


a = 'hnccv'
b = 'hncvohcjhdfnhonxddcocjncchnvohchnjohcvnhjdhihsn'
strings_construction(a, b)
