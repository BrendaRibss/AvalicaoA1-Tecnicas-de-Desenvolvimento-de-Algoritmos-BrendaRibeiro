# Criando um dicionário vazio para armazenar os produtos
# A chave será o nome do produto e o valor será o preço
produtos = {}

# Loop infinito para permitir vários cadastros
while True:
    print("\n--- Cadastro de Produtos do Mercado Brend's ---")
    
    # Solicita o nome do produto
    nome = input("Digite o nome do produto: ")
    
    # Solicita o preço do produto e converte para float
    preco = float(input("Digite o preço do produto: "))
    
    # Armazena o produto no dicionário
    produtos[nome] = preco
    
    print("\nProduto cadastrado com sucesso!")

    # Pergunta ao usuário se deseja cadastrar outro produto
    opcao = input("Deseja cadastrar outro produto? (sim/nao): ").lower()
    
    # Se digitar 'nao', o loop é encerrado
    if opcao == "nao":
        break

# Após o cadastro, exibe todos os produtos
print("\n--- Lista de Produtos Cadastrados ---")
for nome, preco in produtos.items():
    print(f"Produto: {nome} | Preço: R$ {preco:.2f}")

