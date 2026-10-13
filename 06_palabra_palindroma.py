def main():
    palabra = input('Escribe una palabra: ').strip()
    if palabra == palabra[::-1]:
        print('¿Es palíndroma? SI')
    else:
        print('¿Es palíndroma? NO')

if __name__ == '__main__':
    main()
