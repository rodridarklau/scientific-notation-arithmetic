def descomponer_notacion(x, base=10):
    array = []
    x_str = str(x)
    if "." in x_str:
        y = float(x_str)
        parte_entera = x_str.split('.')[0]
        exponente = len(parte_entera) - 1
    else:
        y = int(x_str)
        exponente = len(x_str) - 1

    pf = y / (base ** exponente)
    array.extend([pf, base, exponente])
    return array


def multiplicar_notacion(num1, num2):
    c1, base, e1 = num1
    c2, _, e2 = num2
    resultado_real = (c1 * c2) * (base ** (e1 + e2))
    return descomponer_notacion(resultado_real, base)


def dividir_notacion(num1, num2):
    c1, base, e1 = num1
    c2, _, e2 = num2
    resultado_real = (c1 / c2) * (base ** (e1 - e2))
    return descomponer_notacion(resultado_real, base)


def sumar_notacion(num1, num2):
    c1, base, e1 = num1
    c2, _, e2 = num2
    resultado_real = (c1 * (base ** e1)) + (c2 * (base ** e2))
    return descomponer_notacion(resultado_real, base)


def restar_notacion(num1, num2):
    c1, base, e1 = num1
    c2, _, e2 = num2
    resultado_real = (c1 * (base ** e1)) - (c2 * (base ** e2))
    return descomponer_notacion(resultado_real, base)



n1 = descomponer_notacion(input("Primer número: "))    
n2 = descomponer_notacion(input("Segundo número: "))   

print(f"\nNum 1: {n1[0]} x 10^{n1[2]}")
print(f"Num 2: {n2[0]} x 10^{n2[2]}")
print("-" * 30)
print(f"Multiplicación : {multiplicar_notacion(n1, n2)}")
print(f"División       : {dividir_notacion(n1, n2)}")
print(f"Suma           : {sumar_notacion(n1, n2)}")
print(f"Resta          : {restar_notacion(n1, n2)}")