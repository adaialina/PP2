list1 = [3, 58, 346, 17, 19, 23, 21]

is_prime = list(filter(lambda i: all(i%j!=0 for j in range(2, i//2)), list1))

print(is_prime)