#-- Imports ------------------------------------------------------------------------
import csv # manipulação de arquivo csv
import funcoes_Projeto as funcoes # importa as funções do projeto
import tratamento_erros as tratamento # importa os tratamentos de erros
#-- Variáveis ------------------------------------------------------------------------
limiteAposta = 6 # define a quantidade de números que o usuário pode apostar
limiteSorteio = 30 # define o número máximo que um número da aposta pode chegar
#-- Sistema ------------------------------------------------------------------------

funcoes.configuar_EStrutura_CSV(limiteAposta) # reseta os arquivos csv

Quant_usuario = tratamento.obter_quantidade_usuario("Quantos usuarios: ") # [[tratamento]]

for i in range(Quant_usuario): # pergunta -> recebe -> guarda as apostas

    nomeUsuario = input(f"Qual o nome do {i+1}° usuário?: ")

    aposta = tratamento.obter_valores_aposta(f"{nomeUsuario}, escolha {limiteAposta} números para apostar: ", nomeUsuario, limiteAposta, limiteSorteio) # [[tratamento]]
    
    funcoes.guardarAposta(aposta) # guarda aposta no respectivo csv

#--------------------------------------------------------------------------
print('======== Números Sorteados ========\n')

sorteados = funcoes.sortearNumeros(limiteSorteio) # sorteia os números
for num in sorteados:
    print(num, end=' ')

funcoes.compararNumeros(sorteados) # compara sorteio com apostas, e guarda o resultado em csv

#--------------------------------------------------------------------------
print('\n\n======== Resultados ========')

with open('csv/resultadoApostas.csv', "r", encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo) 
    
    for linha in leitor: # mostra no terminal o resultado de cada usuário 
        print(f"\n{linha['Usuarios']}:") #nome
        print(f"Total de acertos: {linha['Quantidade de Acrtos']}") # acertos
        
        if linha['Numeros Acertados'] != "[]": # caso não tenha acertado nada, nao mostra nada
            print(f"Numeros acertados: {linha['Numeros Acertados']}")
            
        if linha['Categoria'] != "n/a": # caso não tenha acertado mais que 3, não concorre ao prêmio
            print(f"Categoria em que concorreu: {linha['Categoria']}")
            print(f"Quantia recebida: R$ {linha['Prêmio']},00")
        else:
            print(f"Você não acertou suficiente para concorrer em uma categoria")
            print(f"Não recebeu nada")
        