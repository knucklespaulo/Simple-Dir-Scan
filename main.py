'''
status code 200 = sucesso
status code 404 = não encontrado
status code 401 = existe, não autorizado
'''

import requests
diretorios=["backups","senhas","wp-admin","wp-content","database"]

alvo = input("insira o alvo para scan: ")
print("Iniciando Scan...")

#verifica se o ultimo caractere do alvo é uma "/" ou não.
for pasta in diretorios:

    if alvo[len(alvo)-1]=="/":
        url=alvo+pasta
#insere uma "/" caso não seja.       
    else:
        url=alvo+"/"+pasta
    
    requisicao = requests.get(url)
    
    if requisicao.status_code >= 200 and requisicao.status_code < 300:
        print("Diretório encontrado! | "+url)
    elif requisicao.status_code == 401 or requisicao.status_code == 403:
        print("Diretório encontrado, acesso negado. | "+url)
    elif requisicao.status_code == 404:
        print("Diretório não encontrado. |"+url)
        

