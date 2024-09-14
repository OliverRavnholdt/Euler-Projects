N = 1000    # Amount to sum all multiples under

multiples = [3, 5]  # Numbers to check for multiples

total = 0
for n in range(N):
    for i in multiples:
        if n % i == 0:
            print(n)
            total += n
            break

print("The total is:", total)
