x = input("Enter a number: ")
array = []
medir = len(str(x))
exponente = medir - 1
base = 10

if "." in x:
    y = float(x)
    parte_entera = x.split('.')[0]
    exponente = len(parte_entera) - 1
else:
        y = int(x)
        exponente = len(x) -1

pf = y / (base ** exponente)

array.append(pf)
array.append(base)
array.append(exponente)

print(array)