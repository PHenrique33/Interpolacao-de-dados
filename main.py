import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from TXTToCSV import *

np.set_printoptions(suppress=True, precision=4)

rpm16x6_8 = pd.read_csv("data\\8437.5rpm\\16x6\\8000rpm.csv")
rpm16x6_9 = pd.read_csv("data\\8437.5rpm\\16x6\\9000rpm.csv")

rpm16x8_8 = pd.read_csv("data\\8437.5rpm\\16x8\\8000rpm.csv")
rpm16x8_9 = pd.read_csv("data\\8437.5rpm\\16x8\\9000rpm.csv")

rpm16x10_8 = pd.read_csv("data\\8437.5rpm\\16x10\\8000rpm.csv")
rpm16x10_9 = pd.read_csv("data\\8437.5rpm\\16x10\\9000rpm.csv")


# dá pra transformar em loop for provavelmente, mas ainda não sei como vou fazer isso

if True: #para 16x6 / 8000RPM
    numpy16x6_8 = rpm16x6_8.to_numpy()
    numpy16x6_9 = rpm16x6_9.to_numpy()
    aproximacaoRpm16x6_8400 = np.round((numpy16x6_8*3+numpy16x6_9*2)/10, 4)
    aproximacaoRpm16x6_8400 = TransformarCSV("16x6 rpm8400", titulos, aproximacaoRpm16x6_8400)
if True: #para 16x8 / 8000RPM
    numpy16x8_8 = rpm16x8_8.to_numpy()
    numpy16x8_9 = rpm16x8_9.to_numpy()
    aproximacaoRpm16x8_8400 = np.round((numpy16x8_8*3+numpy16x8_9*2)/10, 4)
    aproximacaoRpm16x8_8400 = TransformarCSV("16x8 rpm8400", titulos, aproximacaoRpm16x8_8400)
if True: #para 16x10 / 8000RPM
    numpy16x10_8 = rpm16x10_8.to_numpy()
    numpy16x10_9 = rpm16x10_9.to_numpy()
    aproximacaoRpm16x10_8400 = np.round((numpy16x10_8*3+numpy16x10_9*2)/10, 4)
    aproximacaoRpm16x10_8400 = TransformarCSV("16x10 rpm8400", titulos, aproximacaoRpm16x10_8400)

dados = [aproximacaoRpm16x6_8400, aproximacaoRpm16x8_8400, aproximacaoRpm16x10_8400]
numGraficos = range(1, len(titulos)+1)


posicao = 0
while 1>posicao or posicao>3:
    posicao = int(input("digite o grafico que deseja ver?\n1-16x6 8400rpm\n2-16x8 8400rpm\n3-16x10 8400rpm"))

for i in numGraficos:
    plt.subplot(3,5,i)
    plt.title(f"{titulos[i-1]}")
    plt.plot(range(len(dados[posicao][f"{titulos[i-1]}"])), dados[posicao][f"{titulos[i-1]}"])

plt.show()
