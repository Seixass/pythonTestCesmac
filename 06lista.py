turno = input("Qual é o seu turno? (m/v/n): ").lower()

if turno == 'm':
    print("Bom dia!")
elif turno == 'v':
    print("Boa tarde!")
elif turno == 'n':
    print("Boa noite!")
else:
    print("Valor inválido")