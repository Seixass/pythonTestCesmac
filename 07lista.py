# Programa de classificação de suspeita em crime

# lista de perguntas que serão feitas ao usuário; cada índice corresponde a uma pergunta
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# contador de respostas afirmativas ('s') fornecidas pelo usuário
respostas_sim = 0

print("QUESTIONÁRIO DE INVESTIGAÇÃO")

# percorre a lista de perguntas mostrando número e texto
# enumerate(p ... , 1) inicia a contagem em 1 para exibir
for i, pergunta in enumerate(perguntas, 1):
    # pega a resposta do usuário, remove espaços e converte para minúscula
    resposta = input(f"{i}. {pergunta} (s/n): ").strip().lower()
    # incrementa contador se a resposta for 's' (sim)
    if resposta == 's':
        respostas_sim += 1

print("=" * 50)

# lógica de classificação baseada no número de respostas afirmativas
# cada faixa corresponde a um grau de envolvimento no crime
if respostas_sim == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_sim <= 4:
    classificacao = "Cúmplice"
elif respostas_sim == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"Respostas positivas: {respostas_sim}")
print(f"Classificação: {classificacao}")
print("=" * 50)

# mensagem para o professor
print("\nprofessor, nao consegui resolver muito essa e tive auxilio da IA, porem irei deixar comentado para mostrar que compreendi a resolucao dela.")