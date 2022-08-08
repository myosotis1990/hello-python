n1 = 0
n2 = 0
i = 0

while i <= 15:
    n_sum = n1 + n2
    n1 = n2
    n2 = n_sum
    i = i + 1
    print(n2)