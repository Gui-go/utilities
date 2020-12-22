try:  
    import math
    inp = int(input())
    print(math.exp(inp))
except OverflowError:  
    print("OverFlow Exception Raised.")
except ValueError:
    print('Não tais inputando uma string, feio?')
else:  
    print("Success, no error!")