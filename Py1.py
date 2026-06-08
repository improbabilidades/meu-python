import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    **Universidade da Costa Rica** | Escola de Engenharia Elétrica

    *IE0405 - Modelos Probabilísticos de Sinais e Sistemas*

    ### `PyX` - Série de tutoriais em Python para análise de dados

    # `Py1` - *Funções e bibliotecas padrão*

    > Dentro das bibliotecas padrão do Python há ferramentas úteis para operações numéricas básicas, para o manuseio de arquivos como os que serão aplicados no curso e outras funções úteis para programação em geral.

    *Fabián Abarca Calderón*

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Funções, bibliotecas e métodos

    Em programação, geralmente se aceita que "não há que reinventar a roda" e também que "não há que se repetir", e além disso que "é preciso mantê-lo simples". Para não esquecer isso, existem estes acrônimos:

    * **DRY**, *don't repeat yourself*
    * **KISS**, *keep it simple, stupid*

    Uma forma de seguir estes bons conselhos é criando funções que são invocadas quando há tarefas repetitivas, e também utilizando peças de código ("bibliotecas") que já foram desenvolvidas para resolver aplicações específicas.

    A existência de funções e bibliotecas (com seus módulos e métodos associados), desenvolvidas por uma imensa comunidade global, agrega muitas funcionalidades poderosas ao Python.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 1.1 - Funções

    Em Python, a sintaxe para a criação de uma função é:

    ```python
    def nombre():
        <ação da função>
    ```
    """)
    return


@app.cell
def _():
    def suma(x, y):
        z = x + y
        return z

    print(suma(1, 2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1.2 - Bibliotecas, módulos, métodos e atributos

    As bibliotecas são grupos de funções predefinidas, que podem ser importadas para o código em conjunto e utilizadas para realizar tarefas de forma mais simples, reduzindo assim o tamanho do código próprio e simplificando-o.

    Para importá-las, utiliza-se

    ```python
    import <libreria>
    ```

    onde também se utiliza um "alias": um nome curto (bem curto, como `np` para `numpy`) para se referir a ele pelo resto do programa.

    ```python
    import <libreria> as <alias>
    ```

    Entretanto, em algumas ocasiões, não se deseja importar toda a biblioteca, mas apenas alguns componentes ou "módulos":

    ```python
    from <libreria> import <modulo o metodo>
    ```

    Depois de importá-las, seus atributos e métodos são chamados com a notação de ponto. Por exemplo, a função cosseno da biblioteca NumPy é `np.cos()` (um método) e o número $\pi$ é `np.pi` (um atributo). Se um método for importado diretamente, a notação de ponto não é necessária, por exemplo: `randint()` (uma função de `random`).
    """)
    return


