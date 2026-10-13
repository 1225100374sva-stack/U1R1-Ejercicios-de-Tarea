import sys

def main():
    print('Escribe las edades separadas por espacios (termina con Enter y Ctrl+D):')
    edades = sys.stdin.read().split()
    listaResultado = sorted(set(edades))[::-1]
    print('Edades sin repetir, de mayor a menor:', listaResultado)

if __name__ == '__main__':
    main()
