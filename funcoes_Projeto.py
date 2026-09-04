import os # manipulação do terminal
import csv # arquivos csv
import random # número aleatórios

def sortearNumeros(limite): ### sorteia números e os guarda em uma lista
    '''
    sorteia --> compara repetição --> retorna números sorteados | refaz o sorteio
    '''
    while True:
        numerosSorteados=[] # lista para armazenar números sorteados

        for i in range(6): # sorteia e guarda na lista                     
            numerosSorteados.append(random.randint(1, limite)) # Sorteia um limite de números para cada linha

        if len(set(numerosSorteados)) < len(numerosSorteados): # verifica diferença da lista "compressa" com a original
            continue # refaz um novo sorteio
        else:
            return numerosSorteados # retorna os números sorteados

def compararNumeros(sorteados):### compara números sorteados e apostados, e guarda o resultado no csv
    '''
    resgata resultados [qntAcertos; numAcertos; categoria] --> compara acertos de usuários --> distribui os prêmios --> guarda resultado completo no csv
    '''
    numeros_sorteados = [num for num in sorteados] # converte para uma lista simples
    resultados = [] # resultado de todos os usuários
    premiosCategoria = {"sena":1000000,"quina":500000,"quadra":350000} # atribui o valor total para cada categoria
    qntCategoria = {"sena":0,"quina":0,"quadra":0} # quantidade de cada categoria [alterado de acordo com sistema]

    with open('csv/apostas.csv', "r", encoding="utf-8") as arquivo: # csv-aposta
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            # variáveis iniciais de cada usuário ------
            num_acertados = []
            usuarios = linha.get("Usuarios")
            quantidadeAcertos = 0
            categoria = "n/a" 
            premio = 0 

            for chave in linha: # verifica números acertados
                if chave != "Usuarios":
                    if int(linha[chave]) in numeros_sorteados:
                        quantidadeAcertos += 1
                        num_acertados.append(int(linha[chave]))              
            match quantidadeAcertos: # verifica categoria que vai concorrer
                case 6:
                    categoria = "sena"
                case 5:
                    categoria = "quina"
                case 4:
                    categoria = "quadra" 
            if categoria != "n/a": # se tiver concorrendo a alguma categoria, é contado
                qntCategoria[categoria] += 1 

            resultados.append({ # guarda todos os resultados [dicionário temporário]
                "usuario":usuarios,
                "quantidadeAcertos":quantidadeAcertos,
                "num_acertados":num_acertados,
                "categoria":categoria,
                "premio":premio
            })          
    with open('csv/resultadoApostas.csv', "a", newline="", encoding="utf-8") as arquivo: # csv-resultados
        escritor = csv.writer(arquivo)
        for usu in resultados:
            if usu["categoria"] != "n/a": # se estiver concorrendo a alguma categoria
                usu["premio"] = premiosCategoria[usu["categoria"]] // qntCategoria[usu["categoria"]] # divisão proporcional do prêmio, pela quantidade de cada categoria

            resultadoToCsv = usu.values() # guarda o resultado em uma lista
            escritor.writerow(resultadoToCsv) # guarda no csv
            with open("csv/historico.csv","a", newline="",encoding="utf-8") as arquivoHist:
                escritorHist = csv.writer(arquivoHist)
                escritorHist.writerow(resultadoToCsv)
         
def configuar_EStrutura_CSV(limite): ### reseta o arquivo csv
    '''
    cria a estrutura --> implementa no csv
    '''
    # csv-apostas ----------------------------------------------------
    colunasApostas = ["Usuarios"] + [f"N{x}°" for x in range(1,limite + 1)] # cabeçalho das apostas
    with open('csv/apostas.csv', 'w', newline='', encoding="utf-8") as arquivo: # csv-aposta
        escritor = csv.writer(arquivo)
        escritor.writerow(colunasApostas) # sobrescreve o arquivo

    # csv-resultados ----------------------------------------------------
    colunasResultado = ["Usuarios", "Quantidade de Acrtos", "Numeros Acertados", "Categoria", "Prêmio"] # cabeçalho dos resultados
    with open('csv/resultadoApostas.csv', "w", newline='', encoding='utf-8') as arquivo: # csv-resultado
        escritor = csv.writer(arquivo)
        escritor.writerow(colunasResultado) # sobrescreve o arquivo

def guardarAposta(aposta): ### guarda as apostas no csv
    '''
    recebe --> guarda no csv
    '''
    with open("csv/apostas.csv", "a", newline="", encoding="utf-8") as arquivo: #csv-aposta
        write = csv.writer(arquivo)
        write.writerow(aposta) # guarda a aposta no arquivo csv

def demonstracao(limite): ### simula o sistema de aposta
    '''
    configura csv --> gera números de aposta e de sorteio --> guarda as apostas no csv --> compara apostas e números sorteados --> guarda os resultados no csv
    '''
    listaNomes,numerosApostados = [],[]
    numerosSorteados = sortearNumeros(limite) # recebe números sorteados
    configuar_EStrutura_CSV(limite) # configura os arquivos csv

    for aposta in range(6): # sorteia os números que serão apostados
        numerosApostados += [random.sample(range(1,30),limite)] 
    
    with open("csv/nomes.csv", "r", newline="", encoding="utf-8") as arquivo: # csv-nomes
        leitor = csv.reader(arquivo)
        for i in leitor:
            if i: # se a linha não estiver vazia
                listaNomes.append(i[0]) # resgata apenas o nome
        listaNomes = random.sample(listaNomes,4) # 4 nomes diferentes

        for i in range(len(listaNomes)):            
            guardarAposta([listaNomes[i]] + numerosApostados[i]) # guarda a aposta do usuário no arquivo csv

    compararNumeros(numerosSorteados) # compara os números sorteados com as apostas e guarda o resultado
             
             
       
