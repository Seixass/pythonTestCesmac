n = int(input("Quantos números você vai inserir? "))

if n <= 0:
    print("Por favor, insira um número positivo.")

else:
    numeros = []

    for i in range(n):
        num = float(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

    menor = min(numeros)
    maior = max(numeros)
    soma = sum(numeros)

    print(f"\nMenor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Soma dos valores: {soma}")