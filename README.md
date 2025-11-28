*ESTRUTURAS CONDICIONAIS*

Sistema de Verificação de Idade – Estruturas Condicionais em Python Este repositório contém um exercício prático sobre estruturas condicionais em Python, utilizando if, elif e else. O objetivo é treinar tomada de decisões no código com base na entrada do usuário.

Explicação do Exercício: Crie um programa em Python que solicite a idade do usuário e determine se ele pode entrar em um evento ou não.

O programa deve passar por estas três etapas:

Pedir a idade usando input().
Verificar a idade usando estruturas condicionais.
Exibir a mensagem apropriada de acordo com a regra:
Regras: Faixa de Idade Condição no Evento:

Menor de 12 anos: A entrada é proibida.
- 12 a 17 anos: Entrada somente com responsável.
- 18 ou mais anos: Entrada liberada.
- Como Executar o Programa:

Como executar
- Certifique-se de usar o Visual Studio Code ou qualquer outro editor de código-fonte ( para alguns, será necessária a instalação do Python na versão mais recente).
- Baixe o arquivo.
- Coloque o código para rodar, para que seja requerido do usúarios as informações necessárias.

  
Exemplos de Entrada e Saída:

Exemplo para menores de idade
Entrada:
  Digite sua idade: 10
Saída:
  Entrada não permitida. Evento proibido para menores de 12 anos. 
  
Exemplos para pessoas de 12 a 17 anos:
Entrada:
  Digite sua idade: 15
Saída:
  Entrada permitida somente com responsável. 
  
Exemplo para maiores de idade:
Entrada:
  Digite sua idade: 22
Saída:
  Entrada liberada! Aproveite o evento.


FLUXOGRAMA:
                         ┌──────────────┐
                         │    INÍCIO     │
                         └───────┬──────┘
                                 │
                   ┌─────────────▼──────────────┐
                   │ Ler idade informada pelo    │
                   │ usuário (input -> int)      │
                   └─────────────┬──────────────┘
                                 │
                   ┌─────────────▼──────────────┐
                   │ idade < 12 ?               │
                   └───────┬────────────┬───────┘
                           │ NÃO         │ SIM
                           │             │
                      ┌────▼───┐     ┌──▼────────────────────────────────────────┐
                      │        │     │ Exibir: "Você não pode entrar. Este evento │
                      │        │     │ é proibido para menores de 12 anos!"       │
                      └────┬────┘     └───────────────────────────────────────────┘
                           │
                           │
                 ┌─────────▼───────────┐
                 │ idade >= 12 e < 18 ? │
                 └───────┬──────────────┘
                         │ NÃO
                         │
              ┌──────────▼──────────┐
              │ Exibir: "Entrada    │
              │ liberada!"          │
              └──────────┬──────────┘
                         │
                         ▼
                     ┌───────┐
                     │  FIM  │
                     └───────┘


                (SIM da segunda condição)
                ┌────────────────────────────────────────────┐
                │ Exibir: "Entrada permitida somente com     │
                │ responsável."                               │
                └────────────────────────────────────────────┘


-------------------------------------------------------------------------------------------------------------------------------------------

*ESTRUTURAS DE REPETIÇÃO* 

Esta pasta apresenta dois exercícios simples em Python para praticar estruturas de repetição: um utilizando for e outro utilizando while. Ambos os programas exibem apenas os números pares de 1 a 100.

-Exercício 1: Contador usando o for, ondemostra os números pares ( de 0 a 100).
O programa utiliza um loop for com a função range() para percorrer os números de 1 a 100. Dentro do loop, uma condição verifica se o número é par antes de exibi-lo.

Como executar

Certifique-se de usar o Visual Studio Code ou qualquer outro editor de código-fonte ( para alguns, será necessária a instalação do Python na versão mais recente).
Baixe o arquivo.
Coloque o código para rodar, para que seja requerido do usúarios as informações necessárias.
Exemplo de saída:

2 4 6 8 9 ... 100

Ps: Deverá exibir apenas números pares, caso exiba algum número ímpar, houve algum erro ou modificação no código.

