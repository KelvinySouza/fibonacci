def fibonacci(n):
    if n <= 0:
        return "Entrada inválida"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

numero = int(input("Digite um número para calcular a sequência de Fibonacci: "))
resultado = fibonacci(numero)
print("A sequência de Fibonacci até o número", numero, "é:", resultado)