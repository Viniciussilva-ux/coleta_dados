import requests


def enviar_arquivo():
    # Caminho do arquivo para upload
    caminho = 'https://www.mediafire.com/file/1seeux004yfsxcl/produtos_informatica.xlsx/file'

    # Enviar o arquivo
    requisicao = requests.post('https://app.mediafire.com/myfiles', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print('arquivo enviado. link para acesso:', url)


def enviar_arquivo_chave():
    # Caminho do arquivo e chave para upload
    caminho = 'https://www.mediafire.com/file/1seeux004yfsxcl/produtos_informatica.xlsx/file'
    # chave acesso = // API Key

    # Enviar o arquivo
    requisicao = requests.post(
        'https://app.mediafire.com/myfiles',
        files={'file': open(caminho, 'rb')},
        headers={'authorization': chave_acesso}
    )
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao ['link']
    print('arquivo enviado com chave. link para acesso:', url)


def receber_arquivo(file_url):
    # Receber o arquivo
    requisicao = requests.get(file_url)

    # Salvar o arquivo
    if requisicao.ok:
        with open('', 'wb') as file:
            file.write(requisicao.content)
        print('arquivo baixado com sucesso.')
    else :
        print('erro ao baixar o arquivo:', requisicao.json())


enviar_arquivo()
# enviar_arquivo_chave()
#receber_arquivo('https://www.mediafire.com/file/1seeux004yfsxcl/produtos_informatica.xlsx/file')

