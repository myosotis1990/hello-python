n1 = 1
n2 = 1
i = 1

while i < 15:
    n_sum = n1 + n2
    n1 = n2
    n2 = n_sum
    i = i + 1
    print(n2)