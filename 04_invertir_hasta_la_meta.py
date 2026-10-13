def main():
    d = int(input('Depósito inicial: '))
    a = int(input('Aporte mensual: '))
    m = int(input('Meta: '))

    # 6% anual equivale a 0.5% mensual
    total = float(d)
    mes = 0
    print('Mes y total acumulado:')
    print(f'{mes} {total:.6f}')
    while total < m:
        total = total * 1.005 + a
        mes += 1
        print(f'{mes} {total:.6f}')
    print(f'La meta se alcanza en el mes {mes}')

if __name__ == '__main__':
    main()
