# ABPJ3 - Gestor de Biblioteca

## Objetivo
Este projeto da ABPJ3 é um sistema gestor de biblioteca feito em Python, usando listas e dicionários para cadastrar livros e controlar empréstimos.

O sistema possui as seguintes opções:
- Cadastrar livro
- Listar livros
- Emprestar livro
- Devolver livro
- Buscar livro
- Sair

## Regras do Sistema

1. O sistema mostra o menu, o usuário digita uma opção e o programa valida:
   Se for inválida -> mostra Opção inválida e volta ao menu.
2. Cadastrar livro: digita título/autor/ano e o sistema verifica se já existe antes de salvar.
3. Emprestar livro: informa o título -> se não achar, mostra Livro não encontrado.
   Se achar e estiver disponível, registra o empréstimo.
   Se não, mostra Livro está emprestado.
4. Devolver livro: informa o título -> se não achar, Livro não encontrado.
   Se não estiver emprestado mostra Nada para devolver.
   Se estiver, devolve e confirma.
5. Buscar livro: informa o título -> mostra os dados se encontrar.
   Senão Livro não encontrado.
6. Depois de qualquer ação, o sistema retorna ao menu ao escolher Sair o programa finaliza.

## Estrutura Lógica
- while True para manter o menu rodando
- validação de Opção válida?
- match case para direcionar as opções do menu
- lista para armazenar os livros
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
<img width="2023" height="1291" alt="fluxograma drawio" src="https://github.com/user-attachments/assets/68516b1d-17f2-4d49-9bab-18ff8bb54fb3" />


## Como Executar

1. Instale o Python 3
2. Execute o arquivo: main.py
