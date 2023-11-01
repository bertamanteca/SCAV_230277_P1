import math

pi = 3.142857
m = 8  # Rows
n = 8  # Columns

def Transform(matriu):
    dct = []
    for i in range(m):
        dct.append([0] * n)

    for i in range(m):
        for j in range(n):
            ci = 1 / math.sqrt(m) if i == 0 else math.sqrt(2 / m)
            cj = 1 / math.sqrt(n) if j == 0 else math.sqrt(2 / n)

            sum_val = 0
            for k in range(m):
                for l in range(n):
                    dct_val = matriu[k][l] * math.cos((2 * k + 1) * i * pi / (2 * m)) * math.cos((2 * l + 1) * j * pi / (2 * n))
                    sum_val += dct_val

            dct[i][j] = ci * cj * sum_val

    for i in range(m):
        for j in range(n):
            print(f'{dct[i][j]:.2f}', end="\t")
        print()

matriu = [[255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255]]

Transform(matriu)
