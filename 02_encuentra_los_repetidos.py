def tieneRepetidos(v):
    vistos = set()
    for x in v:
        if x in vistos:
            return 1
        vistos.add(x)
    return 0

def main():
    n = int(input('¿Cuántos números vas a escribir? '))
    v = [int(x) for x in input(f'Escribe los {n} números separados por espacios: ').split()[:n]]
    if tieneRepetidos(v):
        print('¿Hay números repetidos? SI')
    else:
        print('¿Hay números repetidos? NO')

if __name__ == '__main__':
    main()
