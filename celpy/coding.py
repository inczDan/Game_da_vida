import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# convertendo numeros int em binarios
def converte_binario(numero):
    binario = bin(numero)
    binario = binario[2:]
    if len(binario) < 8:
        zeros = [0] * (8 - len(binario))
    binario = zeros + list(binario)
    return list(binario)


# script
MAX = 500  # tamanho da grade
g = np.zeros(1000)  # tamanho da geração
ng = np.zeros(1000)  # tamanho da nova geração
regra = int(input("Entrada númerica: "))
codigo = converte_binario(regra)

# matriz que cada linha armazena uma geração de celulas
matriz_evolucao = np.zeros((MAX, len(g)))  # 500 linhas por 1000 columns

# definindo geração inicial pra começar com uma celula viva.
g[len(g) // 2] = 1  # tamanho da geracao inicial com divisao inteira por 2 = 500
# isso coloca uma celula viva na metade da matriz


# for p atualizar as gerações
for i in range(MAX):
    matriz_evolucao[i, :] = g
    # percorre celulas da geração atual
    for j in range(len(g)):  # indo de 0 a 1000 -1
        if g[j - 1] == 0 and g[j] == 0 and g[(j + 1) % len(g)] == 0:
            ng[j] = int(codigo[7])
            # se a posição na matriz(g) for j-1, e for == 0
            # e se for j, e for == 0 e se j+1 com modulo pelo tamanho de (g) == 0
            # receberá 0, pq o codigo 7 na tabela de binarios é 0
        # isso serve para os casos de elif abaixo
        elif g[j - 1] == 0 and g[j] == 0 and g[(j + 1) % len(g)] == 1:
            ng[j] = int(codigo[6])
        elif g[j - 1] == 0 and g[j] == 1 and g[(j + 1) % len(g)] == 0:
            ng[j] = int(codigo[5])
        elif g[j - 1] == 0 and g[j] == 1 and g[(j + 1) % len(g)] == 1:
            ng[j] = int(codigo[4])
        elif g[j - 1] == 1 and g[j] == 0 and g[(j + 1) % len(g)] == 0:
            ng[j] = int(codigo[3])
        elif g[j - 1] == 1 and g[j] == 0 and g[(j + 1) % len(g)] == 1:
            ng[j] = int(codigo[2])
        elif g[j - 1] == 1 and g[j] == 1 and g[(j + 1) % len(g)] == 0:
            ng[j] = int(codigo[1])
        elif g[j - 1] == 1 and g[j] == 1 and g[(j + 1) % len(g)] == 1:
            ng[j] = int(codigo[0])
            # lendo da geração g e escrevendo na ng, que irá
            # formar a nova geração(linha de baixo)

    g = ng.copy()  # caso só atribua, os vetores geram erro

# plot
plt.figure(1)
plt.axis("off")
plt.imshow(matriz_evolucao, cmap="gray")
plt.savefig("Automata.png", dpi=300)
plt.show()