FLUXOGRAMA:
                 ┌──────────────┐
                 │    INÍCIO     │
                 └───────┬──────┘
                         │
        ┌────────────────▼────────────────┐
        │ Iniciar loop FOR de 1 até 100   │
        └────────────────┬────────────────┘
                         │
               ┌─────────▼─────────┐
               │  Pegar o valor     │
               │  atual (num)       │
               └─────────┬─────────┘
                         │
         ┌───────────────▼─────────────────┐
         │ num é par? (num % 2 == 0)        │
         └───────────────┬─────────────────┘
                         │
                ┌────────┴────────┐
             NÃO│                 │SIM
                │                 │
        ┌───────▼──────┐   ┌─────▼─────┐
        │ Não imprime   │   │ Imprime   │
        │ nada          │   │ o número  │
        └───────┬──────┘   └─────┬─────┘
                │                │
                └──────┬─────────┘
                       │
             (volta ao FOR até acabar)
                       │
             ┌─────────▼─────────┐
             │     FIM DO FOR     │
             └─────────┬─────────┘
                       │
                 ┌─────▼─────┐
                 │    FIM    │
                 └───────────┘


-Exercício 2: Contador com while, onde mostrará os números pares, de 0 a 100. 
Descrição

Este programa utiliza a estrutura de repetição while para contar de 1 a 100. Assim como no exercício anterior, há uma condição para exibir apenas os números pares.

Como executar
- Certifique-se de usar o Visual Studio Code ou qualquer outro editor de código-fonte ( para alguns, será necessária a instalação do Python na versão mais recente).
- Baixe o arquivo.
- Coloque o código para rodar, para que seja requerido do usúarios as informações necessárias.
- 
Exemplo de saída:

2 4 6 8 9 ... 100

Ps: Deverá exibir apenas números pares, caso exiba algum número ímpar, houve algum erro ou modificação no código.

FLUXOGRAMA:
                 ┌──────────────┐
                 │    INÍCIO     │
                 └───────┬──────┘
                         │
        ┌────────────────▼───────────────┐
        │ Inicializar num = 1            │
        └────────────────┬───────────────┘
                         │
             ┌───────────▼───────────┐
             │ num <= 100 ?          │
             └───────┬───────────────┘
                     │
             NÃO     │      SIM
                     │
        ┌────────────▼──────────┐
        │     FIM DO LOOP       │
        └────────────┬──────────┘
                     │
               ┌─────▼─────┐
               │    FIM    │
               └───────────┘


                           (Sim)
                     │
          ┌──────────▼───────────┐
          │ num % 2 == 0 ?       │
          └───────┬──────────────┘
                  │
          NÃO     │      SIM
                  │
   ┌──────────────▼───────┐   ┌───────────────▼────────────┐
   │ Não imprime nada      │   │ Imprime o valor de num     │
   └──────────────┬────────┘   └───────────────┬────────────┘
                  │                            │
                  └──────────────┬─────────────┘
                                 │
                        ┌────────▼────────┐
                        │ num = num + 1   │
                        └────────┬────────┘
                                 │
                                 └───(volta para testar num <= 100)


------------------------------------------------------------------------------------------------------------------------------------------


*LISTAS*

Cadastro de Alunos – Onde o usuário precisará informar a idade dele, para que o programa veja se ele tem ou não permissão para acessar o evento. 
Usando listas, em Python.

Este projeto contém um programa simples em Python que permite ao usuário cadastrar nomes de alunos e, ao final, exibir a lista completa dos nomes inseridos.

Descrição do Programa

O programa utiliza uma lista para armazenar os nomes digitados pelo usuário.
O cadastro continua em um loop até que o usuário digite "exibir lista", momento em que o programa finaliza o cadastro e mostra todos os alunos registrados.

Como o programa funciona
- Cria uma lista vazia chamada alunos.
- Pede ao usuário que digite um nome.
- Cada nome é adicionado à lista.
- O processo continua até o usuário digitar exibir lista.
- Ao terminar, todos os nomes cadastrados são exibidos no console.

Como executar
- Certifique-se de usar o Visual Studio Code ou qualquer outro editor de código-fonte ( para alguns, será necessária a instalação do Python na versão mais recente).
- Baixe o arquivo.
- Coloque o código para rodar, para que seja requerido do usúarios as informações necessárias.

  
- Exemplo de entrada
Digite o nome do aluno ou 'exibir lista' para finalizar: Ana
Digite o nome do aluno ou 'exibir lista' para finalizar: Marcos
Digite o nome do aluno ou 'exibir lista' para finalizar: Julia
Digite o nome do aluno ou 'exibir lista' para finalizar: exibir lista

- Saída esperada
Lista de alunos cadastrados:
- Ana
- Marcos
- Julia


