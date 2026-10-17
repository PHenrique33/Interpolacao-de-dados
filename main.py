import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from TXTToCSV import *

np.set_printoptions(suppress=True, precision=4)

dados = [
         "aproximacaoRpm16x6_8400", "aproximacaoRpm16x8_8400", "aproximacaoRpm16x10_8400",
         "aproximacaoRpm17x6_7900", "aproximacaoRpm17x8_7900", "aproximacaoRpm17x10_7900",
         "aproximacaoRpm18x6_7500", "aproximacaoRpm18x8_7500", "aproximacaoRpm18x10_7500",
         "aproximacaoRpm19x6_7100", "aproximacaoRpm19x8_7100", "aproximacaoRpm19x10_7100",
         "aproximacaoRpm20x6_6700", "aproximacaoRpm20x8_6700", "aproximacaoRpm20x10_6700"]

numGraficos = range(1, len(titulos)+1)



posicao = -1
for i in range(len(dados)):
    print(f"{i}- {dados[i]}")

posicao = int(input("\nqual dado voce deseja ver: "))
while posicao<0 or posicao>len(dados):
    posicao = int(input("dado invalido, tente novamente: "))



aproximacao = int(dados[posicao][-3])
numeroPrincipal = int(dados[posicao][-4])
proporcao = dados[posicao].split("m")[2].split("_")[0]

RpmMenor = pd.read_csv(f"data\\{numeroPrincipal}{aproximacao}00rpm\\{proporcao}\\{numeroPrincipal}000rpm.csv").to_numpy()
RpmMaior = pd.read_csv(f"data\\{numeroPrincipal}{aproximacao}00rpm\\{proporcao}\\{numeroPrincipal+1}000rpm.csv").to_numpy()
aproximacaoRpm = np.round((RpmMaior*aproximacao+RpmMenor*(10-aproximacao))/10, 4)
aproximacaoRpm = TransformarCSV(f"aproximacaoRpm{proporcao}_{numeroPrincipal}{aproximacao}00", titulos, aproximacaoRpm)





for i in numGraficos:
    plt.subplot(3,5,i)
    plt.title(f"{titulos[i-1]}")
    plt.plot(range(len(aproximacaoRpm[f"{titulos[i-1]}"])), aproximacaoRpm[f"{titulos[i-1]}"])

plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig(f"data\\Imagens\\{dados[posicao]}")
plt.show()
