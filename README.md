<h1 align=center>Simulador de Loteria</h1> 

<h6 align=center>Projeto universitário desenvolvido para fins avaliativos, com o objetivo de criar um jogo de loteria utilizando Python e a biblioteca Tkinter.</h6>

> <h2>Sumário</h2>

1. Desenvolvedores
2. Funcionalidades
3. Tecnologias Utilizadas 
4. Requisitos/Instalações
    - 4.1. Python
    - 4.2. Tkinter
    - 4.3. Arquivos do Sistema
5. Execução
6. Como utilizar o sistema

> <h2>1. Desenvolvedores</h2>

- *Alana Kelly Basilio da Silva* <br>
- *Alex Bruno Ramos Ferreira* <br>
- *Gabriel dos Santos Fernandes Estevam*<br>
- *Isac Emanuel da Silva Costa* <br>
- *Izaias Rodrigues Dantas* <br>

> <h2>2. Funcionalidades</h2>

- *Geração de números aleatórios* <br>
- *Registro de múltiplas apostas* <br>
- *Verificação de resultados* <br>
- *Divisão de prêmios proporcional às categorias* <br>
- *Tratamento de erros* <br>
- *Armazenamento de dados em arquivos csv* <br>
- *Interface gráfica*

> <h2>3. Tecnologias Utilizadas</h2>

- `Python 3.14.6` <br>
- `Bibliotecas {Tkinter, Random, csv e os}`
- `Git`
- `VScode`

> <h2>4. Requisitos/Instalações</h2>

Antes de rodar o projeto, é importante que tenha o `Python` e o `Tkinter` instalado na sua máquina. Caso não os tenha, siga o passo a passo.

Bibliotecas como `Random`, `csv` e `os` não necessitam de instalação individual, são bibliotecas nativas do `Python`.

> <h3>4.1. Python</h3>

1. Acesse o site oficial para instalar o `Python` : [Acesse aqui](https://www.python.org/Downloads/).

2. Baixe a versão `3.14.6` do `Python` para o seu sistema operacional. Após isso, execute o instalador.

3. Durante a instalação, caso seu sistema  operacional seja `Windows`, marque a opção `"Add Python to Path"` antes de clicar em instalar.

4. Após a instalação, pressione `Windows + R`, e escreva `cmd`. Após o terminal abrir, escreva esta linha de comando para verificar se a instalação do `Python` na sua máquina deu certo:
```bash
python --version 
```
5. Caso não obtenha resposta, e seu sistema operacional não seja  `Windows`, tente digitar:
```bash
python3 --version 
```
6. Após inserir a linha de comando, se você recebeu como resposta o número da versão como (`Python 3.14.6`), a instalação foi concluída com sucesso.

> <h3>4.2. Tkinter</h3>

1. O `tkinter` geralmente já vem junto com o `Python` no `Windows` e no `Mac`. Para verificar, digite no terminal:

```bash
python -m tkinter
```
2. Caso um pequena janela tenha sido aberta, o `Tkinter `já está instalado e você não precisa fazer mais nada.

3. Se o `Tkinter` não foi instalado e seu sistema operacional é `Windows`, reinstale o `Python`, marcando a opção `Add Python to PATH` caso não tenha sido marcada anteriormente.

4. Para instalar o `Tkinter` individualmente, utilize o comando correspondente ao seu sistema operacional:

- `Mac`:
```bash
brew install python-tk
```
- `Linux [Ubuntu / Debian]`:
```bash
sudo apt-get install python3-tk
```
- `Linux [Fedora]`:
```bash
sudo dnf install python3-tkinter
```
- `Linux [Arch]`:
```bash
sudo pacman -S tk
```
> <h3>4.3. Arquivos do sistema</h3>

É possível obter os arquivos do sistema de duas formas
1. Clonagem do repositório
2. Baixando manualmente os arquivos do sistema

> <h3>4.3.1. Clonagem do repositório</h3>

1. Acesse o link oficial para instalar o `git` : [Acesse aqui](https://git-scm.com/install/).

2. Faça o download do `git`, de forma que seja compatível com seu sistema operacional, após o download, execute o instalador.

3. No processo de instalação, basta clicar em Next na maioria das telas.

- As opções recomendadas são:
    - Editor padrão: Visual Studio Code (caso instalado) ou Vim.
    - PATH: Git from the command line and also from 3rd-party software.
    - HTTPS: Use the OpenSSL library.
    - Line Ending: Checkout Windows-style, commit Unix-style 5.5.line endings.

4. Para verificar se a instalação do Git foi concluída, abra novamente o `cmd` e digite :
```bash
git --version
```
5. Caso a resposta for exibida desta forma, a instalação foi concluída com sucesso.
```bash
git version 2.50.1.windows.1
```
6. Quando instalar o `git`, abra a pasta de Downloads via `cmd`, e logo após clone o repositório do projeto utilizando o link disponibilizado abaixo.
```bash
cd Downloads

git clone https://github.com/disciplina-ilp/projeto-grupo_01-alana_alex_gabriel_isac_izaias.git
```
> <h3>4.3.2. Baixando manualmente os arquivos</h3>

1. Nesta mesma página, suba a tela e clique em `Code`, e logo depois, clique em `Download Zip`
2. Os arquivos do sistema serão baixados automaticamente, em uma pasta zip
3. Após o download, entre na pasta Downloads no seu Explorador de Arquivos, e extraia os arquivos da pasta `projeto-grupo_01-alana_alex_gabriel_isac_izaias-main.zip`.
   - Para uma melhor organização dos arquivos, recomenda-se seguir este passo a passo:
       1. Após extrair os arquivos, entre na pasta que foi criada, selecione a única pasta, e pressione `Control + X`
       2. Retorne para pasta de Downloads, pressione `Control + V`, e depois disso, exclua o arquivo ZIP, e a pasta que ficou vazia.

> <h2>5. Execução</h2>

1. Entre na pasta de Download do Explorador de Arquivos e execute o arquivo `Interface_tkinter.py`

> <h2>6. Como utilizar o sistema</h2>

1. Informe os usuários que irão participar, informando o nome dos usuários e os números apostados. Ao final de cada atribuição de usuário, clique em `Adicionar Aposta`, para salvar no histórico.

    - É possível adicionar usuários com apostas aleatórias apenas clicando em `Demonstração`. 

2. Após informar as apostas, clique em `Realizar sorteio`, para que os resultados sejam exibidos, e os prêmios sejam distribuídos.
    - Os prêmios são ditribuidos individualmente e proporcionalmente entre 3 categorias:
        - Sena - Acertou todos os 6 números : R$ 1.000.000
        - Quina - Acertou 5 números : R$ 500.000
        - Quadra - Acertou 4 números : R$ 450.000
        - Caso não tenha acertado pelo menos 4 números, não disputará os prêmios
    - Para cada categoria, o prêmio será dividido igualmente entre os ganhadores da mesma categoria.

3. Após o resultado ser divulgado, torna-se possível reiniciar o sistema para realizar novas apostas, com números sorteados diferentes.
    - Depois de realizado o sorteio, é necessário que o sistema seja reiniciado para ser possível adicionar mais apostas.
