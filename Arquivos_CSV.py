from csv import reader, DictReader

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
