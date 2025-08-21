def fibonacci(n):
    if n < 2:
        return n
    n_1, n_2 = 1, 0

    for _ in range(n-1):
        n_1, n_2 = n_1 + n_2, n_1

    return n_1


def fibonacci_list(n):
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


for i in range(10):
    print(f'fibonacci({i}): {fibonacci(i)}')

print('*'*20)
print(fibonacci_list(10))