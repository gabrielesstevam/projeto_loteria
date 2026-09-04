#---------------------IMPORTAÇÕES-------------------------------------------------
import tkinter as tk
import os
import funcoes_Projeto as funcoes
import tratamento_erros as tratamento
from erros import QuantidadeApostasError, ValoresApostaIguaisError, ValorMaiorQueMaxError
import random

#---------------------------CORES-------------------------------------------------

BG  = '#050c19'
FG  = '#99eeff'
WT  = '#ffffff'
IBG = '#0f244c'
GRN = '#00ff99'
RED = '#ff6b6b'

#---------------------CONFIG BÁSICAS DA INTERFACE---------------------------------

LIMITE_APOSTA  = 6   # quantos números cada usuário aposta
LIMITE_SORTEIO = 30  # números sorteados vão de 1 até 30

os.makedirs('csv', exist_ok=True)

apostas         = []
sorteio_feito   = False
sorteados_atual = None

#------------------FUNÇÕES DA INTERFACE-------------------------------------------

def adicionar_aposta():
    nome   = entry_nome.get().strip()
    aposta = entry_aposta.get().strip()

    if not nome:
        mostrar_status("Digite o nome do usuário.", RED)
        return

    valores = aposta.split()

    try:
        aposta_lista = tratamento.validar_aposta_valores(nome, valores, LIMITE_APOSTA, LIMITE_SORTEIO)
    except ValueError:
        mostrar_status("Aposta inválida! Use somente números inteiros.", RED)
        return
    except QuantidadeApostasError:
        mostrar_status(f"Aposta inválida! Digite exatamente {LIMITE_APOSTA} números.", RED)
        return
    except ValoresApostaIguaisError:
        mostrar_status("Aposta inválida! Não repita números.", RED)
        return
    except ValorMaiorQueMaxError:
        mostrar_status(f"Aposta inválida! Use números de 1 a {LIMITE_SORTEIO}.", RED)
        return

    if not apostas:
        funcoes.configuar_EStrutura_CSV(LIMITE_APOSTA)  # reseta csv na primeira aposta

    funcoes.guardarAposta(aposta_lista)
    apostas.append(aposta_lista)

    entry_nome.delete(0, tk.END)
    entry_aposta.delete(0, tk.END)
    entry_nome.focus()

    atualizar_historico()
    mostrar_status(f"Aposta de {nome} registrada! ✔", GRN)
    btn_sortear.config(state='normal')

def demonstracao():
    """Escolhe um nome aleatório do csv/nomes.csv, gera uma aposta aleatória e a registra."""
    import csv
 
    with open("csv/nomes.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        nomes = [linha[0] for linha in leitor if linha]
 
    nome_sorteado = random.choice(nomes)
    numeros_sorteados = random.sample(range(1, LIMITE_SORTEIO + 1), LIMITE_APOSTA)
 
    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, nome_sorteado)
    entry_aposta.delete(0, tk.END)
    entry_aposta.insert(0, " ".join(str(n) for n in numeros_sorteados))
 
    adicionar_aposta()

def realizar_sorteio():
    global sorteio_feito, sorteados_atual

    if not apostas:
        mostrar_status("Adicione pelo menos uma aposta antes de sortear.", RED)
        return

    sorteados_atual = funcoes.sortearNumeros(LIMITE_SORTEIO)
    sorteio_feito   = True

    todos = [str(n) for n in sorteados_atual]
    label_sorteados.config(text="🎱 Sorteados: " + "  ".join(todos))
    label_sorteados.pack(pady=6)

    funcoes.compararNumeros(sorteados_atual)  # salva resultados no cv
    exibir_resultados()

    btn_apostar.config(state='disabled')
    btn_sortear.config(state='disabled')
    btn_novo.config(state='normal')
    mostrar_status("Sorteio realizado!", GRN)