@app.cell
def _():
    import math
    import numpy as np
    from random import randint
    from scipy.constants import c

    print("4! =", math.factorial(4))
    print("C/D =", np.pi)
    print("Um número aleatório =", randint(50, 60))
    print("Velocidade da luz =", c)
    return (math,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1.2.1 - Biblioteca `math`

    Estas são funções matemáticas comuns. Há uma grande [variedade](https://docs.python.org/3/library/math.html), entre as quais se incluem:

    ##### Redondeo

    * `math.ceil(x)`: retorna o "teto" de `x`, o menor inteiro maior ou igual a `x`.
    * `math.floor(x)`: retorna o "piso" de `x`, o maior inteiro menor ou igual a `x`.

    ##### Análisis combinatorio

    * `math.comb(n, k)`: retorna o coeficiente binomial $C(n,k)$, correspondente ao número de combinações de `k` elementos que podem ser obtidas de um grupo de `n` elementos, onde a **ordem não importa**.

    $$
    n \choose k
    $$

    * `math.perm(n, k)`: retorna o número de formas de escolher `k` elementos de `n` elementos sem repetição, onde a **ordem importa**.

    ##### Outras funções úteis

    * `math.factorial(x)`: retorna o fatorial de `x`: $x!$.
    * `math.pow(x, y)`: retorna o valor de $x^y$.
    * `math.sqrt(x)`: retorna a raiz quadrada de `x`: $\sqrt{x}$.
    * `math.erf(x)`: retorna o valor da função erro (a função de distribuição normal padrão) avaliada em `x`. Esta função será de grande utilidade neste curso.
    """)
    return


@app.cell
def _(math):
    print(math.ceil(2.3))
    print(math.floor(2.3))
    print(math.erf(1.1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1.2.2 - Biblioteca `random`

    Geração de números pseudoaleatórios, com diferentes distribuições. Há uma grande [variedade](https://docs.python.org/3/library/random.html), entre as quais se incluem:

    * `random.randint(a, b)`: retorna um número aleatório inteiro entre `a` e `b` (intervalo fechado).
    * `random.uniform(a, b)`: retorna um número aleatório em ponto flutuante para uma distribuição uniforme entre `a` e `b`.
    * `random.sample(population, k)`: retorna uma lista com `k` amostras aleatórias retiradas da lista `population`.
    * `random.expovariate(lambd)`: retorna um número aleatório em ponto flutuante para uma distribuição exponencial com parâmetro `lambd`.
    * `random.gauss(mu, sigma)`: retorna um número aleatório (em ponto flutuante) para uma distribuição normal com média `mu` e desvio padrão `sigma`.
    """)
    return


@app.cell
def _():
    import random as rd

    print(rd.gauss(1, 3))
    print(rd.randint(0, 100))
    print(rd.uniform(0, 100))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1.2.3 - Biblioteca `statistics`

    Ferramentas estatísticas para aplicar a um conjunto de dados. Há uma grande [variedade](https://docs.python.org/3/library/statistics.html), entre as quais se incluem:

    * `statistics.mean(data)`: retorna o valor esperado de um conjunto de dados `data`.
    * `statistics.pstdev(data)`: retorna o desvio padrão populacional do conjunto de dados `data`.
    * `statistics.stdev(data)`: retorna o desvio padrão amostral do conjunto de dados `data`.
    * `statistics.pvariance(data)`: retorna a variância populacional do conjunto de dados `data`.
    * `statistics.variance(data)`: retorna a variância amostral do conjunto de dados `data`.

    Entre outras. Consulte a documentação anexa.
    """)
    return


@app.cell
def _():
    import statistics

    data = range(1, 60)

    print(statistics.mean(data))
    print(statistics.variance(data))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1.2.4 - Biblioteca `collections`

    Apresenta alternativas às listas, sets, tuplas e dicionários incluídos no Python por padrão. Inclui diferentes estruturas para armazenar e manipular dados, definidas por classes, cada uma com seus métodos específicos. Há uma grande [variedade](https://docs.python.org/3/library/collections.html), entre as quais se incluem:

    * `collections.deque`: adiciona funcionalidades a uma lista convencional, como `pop` e `append`.
    * `collections.OrderedDict`: dicionário que registra a ordem em que os objetos foram adicionados.
    * `collections.UserString`: adiciona funcionalidades para o manejo de objetos do tipo `String`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A seguir, há um exemplo para a solução "elegante" de um problema comum.

    > Qual é a probabilidade de que, ao lançar dois dados, a soma dos dados seja 7? [2]

    (O resultado é fácil de deduzir: de 36 combinações possíveis, seis somam sete (1 + 6, 2 + 5, 3 + 4, 4 + 3, 5 + 2, 6 + 1), então 6/36 = 1/6 $\approx$ 0.16667).

    Primeiro, o objeto `defaultdict` do [módulo](https://docs.python.org/2/library/collections.html) `collections` cria dicionários com valores padrão quando encontra uma nova chave. Seu uso prático é o de **"dicionário preenchível"**.
    """)
    return


@app.cell
def _():
    from collections import defaultdict

    return (defaultdict,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Agora, é possível criar um dicionário com todas as combinações possíveis e a soma de cada uma, com um duplo laço `for`:
    """)
    return


@app.cell
def _():
    d = {(i, j): i + j for i in range(1, 7) for j in range(1, 7)}
    print(d)
    return (d,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Em seguida, cria-se um `defaultdict` vazio. Isso implica que, mais adiante, se uma chave não for encontrada no dicionário, em vez de um `KeyError` será criada uma nova entrada (um novo `key:value`).
    """)
    return


@app.cell
def _(defaultdict):
    dinv = defaultdict(list)
    print(dinv)
    return (dinv,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    É possível extrair do dicionário as combinações que somam 7. O método `.items()` gera uma lista de pares de "tuplas" (uma tupla é um conjunto ordenado e imutável de elementos) a partir do dicionário de combinações criado em `d`. "Preenchemos" o `defaultdict` com os elementos do dicionário criado anteriormente e o método `.append()`, isso com um laço `for` em que os índices `i,j` representam os pares de combinações e sua soma. A vantagem é que agora estão todos agrupados.
    """)
    return


@app.cell
def _(d, dinv):
    print("Antes...\n")
    print(d.items())

    for i, j in d.items():
        dinv[j].append(i)

    print("\nDespués...")
    dinv
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    O `for` anterior pode ser lido como: "para cada par na lista de itens, na posição `j` (a soma das combinações) adicione a combinação correspondente (em `i`)".

    Extraímos os pares que somam sete e obtemos a quantidade deles.
    """)
    return


@app.cell
def _(dinv):
    print("Combinaciones que suman 7:", dinv[7])
    print("Elementos:", len(dinv[7]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Por fim, e de forma mais geral, obtém-se a probabilidade para todas as somas na forma de um único dicionário:
    """)
    return


@app.cell
def _(dinv):
    probabilidades = {i: len(j) / 36 for i, j in dinv.items()}
    print("O vetor de probabilidades das somas é =", probabilidades)
    print("A probabilidade de a soma ser 7 é =", probabilidades[7])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1.2.5 - Biblioteca `csv`

    Esta biblioteca implementa classes para o manejo de arquivos do tipo CSV (*Comma Separated Values*), com atividades típicas como *ler* dados de e *escrever* dados em um arquivo CSV ou outros similares.

    Entre suas funções estão:

    * `csv.reader(csvfile, dialect='excel', **fmtparams)`: cria um objeto do tipo `reader` com os dados do arquivo `csvfile` para o "dialeto" (formato) especificado. `fmtparams` são "parâmetros de formato" adicionais para modificar a configuração do formato.
    * `csv.writer(csvfile, dialect='excel', **fmtparams)`: cria um objeto do tipo `writer` para escrever dados no arquivo `csvfile` com o "dialeto" (formato) especificado. `fmtparams` são "parâmetros de formato" adicionais para modificar a configuração do formato.

    A [documentação](https://docs.python.org/3/library/csv.html) completa tem todos os detalhes.
    """)
    return


@app.cell
def _():
    import csv

    unos = [1] * 10

    with open("unos.csv", "w", newline="") as archivo:
        escribir = csv.writer(archivo)
        escribir.writerow(unos)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1.2.6 - Biblioteca `os`

    Permite manipular arquivos e caminhos do sistema operacional como se fossem comandos no terminal. A lista completa de funções é apresentada na [documentação](https://docs.python.org/3/library/os.html). Os métodos mais importantes são:

    * `os.getcwd()`: retorna o diretório de trabalho atual.
    * `os.chdir(path)`: altera o diretório de trabalho para o especificado por `path`.
    * `os.path` é um módulo para manipulação de endereços (caminhos) do sistema.
    """)
    return


@app.cell
def _():
    import os

    print(os.getcwd())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1.2.7 - Outras bibliotecas

    #### 1.2.7.1 - Biblioteca `datetime`

    Apresenta classes para manipulação de datas e tempo. Tem dois módulos: `calendar` e `time`, cada um com suas funções, e permitem gerar informações como a data e hora atuais, o fuso horário, entre outras. A documentação completa está [aqui](https://docs.python.org/3/library/datetime.html) e há excelentes exemplos no [Programiz](https://www.programiz.com/python-programming/datetime).
    """)
    return


@app.cell
def _():
    import datetime

    _ahora = datetime.datetime.now()
    print(_ahora)
    print(_ahora.month)
    return (datetime,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 1.2.7.2 - Módulo `calendar`

    Apresenta uma classe `Calendar` que permite criar objetos que representem calendários e inclui métodos para manipulá-los. A documentação completa está [aqui](https://docs.python.org/3/library/calendar.html).
    """)
    return


@app.cell
def _(bisiesto, datetime):
    import calendar

    _ahora = datetime.datetime.now()
    es_bisiesto = calendar.isleap(_ahora.year)
    calendario = calendar.month(_ahora.year, _ahora.month)
    print("Ano bissexto:", es_bisiesto)
    print(calendario)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 1.3 - Como criar uma biblioteca própria?

    Uma biblioteca consiste simplesmente em uma série de arquivos de código (extensão `.py`) com definições das funções a serem utilizadas. Depois de importar a biblioteca para um código, essas funções podem ser acessadas e utilizadas. Os arquivos da biblioteca podem ser distribuídos de forma hierárquica, tendo assim "subbibliotecas" e permitindo classificar as funções.

    Para criar um pacote são necessários dois elementos:
    * Todos os arquivos `.py` com as funções em uma única pasta, com o nome da biblioteca
    * Um arquivo `__init__.py` (que normalmente é deixado vazio) para que o interpretador identifique a pasta como uma biblioteca

    Há muitos [recursos](https://www.tutorialsteacher.com/python/python-package) on-line que explicam e exemplificam este procedimento.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### Mais informações

    * [Documentação oficial do Python](https://docs.python.org/3/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    **Universidade da Costa Rica** | Faculdade de Engenharia | Escola de Engenharia Elétrica

    &copy; 2021

    ---
    """)
    return


if __name__ == "__main__":
    app.run()
