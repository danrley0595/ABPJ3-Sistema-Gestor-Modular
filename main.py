# criação de uma lista para armazenar os livros
livros = []

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
    # Só entra no if se for de 1 a 6, senão retorna no while
    if opcao in ("1", "2", "3", "4", "5", "6"):
        
        match opcao:
            case "1":
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
                
            case "2":
                print("\n---Lista de livros---\n")
                if (len(livros) > 0):
                    for livro in livros:
                        print(f"Título: {livro["titulo"]} - Autor: {livro["autor"]} - Ano: {livro["ano"]} - Status: {livro["status"]} - Usuário: {livro["usuario"]}\n"
            )
                else:
                    print("\nNenhum livro cadastrado.\n")
                    
            case "3":
                print("\nOpção 3\n")
                
            case "4":
                print("\nOpção 4\n")
            case "5":
                print("\nOpção 5\n")
            case "6":
                print("Programa Finalizado!")
                break;
