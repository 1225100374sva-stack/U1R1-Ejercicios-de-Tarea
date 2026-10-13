import sys

def main():
    print('Escribe el número de filas y columnas y después la tabla:')
    datos = sys.stdin.read().split()
    n, m = int(datos[0]), int(datos[1])
    altura = [0] * m
    for i in range(n):
        for j in range(m):
            altura[j] += int(datos[2 + i * m + j])
    print('Suma de cada columna:', ' '.join(str(h) for h in altura))

if __name__ == '__main__':
    main()
