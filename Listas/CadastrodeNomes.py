# Programa para cadastrar nomes de alunos e exibir ao final

# Criamos uma lista vazia para armazenar os nomes
alunos = []

while True:
    # Solicita ao usuário que digite um nome de aluno
    nome = input("Digite o nome do aluno ou 'exibir lista' para finalizar: ")

    # Se o usuário digitar 'exibir lista', o loop encerra
    if nome.lower() == 'exibir lista':
        break

    # Adiciona o nome digitado na lista
    alunos.append(nome)
    print("Aluno cadastrado com sucesso!\n")

# Exibe a lista completa de alunos cadastrados
print("\nLista de alunos cadastrados:")
for aluno in alunos:
    print(f"- {aluno}")

