a = int(input())

def div4and3(a):
    for i in range(a + 1):
        if (i % 3 == 0) and (i % 4 == 0):
            yield i

for i in div4and3(a):
    print(i)