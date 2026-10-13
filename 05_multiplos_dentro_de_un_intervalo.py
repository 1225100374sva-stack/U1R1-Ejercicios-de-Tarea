def main():
    a, b = map(int, input('Escribe dos números a y b separados por un espacio: ').split())
    multiplos = []
    for i in range(a, b + 1):
        if a != 0 and i % a == 0:
            multiplos.append(str(i))
    print(f'Múltiplos de {a} entre {a} y {b}:', ' '.join(multiplos))

if __name__ == '__main__':
    main()
