MS = 5

def func(m):
    for p in range(MS // 2):
        for q in range(p, MS - p - 1):
            a = m[p][q]
            b = m[q][MS - p - 1]
            c = m[MS - p - 1][MS - q - 1]
            d = m[MS - q - 1][p]
            m[p][q] = d
            m[q][MS - p - 1] = a
            m[MS - p - 1][MS - q - 1] = b
            m[MS - q - 1][p] = c

def main():
    m = [[i for j in range(MS)] for i in range(MS)]

    func(m)

    for row in m:
        for ele in row:
            print(ele, end="")
        print()

if __name__ == "__main__":
    main()
