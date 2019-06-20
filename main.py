!pip
install
unidecode

##Acesso Cooredenadas


import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
from unidecode import unidecode
import lxml

# ===============================
# CEP
# ===============================

global position


def cep(consultCEP):
    url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'

    payload = {'relaxation': consultCEP,
               'tipoCEP': 'ALL',
               'semelhante': 'N'}

    r = requests.post(url, data=payload)
    soup = BeautifulSoup(r.text, 'html.parser')
    dados = soup.find_all('td')

    return dados


def cepcoord(consultCEP):
    url = 'https://www.mapacep.com.br/busca-cep.php'

    payload = {'keywords': consultCEP,
               'submit': 'Pesquisar'
               }

    r = requests.post(url, data=payload)
    soup = BeautifulSoup(r.text, 'html.parser')
    dados2 = soup.find_all('title')

    return dados2


consultCEP = input('CEP: ')
# consultCEP = 23821065 #25955310

dados = cep(consultCEP)
dados2 = cepcoord(consultCEP)

title = ['Local: ', 'Bairro: ', 'Cidade: ', 'CEP: ']
edress = []

# ----------------------
cont = 0
for a in dados:
    for b in a:
        edress.append(title[cont] + b)
        print(b)
    cont += 1

# ----------------------

for a in edress:
    print(a)

local = dados[2].get_text()[:len(dados[2].get_text()) - 4:]
local
# str(local)

# unidecode(str(local))

for a in dados2:
    for b in a:
        # print(b)
        coordenadas = b.split()

lat = coordenadas[len(coordenadas) - 3][-12:11:]
log = coordenadas[len(coordenadas) - 1]

print(lat)
print(log)

##Acesso CRESESB

table = []

url = 'http://www.cresesb.cepel.br/index.php?section=sundata'

payload = {'latitude_dec': lat[1:len(lat):],
           'latitude': lat,
           'hemi_lat': '0',
           'longitude_dec': log[1:len(log):],
           'longitude': log,
           'formato': '1',
           'lang': 'pt',
           'section': 'sundata'}

header = {'Accept': 'text/html,application/xhtml+xmlapplication/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
          'Cache-Control': 'max-age=0',
          'Connection': 'keep-alive',
          'Content-Length': '136',
          'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': 'switchgroup_news=0; switchgroup1=none',
          'Host': 'www.cresesb.cepel.br',
          'Origin': 'http://www.cresesb.cepel.br',
          'Referer': 'http://www.cresesb.cepel.br/index.php',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

r = requests.post(url, data=payload)

print(r.status_code)  # if return was 200, all ok
if r.status_code == requests.codes.ok:
    print('Continua Programa... \n')

    print('\n')

import re

# var = re.compile(r'Itaguai')


x = soup2.find_all('td', align="right")
for a in x:
    print(a.get_text())

# z = soup2.find_all('a', href=re.compile(r'localidade.*'))


'''lista_cidades = []
for n in soup2.find_all('a', href=re.compile(r'localidade.*')):
  lista_cidades.append(n.get_text())'''

soup = BeautifulSoup(r.text, 'lxml')

y = soup.select('table #tb_sundata > tbody > tr')  # [#]=id
soup2 = BeautifulSoup(str(y), 'lxml')
z = soup2.find_all('tr')

dados = []
for a in z:
    dados.append(a.get_text())

dd = []
var = []
position = 0
for a in dados:
    texto = a.split('\n')
    var.append(texto)
cont = 0
for b in var:
    for c in b[3:]:
        if c == unidecode(str(local)):
            print(' positin: ', cont)
            position = '{}'.format(cont)
            # print(b[8:len(b)-1])
            dd.append(b[8:len(b) - 1])

    cont += 1

mes = [
    'Distância [km]',
    'Jan',
    'Fev',
    'Mar',
    'Abr',
    'Mai',
    'Jun',
    'Jul',
    'Ago',
    'Set',
    'Out',
    'Nov',
    'Dez',
    'Média',
    'Delta'
]

df = pd.DataFrame(data=dd, columns=mes)
print('Irradiação solar diária média [kWh/m2.dia]')
print(df)

print('\n\n')

# ===================================================

print(position)

y2 = soup.select('table .tb_sundata > tbody > tr')  # [.]=class
soup3 = BeautifulSoup(str(y2), 'lxml')
z2 = soup3.find_all('tr')

dados2 = []
for a in z2:
    # print(a.get_text())
    dados2.append(a.get_text())

dd2 = []
var2 = []
for a in dados2:
    texto2 = a.split('\n')
    var2.append(texto2)

global result

result = 0
if int(position) == 0:
    print(var2[1])
    result = var2[1]

elif int(position) == 1:
    print(var2[5])
    result = var2[5]

elif int(position) == 2:
    print(var2[9])
    result = var2[9]

print(result)

mes2 = [
    'Jan',
    'Fev',
    'Mar',
    'Abr',
    'Mai',
    'Jun',
    'Jul',
    'Ago',
    'Set',
    'Out',
    'Nov',
    'Dez',
    'Média',
    'Delta'
]

bass = pd.DataFrame(data=[result[4:18]], columns=mes2)

bass

