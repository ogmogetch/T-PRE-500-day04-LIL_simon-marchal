def display_multiples(n):
    for i in range(2, n // 2 + 1):
        multiples = []
        for j in range(n - i, 1, -1):
            if j % i == 0:
                multiples.append(j)
        if multiples:
            print(" ".join(map(str, multiples)))

n = int(input("Enter an integer n: "))
display_multiples(n)