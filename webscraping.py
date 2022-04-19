import requests

response = requests.get('https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/envioColeta/dadosFotoEnvioColeta.jsf;jsessionid=HTARxpwFZdk8JeCHc7Mg7WCu.sucupira-204')

print ('Status Code' , response.status_code)
print ('Header')
print (response.headers)