def exibir_resultados():
    """Lê o csv de resultados e exibe na caixa de texto"""
    import csv

    texto_resultado.config(state='normal')
    texto_resultado.delete('1.0', tk.END)

    with open('csv/resultadoApostas.csv', 'r', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            texto_resultado.insert(tk.END, f"👤 {linha['Usuarios']}\n")
            texto_resultado.insert(tk.END, f"   Acertos: {linha['Quantidade de Acrtos']}")

            acertados = linha['Numeros Acertados']
            if acertados != "[]":
                texto_resultado.insert(tk.END, f"  |  Números: {acertados}")

            if linha['Categoria'] != 'n/a':
                texto_resultado.insert(tk.END, f"\n   Categoria: {linha['Categoria'].upper()}  |  Prêmio: R$ {linha['Prêmio']},00\n")
            else:
                texto_resultado.insert(tk.END, "\n   Sem prêmio desta vez.\n")

            texto_resultado.insert(tk.END, "\n")

    texto_resultado.config(state='disabled')
    frame_resultado.pack(pady=6, padx=10, fill='x')


def novo_jogo():
    global apostas, sorteio_feito, sorteados_atual
    apostas         = []
    sorteio_feito   = False
    sorteados_atual = None

    entry_nome.delete(0, tk.END)
    entry_aposta.delete(0, tk.END)
    label_sorteados.config(text="")
    label_sorteados.pack_forget()
    frame_resultado.pack_forget()

    texto_historico.config(state='normal')
    texto_historico.delete('1.0', tk.END)
    texto_historico.config(state='disabled')

    btn_apostar.config(state='normal')
    btn_sortear.config(state='disabled')
    btn_novo.config(state='disabled')

    mostrar_status("Novo jogo iniciado!", GRN)
    entry_nome.focus()


def atualizar_historico():
    texto_historico.config(state='normal')
    texto_historico.delete('1.0', tk.END)
    for ap in apostas:
        numeros = "  ".join(str(n) for n in ap[1:])
        texto_historico.insert(tk.END, f"{ap[0]:15s}  →  {numeros}\n")
    texto_historico.config(state='disabled')


def mostrar_status(msg, cor=FG):
    label_status.config(text=msg, fg=cor)

#-------------------------JANELA--------------------------------------------------

janela = tk.Tk()
janela.title('Simulador de Loteria - TSI')
janela.config(bg=BG)
janela.geometry('500x620')
janela.resizable(False, False)


frame_cadastro = tk.Frame(janela)
frame_loteria = tk.Frame(janela)

#---------------------------------------------------------------------------------

#-------------------WIDGETS DA JANELA DE CADASTRAMENTO----------------------------
frame_cadastro.pack()

tk.Label(
    janela, 
    text='🍀 Loteria TSI', 
    font=('Arial', 18, 'bold'), 
    bg=BG, 
    fg=WT
).pack(pady=6)


frame_aposta = tk.Frame(
    janela, 
    bg=BG
)
frame_aposta.pack(pady=4)


tk.Label(
    frame_aposta, 
    text='Nome do usuário:', 
    bg=BG, 
    fg=FG
).grid(row=0, column=0, sticky='w')


entry_nome = tk.Entry(
    frame_aposta, 
    width=22, 
    font=('Arial', 11), 
    bg=IBG, 
    fg=WT, 
    relief='flat', 
    bd=6, 
    insertbackground=WT
)
entry_nome.grid(row=0, column=1, padx=6, pady=3)


tk.Label(
    frame_aposta, 
    text=f'{LIMITE_APOSTA} números (1–{LIMITE_SORTEIO}):', 
    bg=BG, 
    fg=FG
).grid(row=1, column=0, sticky='w')


entry_aposta = tk.Entry(
    frame_aposta, 
    width=22, 
    font=('Arial', 11), 
    bg=IBG, 
    fg=WT, 
    relief='flat', 
    bd=6, 
    insertbackground=WT
)
entry_aposta.grid(row=1, column=1, padx=6, pady=3)


frame_botoes = tk.Frame(
    janela, 
    bg=BG
)
frame_botoes.pack(pady=6)


btn_apostar = tk.Button(
    frame_botoes, 
    text='➕ Adicionar Aposta', 
    command=adicionar_aposta, 
    width=18, 
    bg=FG, 
    fg=BG, 
    relief='flat', 
    cursor='hand2', 
    activebackground=FG, 
    font=('Arial', 10, 'bold')
)
btn_apostar.grid(row=0, column=0, padx=5)


btn_sortear = tk.Button(
    frame_botoes, 
    text='▶ Realizar Sorteio', 
    command=realizar_sorteio, 
    width=18, 
    bg=FG, 
    fg=BG, 
    relief='flat', 
    cursor='hand2', 
    activebackground=FG, 
    font=('Arial', 10, 'bold'), 
    state='disabled'
)
btn_sortear.grid(row=0, column=1, padx=5)


btn_novo = tk.Button(
    frame_botoes, 
    text='🔄 Novo Jogo', 
    command=novo_jogo, 
    width=18, 
    bg=IBG, 
    fg=FG, 
    relief='flat', 
    cursor='hand2', 
    activebackground=IBG, 
    font=('Arial', 10, 'bold'), 
    state='disabled'
)
btn_novo.grid(row=0, column=2, padx=5)

btn_demo = tk.Button(
    frame_botoes, 
    text='🎲 Demonstração', 
    command=demonstracao, 
    width=18, 
    bg=IBG, 
    fg=FG, 
    relief='flat', 
    cursor='hand2', 
    activebackground=IBG, 
    font=('Arial', 10, 'bold')
)
btn_demo.grid(row=1, column=0, columnspan=3, pady=(6, 0))

label_status = tk.Label(
    janela, 
    text='', 
    font=('Arial', 10), 
    bg=BG, 
    fg=FG
)
label_status.pack()


label_sorteados = tk.Label(
    janela, 
    text='', 
    font=('Arial', 12, 'bold'), 
    bg=BG, 
    fg=GRN
)
label_sorteados.pack_forget()


frame_resultado = tk.Frame(
    janela, 
    bg=BG
)


tk.Label(
    frame_resultado, 
    text='Resultados', 
    font=('Arial', 11, 'bold'), 
    bg=BG, 
    fg=FG
).pack(anchor='w')


texto_resultado = tk.Text(
    frame_resultado, 
    width=58, 
    height=7, 
    font=('Courier', 9), 
    state='disabled', 
    bg=IBG, 
    fg=WT, 
    relief='flat'
)
texto_resultado.pack()


frame_resultado.pack_forget()


tk.Label(
    janela, 
    text='Histórico de apostas', 
    font=('Arial', 11, 'bold'), 
    bg=BG, 
    fg=FG
).pack(pady=(8, 2))


texto_historico = tk.Text(
    janela, 
    width=58, 
    height=6, 
    font=('Courier', 9), 
    state='disabled', 
    bg=IBG, 
    fg=WT, 
    relief='flat'
)
texto_historico.pack(padx=10, pady=(0, 10))

entry_nome.focus()

#---------------------------------------------------------------------------------

janela.mainloop() #ativação da janela em loop infinito