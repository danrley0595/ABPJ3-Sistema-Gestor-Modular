#Função para exibir o menu e informar a opção desejada
def exibirMenu():
    #Laço para apresentar o menu enquanto condição verdadeira
    while True:
        print("\n=== GESTOR DE BIBLIOTECA ===\n")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("5 - Buscar livro por título")
        print("6 - Sair")
        # .Strip para tirar espaços em branco do começo e do fim
        opcao = input("Digitar opção do menu(1 a 6):").strip()
        executarOpcao(opcao)
        
# Verifica se a opção está entre as definidas no if, caso sim executa a opção desejada
# Caso não retorno na função exibir 
def executarOpcao(opcao):
            # Só entra no if se for de 1 a 6, senão retorna no while
        if opcao in ("1", "2", "3", "4", "5", "6"):
            match opcao:
                case "1":
                    cadastrarLivro()
                case "2":
                    listarLivro()
                case "3":
                    emprestarLivro()
                case "4":
                    print("\nOpção 4\n")
                case "5":
                    print("\nOpção 5\n")
                case "6":
                    sair_Programa()
    
# função para cadastrar livro 
def cadastrarLivro():
    print("\n--- Cadastrar livro ---\n")
    titulo = input("Título: ").strip().upper() 
    autor = input("Autor: ").strip().upper() 
    ano = input("Ano: ").strip().upper() 
                
    # adicona livro a lista
    livros.append({
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "status": "DISPONIVEL",
         "usuario": ""
        })
    print("\nLivro Cadastrado com Sucesso!")

#função para listar todos os livros, caso exista.    
def listarLivro():
    print("\n---Lista de livros---\n")
    if (len(livros) > 0):
        for livro in livros:
            print(f"Título: {livro["titulo"]} - Autor: {livro["autor"]} - Ano: {livro["ano"]} - Status: {livro["status"]} - Usuário: {livro["usuario"]}"
            )
    else:
        print("\nNenhum livro cadastrado.\n")
        
#função para emprestar o livro, onde verifica se o livro existe          
def emprestarLivro():
    titulo = str(input("Informe o título do livro que deseja buscar:")).strip().upper()
    cont = 0
    if (len(livros) > 0):
        for livro in livros:
            if(livro["titulo"] == titulo and livro["status"] == "DISPONIVEL"):
                usuario = str(input("Informe seu nome: ")).strip().upper()
                livro["usuario"] = usuario
                livro["status"] = "EMPRESTADO"
                print(f"Livro emprestado com sucesso para {usuario}!")
                
            elif(livro["titulo"] == titulo and livro["status"] == "EMPRESTADO"):
                print("Livro se encontra emprestado!")
        if(cont == 0):
            print("Livro não encontrado!")
    
    else:
        print("\nNão existe livros cadastrados.\n")

def devolverLivro():
    titulo = str(input("Informe o título do livro que deseja devolver:")).strip().upper()
    cont = 0
    if (len(livros) > 0):
        for livro in livros:
            if(livro["titulo"] == titulo and livro["status"] == "EMPRESTADO"):
                livro["usuario"] = ""
                livro["status"] = "DISPONIVEL"
                print(f"Livro devolvido com sucesso!")
                cont += 1
                
            elif(livro["titulo"] == titulo and livro["status"] == "DISPONIVEL"):
                print("Livro se encontra disponivel não é possivel devolver!")
                cont += 1
        if(cont == 0):
            print("Livro não encontrado!")
            
    else:
        print("\nNão existe livros cadastrados.\n")
        
def sair_Programa():
    print("Programa Finalizado!")
    exit()

# criação de uma lista para armazenar os livros
livros = []
opcao = str()

#Chama a função para apresentar o menu e seguir com fluxo de funções
exibirMenu()
