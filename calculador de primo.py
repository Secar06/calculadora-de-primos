def es_primo(n, divisores = 0,):
    for i in range(1,n+1):
        if n % i == 0:
            divisores += 1    
    if divisores <= 2:
        return "Es primo"
    elif divisores >= 3:
            return "No es primo"

print(es_primo(997))