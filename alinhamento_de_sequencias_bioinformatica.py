#variáveis globais
seq1 = "TTAACTTTACTATT"
seq2 = "TTCTGTTGATT"

acerto = 2
erro = -3
espaco = -2



def custoAlinhamento(i, j):
    if(seq1[j] == seq2[i]):
        return acerto
    return erro

def preencher():
    matriz = []
    for i in range(len(seq2)+1):
        linha = []
        for j in range(len(seq1)+1):
            linha.append(-10000) #valor aleatório definido para não interferir na análise das posições e não gerar conflito durante os cálculos
        matriz.append(linha)

    #preenchimento inicial dos espaços
    for i in range(len(seq2)+1):
        matriz[i][0] = espaco * i
    for j in range(len(seq1)+1):
        matriz[0][j] = espaco * j
    #preenchimento seguindo a lógica do maior valor
    for i in range(1, len(seq2)+1):
        for j in range(1, len(seq1)+1):
            A = matriz[i-1][j-1] + custoAlinhamento(i-1, j-1)
            B = matriz[i][j-1] + espaco
            C = matriz[i-1][j] + espaco
            matriz[i][j] = max(A, B, C)

    return matriz

def alinhar(matrizValores):
    alinhamentoA = ""
    alinhamentoB = ""
    i = len(seq2)
    j = len(seq1)
    while i > 0 and j > 0:
        valorAtual = matrizValores[i][j]
        valorDiagonal = matrizValores[i-1][j-1]
        valorVertical = matrizValores[i][j-1]
        valorHorizontal = matrizValores[i-1][j]
        if valorAtual == valorDiagonal + custoAlinhamento(i-1, j-1):
            alinhamentoA += seq2[i-1]
            alinhamentoB += seq1[j-1]
            i -= 1
            j -= 1
        elif valorAtual == valorHorizontal + espaco:
            alinhamentoA += seq2[i-1]
            alinhamentoB += "-"
            i -= 1
        elif valorAtual == valorVertical + espaco:
            alinhamentoA += "-"
            alinhamentoB += seq1[j-1]
            j -= 1
    while i > 0:
        alinhamentoA += seq2[i-1]
        alinhamentoB += "-"
        i -= 1
    while j > 0:
        alinhamentoA += "-"
        alinhamentoB += seq1[j-1]
        j -= 1
    alinhamentoA = alinhamentoA[::-1]
    alinhamentoB = alinhamentoB[::-1]
    return [alinhamentoA, alinhamentoB]



if __name__ == "__main__":
    matrizValores = preencher()
    alinhamento = alinhar(matrizValores)
    arquivo = open('resolucaoAlinhamentoDeSequenciasIsabelle.txt', 'w') #criando um arquivo para armazenar a solução
    arquivo.write("TRABALHO DE ALINHAMENTO DE SEQUENCIAS \nALUNA: Isabelle Rodrigues Coelho \n")
    arquivo.write("\nAlinhamento ótimo encontrado: \n")
    arquivo.write(alinhamento[0] + "\n")
    arquivo.write(alinhamento[1] + "\n")
    arquivo.write("\n Para executar o código basta escrever a seguinte linha de comando: \n python3 alinhamento_de_sequencias_bioinformatica.py")