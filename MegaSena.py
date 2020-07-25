# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 23:25:52 2020

@author: vroque
"""

import requests
import pandas as pd
import yaml
# Utilizei a biblioteca yaml para lidar com os dicionarios obtidos a partir da requisição
from random import randint
from time import sleep

# Definido os responses headers para facilitar a requisção
heads = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

lista_resultados_site = []
root_site = 'https://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA0sjIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQE-F4ca/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0KO6H80AU71KG7J0072/res/id=buscaResultado/c=cacheLevelPage/=/?timestampAjax=1595642946221&concurso='


# Gerando a lista de URLs a serem consultadas
for concurso in range (1,2283):
    site = root_site + str(concurso)
    lista_resultados_site.append(site)


# Requisitando as URLs
lista_resultados = []
lista_resultados_ganhadores = []
for concurso in range (0,25):
    resultado = lista_resultados_site[concurso]
    sleep(randint(6,18))
    r = requests.get(resultado,headers= heads,verify = False)

 # Data Source original
    json_result = r.text
    res = yaml.load(json_result)
    print(res)
   
 # Definindo as informações relevantes
    
    concurso = res.get("concurso")
    ganhadores = res.get("ganhadores")
    ganhadores_quina = res.get("ganhadores_quina")
    ganhadores_quadra = res.get("ganhadores_quadra")
    valor = res.get("valor")
    valor_quina = res.get("valor_quina")
    valor_quadra = res.get("valor_quadra")
    resultadoOrdenado = res.get("resultadoOrdenado")
    dataStr = res.get("dataStr")
    ganhadoresPorUf = res.get("ganhadoresPorUf")

#Armazendando essas informações no dicionário de "Resultados da Mega Sena"
    dict_result = {"concurso": concurso,"ganhadores": ganhadores,
     "ganhadores_quina": ganhadores_quina,"ganhadores_quadra": ganhadores_quadra,
     "valor": valor,"valor_quina": valor_quina,"valor_quadra": valor_quadra,
     "resultadoOrdenado": resultadoOrdenado,"dataStr": dataStr}

#Armazendando essas informações no dicionário de "Ganhadores da Mega Sena" 
    dict_result_ganhadores = {"concurso": concurso,  "ganhadoresPorUf": ganhadoresPorUf}


    
    lista_resultados.append(dict_result)
    #print(lista_resultados)
    lista_resultados_ganhadores.append(dict_result_ganhadores)
    print('---------------------------------------------------------')
    print(dict_result_ganhadores)


df = pd.DataFrame.from_dict(lista_resultados)

df.to_excel('Resultados MegaSena.xlsx')

with open("Ganhadores.txt", "w") as output:
    output.write(str(dict_result_ganhadores))

