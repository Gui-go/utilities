



dict1 = dict({"key1": 1, "key2": "b", "key3": [1, "b", "c3"]})
dict1
dict1["key2"]
dict1["key3"][0:2]
dict1["wrongKey"] # Solta mensagem de erro
dict1.get("key3")
dict1.get("wrongKey") # Não solta mensagem de erro
dict1.get("wrongKey", [])
dict1.get("wrongKey", "ZERO")
dict1["key3"].append("D4")
dict1["key3"]



# Dictionary comprehention
dc = { i: i * 2 for i in range(10) if i % 2 == 0 }

for i, e in dc.items():
    print(f'{i} x 2 = {e}')

