import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text,'html.parser')

# Exibir o texto
print(extracao.text.strip())

# Filtrar a exibição pela tag
for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()
    print('titulo: ', titulo)

'''
Desafio 
filtrar tags ['h2','p']
contar quantos h2 e p existem no documento (linha_texto.name == tag)
'''

# Contar quantidade de títulos e parágrafos
contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all(['h2','p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1 # contar_titulos = cotar_titulos + 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1

print('total de titulos', contar_titulos)
print('total de paragrafos', contar_paragrafos)

# Exibir somente o texto das tags h2 e p
for linha_texto in extracao.find_all(['h2','p']):
    if linha_texto.name == 'h2':
        titulo = linha_texto.text.strip()
        print('titulo: \n', titulo )
    elif linha_texto.name == 'p':
        paragrafo = linha_texto.text.strip()
        print('paragrafo: \n', paragrafo)

# exibir tags aninhada
for titulo in extracao.find_all('h2'):
    print('\n titulo:', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('texto link:', a.text.strip(),'| URL:', a['href'])




