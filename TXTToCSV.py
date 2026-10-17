import os
import csv
import numpy as np
import pandas as pd



np.set_printoptions(suppress=True, precision=4)

base = "C:\\Users\\PEDRO\\Desktop\\Interpolação de Dados\\data"

arquivosCsv = []
arquivosTxt = []

for base, pastas, textos in os.walk(base):
    for texto in textos:
        if texto.endswith(".txt"):
            caminho_completo = os.path.join(base, texto)
            arquivosTxt.append(caminho_completo)


arquivosCsv = []
titulos = 0
for arquivo in arquivosTxt:
    arquivosCsv.append(f"{arquivo[:-3]}csv")

for i in range(len(arquivosTxt)):
    with open(arquivosTxt[i], "r", encoding="utf-8") as rpm8:
        dados = rpm8.read().splitlines()    
        titulos = dados[0].split()

    with open(f"{arquivosCsv[i]}", "w", newline="", encoding="utf-8") as saida:
        escritor = csv.writer(saida)

        for linha in dados:
            valores = linha.split()

            if len(valores)==15:
                escritor.writerow(valores)


def TransformarCSV(nomeDoArquivo, titulo, informacaoNumpy):
    with open(f"data\\Aproximacoes\\{nomeDoArquivo}.csv", "w", newline="", encoding="utf-8") as aproximacao:
        escritor = csv.writer(aproximacao)
        escritor.writerow(titulo)
        for linha in informacaoNumpy:
            escritor.writerow(linha)

    return pd.read_csv(f"data\\Aproximacoes\\{nomeDoArquivo}.csv")