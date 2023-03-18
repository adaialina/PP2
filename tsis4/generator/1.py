a = int(input())

def squares(a):
    for i in range(a):
        if (i*i) <= a:
            yield i * i

for i in squares(a):
    print (i)