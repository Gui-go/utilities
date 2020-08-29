#!/usr/local/bin/python3
def sequence():
    num = 0
    while True:
        num += 1
        yield num
# Caso seja feito com return ou print, o resultado seria diferente.

if __name__ == '__main__':
    seq = sequence()

    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))