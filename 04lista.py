def validar_nome(nome):
    while len(nome) <= 3:
        nome = input("Nome inválido! Deve ter mais de 3 caracteres. Digite novamente: ")
    return nome

def validar_idade(idade):
    while True:
        try:
            idade = int(idade)
            if 0 <= idade <= 150:
                return idade
            else:
                idade = input("Idade inválida! Deve estar entre 0 e 150. Digite novamente: ")
        except ValueError:
            idade = input("Idade inválida! Digite um número inteiro: ")

def validar_salario(salario):
    while True:
        try:
            salario = float(salario)
            if salario > 0:
                return salario
            else:
                salario = input("Salário inválido! Deve ser maior que zero. Digite novamente: ")
        except ValueError:
            salario = input("Salário inválido! Digite um número: ")

def validar_sexo(sexo):
    while sexo.lower() not in ['f', 'm']:
        sexo = input("Sexo inválido! Digite 'f' ou 'm': ")
    return sexo.lower()

def validar_estado_civil(estado):
    while estado.lower() not in ['s', 'c', 'v', 'd']:
        estado = input("Estado civil inválido! Digite 's', 'c', 'v' ou 'd': ")
    return estado.lower()

nome = input("Nome: ")
nome = validar_nome(nome)

idade = input("Idade: ")
idade = validar_idade(idade)

salario = input("Salário: ")
salario = validar_salario(salario)

sexo = input("Sexo (f/m): ")
sexo = validar_sexo(sexo)

estado_civil = input("Estado Civil (s/c/v/d): ")
estado_civil = validar_estado_civil(estado_civil)

print("\n=== DADOS VALIDADOS ===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

#tranquilo, porém trabalhoso.