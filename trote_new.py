import webbrowser
import time
import pyautogui
import pyperclip
import re
import csv
import os
import random
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta  # Certifique-se de ter o módulo dateutil instalado

# Dicionário para realizar o looping de pesquisa sobre as universidades
universidades = ['', 'UNESP', 'USP', 'UNICAMP'] 

# Dicionário para converter os meses por extenso para seus números correspondentes
meses = {
    'jan': '01', 'fev': '02', 'mar': '03', 'abr': '04', 'mai': '05', 'jun': '06',
    'jul': '07', 'ago': '08', 'set': '09', 'out': '10', 'nov': '11', 'dez': '12'
}

# Função para converter datas no formato "15 de mar. de 2024" para "15/03/2024"
def converter_data_textual(data_textual):
    padrao = re.compile(r'(\d{1,2})\s*de\s*(\w+)\.?\s*de\s*(\d{4})')
    resultado = padrao.search(data_textual)
    
    if resultado:
        dia = resultado.group(1)
        mes = resultado.group(2).lower()[:3]  # Pega os três primeiros caracteres do mês
        ano = resultado.group(3)
        
        if mes in meses:
            mes_numerico = meses[mes]
            return f"{dia.zfill(2)}/{mes_numerico}/{ano}"
        
    return data_textual  # Retorna o texto original se não encontrar um padrão válido

# Função para calcular a data baseada em expressões como "X semanas atrás", "X dias atrás" ou "X meses atrás"
def calcular_data(texto, data_base):
    padrao = re.compile(r'(\d+)\s*(semanas|dias|meses)\s*atrás')
    resultado = padrao.search(texto)

    if resultado:
        quantidade = int(resultado.group(1))
        unidade = resultado.group(2)

        if unidade == "semanas":
            dias_atras = quantidade * 7
            data_calculada = data_base - timedelta(days=dias_atras)
        elif unidade == "dias":
            dias_atras = quantidade
            data_calculada = data_base - timedelta(days=dias_atras)
        elif unidade == "meses":
            data_calculada = data_base - relativedelta(months=quantidade)

        return data_calculada.strftime('%d/%m/%Y')
    
    return texto  # Retorna o texto original se não houver expressão a ser substituída

# Função para processar a data
def processar_data(linha_data, data_base):
    linha_limpa = linha_data.replace('.', '', 1)
    data_convertida = converter_data_textual(linha_limpa)
    data_calculada = calcular_data(data_convertida, data_base)
    return data_calculada

# Função para limpar o texto
def limpar_texto(texto):
    # Remove o conteúdo do padrão superior
    padrao_superior = r"Ir para o conteúdo principal.*?Ferramentas"
    texto_limpo = re.sub(padrao_superior, '', texto, flags=re.DOTALL)

    # Divide o texto em linhas
    linhas = texto_limpo.splitlines()

    # Remove linhas vazias ou com espaços em branco
    linhas = [linha.strip() for linha in linhas if linha.strip()]

    # Junta as linhas de volta em uma única string
    texto_limpo = '\n'.join(linhas)

    return texto_limpo

# Função para classificar as linhas e adicionar o número da notícia
def classificar_linhas(texto, data_base, numero_inicial):
    linhas = texto.splitlines()
    noticias = []
    numero_noticia = numero_inicial

    for idx in range(0, len(linhas), 4):
        noticia = {}
        noticia['Número'] = numero_noticia
        if idx < len(linhas):  
            noticia['Fonte'] = linhas[idx]
        else:
            noticia['Fonte'] = ''
        if idx + 1 < len(linhas):  
            noticia['Manchete'] = linhas[idx + 1]
        else:
            noticia['Manchete'] = ''
        if idx + 2 < len(linhas):  
            noticia['Descrição'] = linhas[idx + 2]
        else:
            noticia['Descrição'] = ''
        if idx + 3 < len(linhas):
            data_final = processar_data(linhas[idx + 3], data_base)
            noticia['Data'] = data_final
        else:
            noticia['Data'] = data_base.strftime('%d/%m/%Y')
        noticias.append(noticia)
        numero_noticia += 1  # Incrementa o número da notícia
    return noticias

# Função principal para raspagem de páginas
def raspar_paginas():
    noticias = []
    data_base = datetime(2024, 9, 29)
    numero_noticia = 1

    # loop externo: cada termo de busca
    for uni in universidades:
        # monta o termo: "trote universitário" + uni (se houver)
        termo = 'trote universitário' + (f' {uni}' if uni else '')
        q = urllib.parse.quote_plus(termo)  # transforma espaços em + e acentos em %xx

        # loop interno: páginas de 0 até 44 (45 páginas -> 0..44)
        for page in range(45):
            start_value = page * 10
            url = f'https://www.google.com/search?q={q}&tbm=nws&start={start_value}'
            
            print(f"🔍 Buscando “{termo}” — página {page+1}/45")
            webbrowser.open(url)
            time.sleep(8)

            # copia todo o texto da página
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            texto = pyperclip.paste()

            # limpa e classifica (suas funções existentes)
            texto_limpo = limpar_texto(texto)
            noticias_pagina = classificar_linhas(texto_limpo, data_base, numero_noticia)
            noticias.extend(noticias_pagina)
            numero_noticia += len(noticias_pagina)

            # fecha aba e espera um pouco
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(random.uniform(5, 10))

    # grava CSV no final
    with open('noticias.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Número', 'Fonte', 'Manchete', 'Descrição', 'Data']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for noticia in noticias:
            writer.writerow(noticia)

    print("✅ 'NOTICIAS - MANCHETES.csv' gerado com sucesso!")

# Chama a função principal
raspar_paginas()
