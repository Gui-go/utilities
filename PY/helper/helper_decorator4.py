def bold(f):
    def wrapped():
        return '<b>' + f() + '</b>'
    return wrapped

def italic(f):
    def wrapped():
        return '<i>' + f() + '</i>'
    return wrapped

@bold
@italic
def hello():
    return 'hello'

print(hello())

