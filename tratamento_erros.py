from erros import QuantidadeApostasError, ValoresApostaIguaisError, ValorMaiorQueMaxError # importação dos erros criados

def obter_quantidade_usuario(mensagem): # verifica se digitou um número inteiro
    while True:
        try:
            quantidade = int(input(mensagem))
            return quantidade
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def obter_valores_aposta(mensagem, nomeUsuario, limiteAposta, maxAposta): # verifica erros de aposta [  ]
    while True:
        try:
            valores_aposta = input(mensagem).split()
            valores_aposta_int = [int(x) for x in valores_aposta]

            for i in valores_aposta_int: # vrf: se a aposta é acima ou abaixo do limite
                if (i > maxAposta) or (i <= 0):
                    raise ValorMaiorQueMaxError
            if len(valores_aposta_int) != limiteAposta: # vrf: se é diferente da quantidade delimitada de apostas
                raise QuantidadeApostasError
            elif len(set(valores_aposta_int)) < len(valores_aposta_int): # vrf: se alguma das apostas são iguais
                raise ValoresApostaIguaisError
            else: # caso não ocorra erro, será retornado a aposta do usuário
                usuario_aposta = [nomeUsuario] + valores_aposta_int
                return usuario_aposta
        except ValueError:
            print("Erro: Você digitou uma letra ou caractere inválido! Use apenas números inteiros.")
        except QuantidadeApostasError:
            print(f"\nAposta Inválida | Aposte em {limiteAposta} números \n")
        except ValoresApostaIguaisError:
            print("Aposta Inválida | Aposte em números diferentes \n")
        except ValorMaiorQueMaxError:
            print(f"Aposta Inválida | Aposte em números de 1-{maxAposta} \n")


# FUNÇÃO PONTE, APENAS CHAMA AS FUNÇÕES DO TRATAMENTO DE ERRO, JÁ QUE TKINTER NÃO USA IMPUT.

def validar_aposta_valores(nomeUsuario, valores_aposta, limiteAposta, maxAposta):
    valores_aposta_int = [int(x) for x in valores_aposta]
    for i in valores_aposta_int:
        if (i > maxAposta) or (i <= 0):
            raise ValorMaiorQueMaxError
    if len(valores_aposta_int) != limiteAposta:
        raise QuantidadeApostasError
    elif len(set(valores_aposta_int)) < len(valores_aposta_int):
        raise ValoresApostaIguaisError
    return [nomeUsuario] + valores_aposta_int