FLUXOGRAMA:
                 ┌──────────────┐
                 │    INÍCIO     │
                 └───────┬──────┘
                         │
             ┌───────────▼───────────┐
             │ Criar lista "alunos"  │
             └───────────┬───────────┘
                         │
                ┌────────▼────────┐
                │   Início do     │
                │     loop        │
                └────────┬────────┘
                         │
              ┌──────────▼──────────┐
              │ Ler nome digitado   │
              │ (input do usuário)  │
              └──────────┬──────────┘
                         │
             ┌───────────▼─────────────┐
             │ nome == "exibir lista"? │
             └───────┬───────────┬─────┘
                     │ NÃO       │ SIM
                     │           │
       ┌─────────────▼───┐       │
       │ Adiciona nome   │       │
       │ à lista alunos  │       │
       └───────────┬─────┘       │
                   │              │
       ┌───────────▼────────┐     │
       │ Exibe mensagem:    │     │
       │ "Aluno cadastrado" │     │
       └───────────┬────────┘     │
                   │              │
                   └───────┬──────┘
                           │
                     (volta ao loop)
                           │
                 ┌─────────▼─────────┐
                 │       FIM DO      │
                 │        LOOP       │
                 └─────────┬─────────┘
                           │
            ┌──────────────▼──────────────┐
            │  Exibir lista de alunos     │
            └──────────────┬──────────────┘
                           │
                     ┌─────▼─────┐
                     │    FIM    │
                     └───────────┘


------------------------------------------------------------------------------------------------------------------------------------------

*Dicionários*

Sistema de Cadastro de Produtos, onde o usuário precisará entrar com os dados ( nome do produto e valores) para que crie um dicionário. 
Usando dicionário e em Python

Este projeto apresenta um sistema simples de cadastro de produtos, onde cada item possui nome e preço, sendo armazenados em um dicionário do Python.
Ao final, o programa exibe todos os produtos cadastrados com seus respectivos valores.

Objetivo do Exercício
- Utilizar corretamente a estrutura dict();
- Inserir e recuperar dados do dicionário;
- Criar uma aplicação simples, clara e funcional em Python utilizando entrada de dados do usuário.

Como o programa funciona
- Um dicionário chamado produtos é criado para armazenar os itens no formato:
{ nome_do_produto: preço }
- O programa solicita continuamente:
  Nome do produto
  Preço do produto
- O usuário pode encerrar digitando "nao".

Ao final, todos os produtos cadastrados são exibidos.

Como executar
- Certifique-se de usar o Visual Studio Code ou qualquer outro editor de código-fonte ( para alguns, será necessária a instalação do Python na versão mais recente).
- Baixe o arquivo.
- Coloque o código para rodar, para que seja requerido do usúarios as informações necessárias.

  
Exemplo de entrada
Digite o nome do produto ou 'sair' para finalizar: Arroz
Digite o preço de 'Arroz': R$ 12.50

Digite o nome do produto ou 'sair' para finalizar: Feijão
Digite o preço de 'Feijão': R$ 9.80

Digite o nome do produto ou 'nao' para finalizar: nao

Saída esperada
Lista de Produtos Cadastrados:
- Arroz: R$ 12.50
- Feijão: R$ 9.80


FLUXOGRAMA:
                      ┌──────────────┐
                      │    INÍCIO     │
                      └───────┬──────┘
                              │
         ┌────────────────────▼────────────────────┐
         │ Criar dicionário vazio: produtos = {}   │
         └────────────────────┬────────────────────┘
                              │
                   ┌──────────▼───────────┐
                   │   Início do Loop     │
                   └──────────┬───────────┘
                              │
             ┌────────────────▼────────────────┐
             │ Exibir título "Cadastro..."     │
             └────────────────┬────────────────┘
                              │
                  ┌───────────▼───────────┐
                  │ Ler nome do produto    │
                  └───────────┬───────────┘
                              │
                  ┌───────────▼────────────┐
                  │ Ler preço (float)       │
                  └───────────┬────────────┘
                              │
        ┌─────────────────────▼────────────────────┐
        │ Armazenar no dicionário: produtos[nome]  │
        │                       = preco            │
        └─────────────────────┬────────────────────┘
                              │
            ┌─────────────────▼─────────────────┐
            │ Exibir mensagem: "Produto cadastrado" │
            └─────────────────┬─────────────────┘
                              │
              ┌───────────────▼──────────────┐
              │ Perguntar: cadastrar outro?   │
              │         (sim/nao)             │
              └───────────────┬──────────────┘
                              │
                ┌─────────────┴───────────────┐
               NÃO                             SIM
                │                               │
       ┌────────▼────────┐            ┌────────▼─────────┐
       │ Encerrar loop    │            │ Volta ao início  │
       └────────┬─────────┘            └────────┬─────────┘
                │                                │
                ▼                                │
      ┌────────────────────────┐                 │
      │ Exibir lista de        │                 │
      │ produtos cadastrados   │                 │
      └───────────┬────────────┘                 │
                  │                               
            ┌─────▼─────┐
            │    FIM    │
            └───────────┘

