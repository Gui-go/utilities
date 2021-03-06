test = "testando"
print(test)

# ord() returns the unicode associated with a string
print(ord("G"))

# chr() returns the character strings associated with a unicode number
print(chr(108), chr(105), chr(115), chr(116))

# type() returns the type of the object
type(ord("G"))
type(chr(110))

# dir() returns what methods are available for this object
dir(test)

#-----------------------------
import pandas as pd
df = pd.DataFrame(
    {
        "a": ["carro", "carro", "carro", "carro", "bike", "bike"],
        "b": [1, 2, 3, 4, 1, 1]
    }
)

df.groupby('key').transform(lambda x: x - x.mean())