import sys

def main():
    print('Escribe los nombres de los instructores separados por espacios:')
    instructores = sys.stdin.read().split()
    print('Número de instructores:', len(instructores))

if __name__ == '__main__':
    main()
