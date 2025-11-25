# Tarefa Prática: Sistema de Verificação de Idade para Entrada em Eventos

# Pede ao usuário que informe sua idade
idade = int(input("Informe sua idade: "))

# Verifica qual a idade informada e decide o tipo de saída
if idade < 12:
    # Menores de 12 anos não podem entrar
    print("Você não pode entrar. Este evento é  proibido para menores de 12 anos!")

elif idade >= 12 and idade < 18:
    # Entre 12 e 17 anos podem entrar apenas acompanhados por um responsável
    print("Entrada permitida somente com responsável.")

else:
    # 18 anos ou mais podem entrar
    print("Entrada liberada! Aproveite o evento!")
