import csv
import pandas as pd
import numpy as np

np.set_printoptions(suppress=True, precision=4)

arquivo16x6_8000 =   "data\\8437.5rpm\\16x6\\8000rpm.txt"
arquivo16x6_9000 =   "data\\8437.5rpm\\16x6\\9000rpm.txt"
arquivo16x8_8000 =   "data\\8437.5rpm\\16x8\\8000rpm.txt"
arquivo16x8_9000 =   "data\\8437.5rpm\\16x8\\9000rpm.txt"
arquivo16x10_8000 = "data\\8437.5rpm\\16x10\\8000rpm.txt"
arquivo16x10_9000 = "data\\8437.5rpm\\16x10\\9000rpm.txt"

arquivos = [arquivo16x6_8000, arquivo16x6_9000,
            arquivo16x8_8000, arquivo16x8_9000,
            arquivo16x10_8000, arquivo16x10_9000]

arquivosCsv = []
titulos = 0
for arquivo in arquivos:
    arquivosCsv.append(f"{arquivo[:-3]}csv")

for i in range(len(arquivos)):
    with open(arquivos[i], "r", encoding="utf-8") as rpm8:
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