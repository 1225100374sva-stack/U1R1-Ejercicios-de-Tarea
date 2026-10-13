def main():
    print('Permutaciones de 1, 2, 3 y 4:')
    for a in range(1, 5):
        for b in range(1, 5):
            if b == a:
                continue
            for c in range(1, 5):
                if c == a or c == b:
                    continue
                for d in range(1, 5):
                    if d == a or d == b or d == c:
                        continue
                    print(a, b, c, d)

if __name__ == '__main__':
    main()
