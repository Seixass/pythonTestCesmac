total = 0
quantidade_acima_50 = 0

while True:
    preco = float(input("Digite o preço do produto (0 para sair): R$ "))
    
    if preco == 0:
        break
    
    total += preco
    
    if preco > 50:
        quantidade_acima_50 += 1

print("\n--- RESULTADO ---")
print(f"Total da compra: R$ {total:.2f}")
print(f"Produtos acima de R$ 50,00: {quantidade_acima_50}")

if total > 100:
    desconto = total * 0.10
    total_com_desconto = total - desconto
    print(f"Desconto de 10%: R$ {desconto:.2f}")
    print(f"Total com desconto: R$ {total_com_desconto:.2f}")