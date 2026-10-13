def main():
    a, b = map(int, input('Escribe dos números a y b separados por un espacio: ').split())
    print(f'Números del {a} al {b}:')
    for i in range(a, b + 1):
        print(i)

if __name__ == '__main__':
    main()
