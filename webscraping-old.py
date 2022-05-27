import requests
from bs4 import BeautifulSoup
response = requests.get('https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/envioColeta/dadosFotoEnvioColeta.jsf;jsessionid=HTARxpwFZdk8JeCHc7Mg7WCu.sucupira-204')
content = response.content

''' print ('Status Code' , response.status_code)
print ('Header')
print (response.headers) '''

#print('\n  Content')
#print(response.content)

site = BeautifulSoup(content, 'html.parser')

#Dados do Envio
DadosDoEnvio=site.find('div',attrs={'class': 'conteudo'})
#Calendario
Calendario=DadosDoEnvio.find('div', attrs={'class': 'input-group'})
#Instituição de Ensino Superior
# Instituicao= DadosDoEnvio.find()

# print(DadosDoEnvio.find())
print("-------------------------------")
print(DadosDoEnvio.find())

