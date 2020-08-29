#!/usr/local/bin/python3
# Implementação simplificada do map


def mapear(funcao, lista):
    for elemento in lista:
        yield funcao(elemento)

# Mesma coisa
# def mapear(funcao, lista):
#     return (funcao(elemento) for elemento in lista)


if __name__ == "__main__":
    resultado = mapear(lambda x: x ** 2, [2, 3, 4, 5, 6, 7, 8])
    # print(list(resultado)) Irá imprimir todos de uma vez
    print(next(resultado)) # Lazy evaluation
    print(next(resultado))
    print(next(resultado))