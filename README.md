# ABPJ3 - Gestor de Biblioteca

## Objetivo
Este projeto da ABPJ3 é um sistema simples de Gestor de Biblioteca feito em Python, usando listas e dicionários para cadastrar livros e controlar empréstimos.

O sistema possui as seguintes opções:
- Cadastrar livro
- Listar livros
- Emprestar livro
- Devolver livro
- Buscar livro
- Sair


## Regras do Sistema



## Estrutura Lógica
- while True para manter o menu rodando
- validação de Opção válida?
- match case (ou if/elif/else) para direcionar as opções do menu
- list para armazenar os livros
- dict para representar cada livro (título, autor, ano, status, usuário)
- for para procurar/listar livros
- .append() para adicionar livro



## Fluxo do Programa
1. Início  
2. Apresenta menu com opções  
3. Digitar opção do menu  
4. Opção válida?  
   - Não -> Mostrar "Opção inválida" -> volta ao menu  
   - Sim -> executa a opção escolhida:  
     1) Cadastrar livro  
     2) Listar livros  
     3) Emprestar livro  
     4) Devolver livro  
     5) Buscar livro  
     6) Sair  
5. Retornar Menu  
6. Fim (quando selecionar Sair)



## Fluxograma


1. Instale o Python 3
2. Execute o arquivo: main.py
