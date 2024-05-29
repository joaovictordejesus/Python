def criar_csv_livros():
    livros = [
        {"Título": "Livro 1", "Autor": "Autor 1", "Ano de publicação": 2001, "Número de páginas": 100},
        {"Título": "Livro 2", "Autor": "Autor 2", "Ano de publicação": 2002, "Número de páginas": 200},
    ]
    
    with open("meus_livros.csv", "w") as file:
        file.write("Título,Autor,Ano de publicação,Número de páginas\n")
        for livro in livros:
            linha = f'{livro["Título"]},{livro["Autor"]},{livro["Ano de publicação"]},{livro["Número de páginas"]}\n'
            file.write(linha)

criar_csv_livros()