a = int(input())

for i in range(0, a + 1, 2):
    if i < a - 1:
        print(i, end = ', ')
    else:
        print(i)