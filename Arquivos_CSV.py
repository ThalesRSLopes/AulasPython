from csv import reader, DictReader, writer, DictWriter


print("Utilizando reader")
# faz a leitura do arquivo e retorna uma lista (iterator)
# onde cada linha é uma lista (o conteúdo é uma lista de listas)
with open('files\\lutadores.csv', encoding='utf-8') as arquivo:
    leitor = reader(arquivo, delimiter=',')
    next(leitor)
    for linha in leitor:
        print(f'{linha[0]} nasceu em {linha[1]} e tem {linha[2]} centímetros de altura')


print("\n\nUtilizando DictReader")
# faz a leitura do arquivo e retorna um dicionário
# onde cada linha é um dicionário (o conteúdo é uma lista de dicionários)
with open('files\\lutadores.csv', encoding='utf-8') as arquivo:
    leitor = DictReader(arquivo, delimiter=',')
    for linha in leitor:
        print(f'{linha["Nome"]} nasceu em {linha["País"]} e tem {linha["Altura (em cm)"]} centímetros de altura')


print("\n\nEscrevendo dados no arquivo csv utilizando Writer")
with open('files\\filmes.csv', 'w', encoding='utf-8') as arquivo:
    escritor = writer(arquivo)
    # Escreve o cabeçalho
    escritor.writerow(["Título", "Gênero", "Duração"])
    # Escrevendo os filmes
    escritor.writerow(["O Senhor dos Anéis: A Sociedade do Anel", "Fantasia", "233"])
    escritor.writerow(["O Senhor dos Anéis: As duas Torres", "Fantasia", "245"])
    escritor.writerow(["O Senhor dos Anéis: O Retorno do Rei", "Fantasia", "257"])

print("\nOs dados escritos no arquivo foram:")
# faz a leitura do arquivo e retorna um dicionário
# onde cada linha é um dicionário (o conteúdo é uma lista de dicionários)
with open('files\\filmes.csv', encoding='utf-8') as arquivo:
    leitor = DictReader(arquivo, delimiter=',')
    for linha in leitor:
        print(f'O filme {linha["Título"]} é do gênero {linha["Gênero"]} e tem {linha["Duração"]} minutos de duração')


print("\n\nEscrevendo dados no arquivo csv utilizando DictWriter")
with open('files\\filmes2.csv', 'w', encoding='utf-8') as arquivo:
    cabecalho = ["Título", "Gênero", "Duração"]
    escritor = DictWriter(arquivo, fieldnames=cabecalho)
    # Escreve o cabeçalho
    escritor.writeheader()
    # Escrevendo os filmes
    escritor.writerow({"Título": "O Senhor dos Anéis: A Sociedade do Anel", "Gênero": "Fantasia", "Duração": "233"})
    escritor.writerow({"Título": "O Senhor dos Anéis: As duas Torres", "Gênero": "Fantasia", "Duração": "245"})
    escritor.writerow({"Título": "O Senhor dos Anéis: O Retorno do Rei", "Gênero": "Fantasia", "Duração": "257"})


print("\nOs dados escritos no arquivo foram:")
# faz a leitura do arquivo e retorna um dicionário
# onde cada linha é um dicionário (o conteúdo é uma lista de dicionários)
with open('files\\filmes2.csv', encoding='utf-8') as arquivo:
    leitor = DictReader(arquivo, delimiter=',')
    for linha in leitor:
        print(f'O filme {linha["Título"]} é do gênero {linha["Gênero"]} e tem {linha["Duração"]} minutos de duração')
