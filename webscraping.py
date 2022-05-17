import requests
from bs4 import BeautifulSoup
response = requests.get('https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/envioColeta/dadosFotoEnvioColeta.jsf;jsessionid=HTARxpwFZdk8JeCHc7Mg7WCu.sucupira-204https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/envioColeta/dadosFotoEnvioColeta.jsf;jsessionid=HTARxpwFZdk8JeCHc7Mg7WCu.sucupira-204')
content = response.content

print ('Status Code' , response.status_code)
print ('Header')
print (response.headers)

print('\n  Content')
print(response.content)

site = BeautifulSoup(content, 'html.parser')

calendario=site.find('div',attrs={'class': 'input-group'})
print(calendario)