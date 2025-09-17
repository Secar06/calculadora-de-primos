def sec_fibbo(n, anterior = 0, actual = 0, x=0):
    for i in range(0, n):
            x = actual
            actual = anterior + actual
            anterior = x
            if i <= 1:
                actual += i
    return actual   
n = int(input("ingrese un numero: "))
resultado = sec_fibbo(n)
print(f"El numero en la posicion {n} de la sucesion de fibbonachi es {resultado}")