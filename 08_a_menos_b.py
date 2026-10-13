def main():
    b = input('Escribe los 3 números de B separados por espacios: ').split()[:3]
    n = int(input('¿Cuántos números tiene A? '))
    arreglo = input(f'Escribe los {n} números de A separados por espacios: ').split()[:n]
    resultado = [x for x in arreglo if int(x) not in map(int, b)]
    print('A sin los números de B:', ' '.join(resultado))

if __name__ == '__main__':
    main()
