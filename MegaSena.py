# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 23:25:52 2020

@author: vroque
"""

import requests
import pandas as pd
import yaml
from random import randint
from time import sleep


heads = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

lista_resultados_site = []
root_site = 'https://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/!ut/p/a1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOLNDH0MPAzcDbwMPI0sDBxNXAOMwrzCjA0sjIEKIoEKnN0dPUzMfQwMDEwsjAw8XZw8XMwtfQ0MPM2I02-AAzgaENIfrh-FqsQ9wNnUwNHfxcnSwBgIDUyhCvA5EawAjxsKckMjDDI9FQE-F4ca/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_HGK818G0KO6H80AU71KG7J0072/res/id=buscaResultado/c=cacheLevelPage/=/?timestampAjax=1595642946221&concurso='

for concurso in range (1,2283):
    site = root_site + str(concurso)
    lista_resultados_site.append(site)

lista_resultados = []
lista_resultados_ganhadores = []
for concurso in range (0,25):
    resultado = lista_resultados_site[concurso]
    sleep(randint(6,18))
    r = requests.get(resultado,headers= heads,verify = False)
    
    json_result = r.text
    res = yaml.load(json_result)
    print(res)
   
    
    #res = json.loads(json_result)
    
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
    
    dict_result = {"concurso": concurso,"ganhadores": ganhadores,
     "ganhadores_quina": ganhadores_quina,"ganhadores_quadra": ganhadores_quadra,
     "valor": valor,"valor_quina": valor_quina,"valor_quadra": valor_quadra,
     "resultadoOrdenado": resultadoOrdenado,"dataStr": dataStr}
    
    dict_result_ganhadores = {"concurso": concurso,  "ganhadoresPorUf": ganhadoresPorUf}


    
    lista_resultados.append(dict_result)
    #print(lista_resultados)
    lista_resultados_ganhadores.append(dict_result_ganhadores)
    print('---------------------------------------------------------')
    print(dict_result_ganhadores)


df = pd.DataFrame.from_dict(lista_resultados)

df.to_excel('Ganhadores MegaSena.xlsx')

with open("Ganhadores.txt", "w") as output:
    output.write(str(dict_result_ganhadores))

