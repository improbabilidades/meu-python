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

    **UNIVERSIDADE FEDERAL DA PARAÍBA** | CENTRO DE INFORMÁTICA

    ### `PyX` - Série de tutoriais de Python para análise de dados

    # `Py0` - *Introdução ao Python*

    *MATERIAL CRIADO E CEDIDO POR: Prof. Fabián Abarca - da Universidad de Costa Rica.*

    Profa Elizabet Medeiros

    > Python é uma linguagem de programação de uso geral, atualmente a mais popular para análise de dados. Sua sintaxe foi pensada desde o início para ser mais legível.

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Introdução

    Alguns dos principais pontos que trazem **destaque para o Python** são:
    - **É uma linguagem interpretada** --> isso acelera bastante a velocidade de desenvolvimento
    - **É linguagem de alto nível** --> sua sintaxe é simples, fácil de aprender e muito próxima da linguagem falada por nós
    - **Possui uma semântica dinâmica** --> o próprio programa “reconhece” qual tipo de dado está sendo utilizado, fazendo com que ele não precise ser previamente declarado
    - É utilizado para desenvolvimento de **software, análise de dados, inteligência artificial, automação de tarefas, criação de aplicativos web, programação orientada a objetos, mineração de dados** e muito mais

    ##Motivos para aprender a programar em Python##

    - Tem sintaxe simples;
    - É multiplataforma e de código aberto;
    - É versátil;
    - Tem uma comunidade fiel e ativa;
    - É utilizado por grandes empresas;
    - É a linguagem mais popular em ciência de dados;
    - Está em alta no mercado de trabalho.
    - Python é constantemente indicado como primeira linguagem de programação para iniciantes.
    - Permite aplicar orientação a objetos Python e conceitos modernos de programação.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Instalação

    Existem várias formas de execução de Python. Pode ser executado no próprio computador ou em alguma das várias plataformas online que existem, como [Google Colab](https://colab.research.google.com/) ou [molab](https://molab.marimo.io/notebooks). Na máquina local é necessário instalar Python e um gerenciador de pacotes em qualquer plataforma (Linux, Windows, macOS).

    - A instalação recomendada de Python e seus pacotes é com [uv]
    - Para instalar o Python, pode seguir primeiro as [instruções de instalação de **uv**](https://docs.astral.sh/uv/getting-started/installation/) para seu sistema operacional.
    - Depois da instalação do **uv**, basta rodar o comando abaixo para instalar o Python:
    ```bash
    uv python install
    ```
    * Ou usá-lo em modo interativo na CLI:

    ```bash
    $ python
    >>> print('Olá')
    Olá
    ```

    ou a partir de qualquer um dos muitos **IDE** (ambientes de desenvolvimento integrado, *Integrated Development Environments*) disponíveis, como:

    * [Visual Studio Code](https://code.visualstudio.com/) (recomendado)
    * [Spyder](https://docs.spyder-ide.org/current/installation.html)
    * [Cursor](https://cursor.com/)
    * [Antigravity](https://antigravity.google/)
    * [Eclipse](https://www.eclipse.org/ide/)
    * [PyCharm](https://www.jetbrains.com/es-es/pycharm/)
    * [Sublime](https://www.sublimetext.com/)

    ### Mais informações

    As informações mais precisas sobre os aspectos básicos da linguagem Python estão no [manual de referência](https://docs.python.org/3/library/) da _Biblioteca Padrão_ do Python. No entanto, é possível encontrar muitas outras boas referências na internet, desde cursos online, páginas de referência (ver final do documento), perguntas em fóruns e até o muito bom [Wikibook de Python](https://en.wikibooks.org/wiki/Python_Programming).

    #### Antes de começar...

    **Nota 0**: Para executar uma célula de código neste _notebook_ utilizam-se as teclas `shift` + `enter`, ou "Run" no painel superior quando a célula está selecionada.

    **Nota 1**: A função `print()` mostra o resultado da avaliação do(s) seu(s) argumento(s).

    **Nota 2**: Os comentários no código-fonte de Python são feitos com `#` em uma única linha ou com `''' (comentário) '''` em várias linhas.

    **Nota 3**: Em Python o índice começa em 0.

    **Nota 4**: Como linguagem orientada a objetos, Python utiliza a "notação do ponto": `objeto.atributo` ou `objeto.método()`, que são *variáveis* e *funções* associadas a um objeto.

    **Nota 5**: A forma "pitônica" de programar em Python (*the Pythonic way*) são convenções que tornam o código mais legível e simples.

    **Nota 6**: O _guia de estilo_ para a escrita de código em Python é o [PEP 8](https://peps.python.org/pep-0008/), que estabelece as boas práticas (obrigatórias neste curso) para melhorar a legibilidade e dar consistência ao código.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.1 - Variáveis

    Em Python, a atribuição de um dado a uma variável **não** requer a indicação explícita do *tipo de dado*.

    **Nota**: Isso é conhecido como linguagem "dinamicamente tipada", que verifica o tipo de dado em tempo de execução.

    Portanto, basta escrever o seguinte para atribuir números ou caracteres ou qualquer outro objeto de Python a uma variável:
    """)
    return


@app.cell
def _():
    number = 15
    string = "olá!"
    n1, n2, n3 = (1, 2, 3)
    print(number, string, n1 + n2 + n3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.2 - Valores _booleanos_ e comparações

    Os dois valores lógicos (_booleanos_) em Python são `True` (ou `1`) e `False` (ou `0`), sobre os quais se aplicam as operações lógicas `or`, `and` e `not`.
    """)
    return


@app.cell
def _():
    i = True and (not False)
    j = 0 or 0 or (not 0)
    print(i, j)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Comparações entre números

    A avaliação das comparações retorna `True` ou `False`.

    | Operação    | Significado                 |
    |-------------|-----------------------------|
    |     `<`     | é estritamente menor que    |
    |     `<=`    | é menor ou igual a          |
    |     `>`     | é estritamente maior que    |
    |     `>=`    | é maior ou igual a          |
    |     `==`    | é igual a                   |
    |     `!=`    | não é igual a               |
    |     `is`    | identidade                  |
    |   `is not`  | identidade negada           |

    **Nota 1**: `=` é de atribuição, `==` é de comparação.

    **Nota 2**: as operações podem ser encadeadas, por exemplo: `x < y < z`
    """)
    return


@app.cell
def _():
    print(12 < 24)
    print(2023 != 2024)
    print(34 >= 21 > 13 > 8)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.3 - Tipos de dados numéricos e seus operadores

    Em Python existem três tipos distintos de dados numéricos:

    * `int`: número inteiro, positivo ou negativo
    * `float`: número de ponto flutuante (decimal) positivo ou negativo
    * `complex`: números com uma "parte real" e uma "parte imaginária" de ponto flutuante

    **Nota 1**: As funções respectivas `int()`, `float()` e `complex(a, b)` permitem converter de um tipo para outro.

    **Nota 2**: A função `type()` permite verificar o tipo de dado numérico ou de qualquer dado de uma variável em Python.
    """)
    return


@app.cell
def _():
    # Definição
    n_int = 2
    print(n_int, "é", type(n_int))
    n_float = 3.0
    print(n_float, "é", type(n_float))
    n_complex = 5 + 8j
    print(n_complex, "é", type(n_complex))

    # Conversão de tipo de dado
    new_int = int(n_float)
    new_float = float(n_int)
    new_complex = complex(new_int, new_float)
    print(new_int, new_float, new_complex)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Operações básicas sobre dados numéricos

    | Operação          | Resultado                          |
    |-------------------|------------------------------------|
    | `x + y`           | soma de `x` e `y`                  |
    | `x - y`           | subtração de `x` e `y`             |
    | `x * y`           | produto de `x` e `y`               |
    | `x / y`           | quociente de `x` e `y`             |
    | `x // y`          | piso do quociente de `x` e `y`     |
    | `x % y`           | resto de `x / y`                   |
    | `-x`              | `x` negativo                       |
    | `+x`              | `x` sem mudança de sinal           |
    | `abs(x)`          | magnitude de `x`                   |
    | `int(x)`          | `x` convertido para inteiro        |
    | `float(x)`        | `x` convertido para ponto flutuante|
    | `complex(re, im)` | número complexo                    |
    | `c.conjugate()`   | conjugado do número complexo `c`   |
    | `divmod(x, y)`    | o par `(x // y, x % y)`           |
    | `pow(x, y)`       | `x` elevado à potência de `y`      |
    | `x ** y`          | `x` elevado à potência de `y`      |
    """)
    return


@app.cell
def _():
    print(10 / 3)
    print(10 // 3)
    print(10 % 3)
    m, n = divmod(10, 3)
    print(m, n, 3 * m + n)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.4 - Números binários, octais, hexadecimais e suas operações

    Para declarar um número **binário** inicia-se com `0b`, para declarar um número **octal** inicia-se com `0o`, para declarar um número **hexadecimal** inicia-se com `0x`. Para converter entre um tipo e outro e também `int` utilizam-se as funções `bin()`, `oct()`, `hex()` e `int()`.
    """)
    return


@app.cell
def _():
    a = 42
    b = 2020
    c = 25
    print(bin(a))
    print(hex(a))
    print(int(b))
    print(int(c))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Operações binárias (bit a bit) sobre números inteiros

    | Operação    | Resultado                       |
    |-------------|---------------------------------|
    | `x [barra] y`^    | **OR** de `x` e `y`                 |
    | `x ^ y`     | **XOR** de `x` e `y`                |
    | `x & y`     | **AND** de `x` e `y`                |
    | `x << n`    | Deslocamento à esquerda de `x` em `n` bits        |
    | `x >> n`    | Deslocamento à direita de `x` em `n` bits |
    | `~x`        | **NOT** (inversão) de `x`          |

    ^ `[barra]` é |
    """)
    return


@app.cell
def _():
    a = 21 & 10
    b = ~a
    c = 13 | 21
    d = 74 << 2
    print(a, b, c, d)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.5 - Tipos de sequências de dados e seus operadores

    As variáveis do tipo "sequência" permitem armazenar **grupos de dados**. Também são chamadas de "contêineres".

    Em Python existem vários tipos:

    * `list`: sequência **mutável** (*que pode mudar*) tipicamente utilizada para armazenar elementos *homogêneos* (de um mesmo tipo de dados ou sequências).
    * `tuple`: sequência **imutável** (*que **não** pode mudar*) tipicamente utilizada para armazenar elementos *heterogêneos* (de tipos diferentes).
    * `range`: sequência **imutável** de **números** tipicamente utilizada para iterar em um laço.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.5.1 Como criar sequências

    #### 0.5.1.1 Criação de listas

    Todas estas opções criam listas:

    * `[]` (lista vazia)
    * `[a]`, `[a, b, c]`
    * `[x for x in iterable]` (*list comprehension*)
    * `list()` ou `list(iterable)`

    **Nota**: Assim como em algumas linguagens de computação científica (Matlab, R...), as listas podem ser utilizadas para criar "vetores" e "matrizes".
    """)
    return


@app.cell
def _():
    L1 = ["ha"]
    L2 = L1 * 3
    L3 = ["alpha", "beta", "gamma"]
    L4 = [x for x in range(6)]
    L5 = [x for x in range(6) if x % 3 != 0]
    L6 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(L1, L2, L3)
    print(L4)
    print(L5)
    print(L6)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 0.5.1.2 Criação de tuplas

    * `()` (tupla vazia)
    * `a`, ou `(a,)`
    * `a, b, c` ou `(a, b, c)`
    * `tuple()` ou `tuple(iterable)`
    """)
    return


@app.cell
def _():
    T1 = (1,)
    T2 = 1, 2, 3
    T3 = ("In", "a", "galaxy", "far", "far", "away")
    T4 = tuple([x for x in range(3)])

    print(type(T1))
    print(T2, T3, T4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 0.5.1.3 Criação de ranges

    * `range(stop)` (começa em 0 e **não** inclui `stop`)
    * `range(start, stop[, step])` (como em `start:step:stop`)
    """)
    return


@app.cell
def _():
    range(1000)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.5.2 Operações sobre sequências

    | Operação               | Resultado                                                                                          |
    |------------------------|----------------------------------------------------------------------------------------------------|
    | `x in s`               | `True` se um elemento de `s` é igual a `x`, caso contrário `False`                                 |
    | `x not in s`           | `False` se um elemento de `s` é igual a `x`, caso contrário `True`                                 |
    | `s + t`                | a concatenação de `s` e `t`                                                                       |
    | `s * n` ou `n * s`     | equivalente a adicionar `s` a si mesmo `n` vezes                                                   |
    | `s[i]`                 | `i`-ésimo elemento de `s`, com origem em 0                                                         |
    | `s[i:j]`               | fatia de `s` de `i` a `j`                                                                          |
    | `s[i:j:k]`             | fatia de `s` de `i` a `j` com passo `k`                                                            |
    | `len(s)`               | comprimento de `s`                                                                                 |
    | `min(s)`               | menor elemento de `s`                                                                              |
    | `max(s)`               | maior elemento de `s`                                                                              |
    | `s.index(x[, i[, j]])` | índice da primeira ocorrência de `x` em `s` (no ou após o índice `i` e antes do índice `j`)        |
    | `s.count(x)`           | número total de ocorrências de `x` em `s`                                                          |

    **Nota**: A forma "pitônica" de acessar o último elemento da sequência é com o índice `-1`, ou seja, `s[-1]`. Dessa forma não é necessário conhecer *a priori* a quantidade de elementos em `s`.
    """)
    return


@app.cell
def _():
    start = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    continuation = 55, 89, 144, 233
    sequence = start + continuation

    print(sequence)
    print(sequence[4])
    print(sequence[0:-1:2])
    print(sequence.count(1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.5.3 Operações sobre sequências *mutáveis*

    | Operação              | Resultado                                                                                  |
    |-----------------------|--------------------------------------------------------------------------------------------|
    | `s[i] = x`            | o elemento `i` de `s` é substituído por `x`                                                |
    | `s[i:j] = t`          | uma porção de `s` de `i` a `j` é substituída pelo conteúdo do iterável `t`                  |
    | `del s[i:j]`          | igual a `s[i:j] = []`                                                                      |
    | `s[i:j:k] = t`        | os elementos de `s[i:j:k]` são substituídos pelos de `t`                                   |
    | `del s[i:j:k]`        | elimina os elementos `s[i:j:k]` da lista                                                   |
    | `s.append(x)`         | adiciona `x` ao final da sequência (igual a `s[len(s):len(s)] = [x]`)                      |
    | `s.clear()`           | elimina todos os elementos de `s` (igual a `del s[:]`)                                     |
    | `s.copy()`            | cria uma cópia superficial de `s` (igual a `s[:]`)                                         |
    | `s.extend(t) ou s += t`| estende `s` com o conteúdo de `t` (na maior parte igual a) `s[len(s):len(s)] = t`         |
    | `s *= n`              | atualiza `s` com seu conteúdo repetido `n` vezes                                           |
    | `s.insert(i, x)`      | insere `x` em `s` no índice dado por `i` (igual a) `s[i:i] = [x]`                          |
    | `s.pop([i])`          | recupera o elemento em `i` e também o remove de `s`                                        |
    | `s.remove(x)`         | remove o primeiro elemento de `s` onde `s[i]` é igual a `x`                                |
    | `s.reverse()`         | inverte os elementos de `s` no lugar                                                       |
    """)
    return


@app.cell
def _():
    phrase = ["all", "you", "need", "is", "love"]
    print(phrase)

    need = "food"
    phrase[-1] = need
    print(phrase)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.6 - Sequências de texto (*strings*) e seus operadores

    As "cadeias" de texto ou *strings* `str` são sequências imutáveis de caracteres alfanuméricos.

    ### 0.6.1 Criação de sequências de texto

    * `'olá'` (pode conter aspas duplas dentro)
    * `"olá"` (pode conter aspas simples dentro)
    * `'''olá'''` ou `\"\"\"olá\"\"\"` (múltiplas linhas)
    * Com a função `str()` a partir de outro tipo de dado

    **Nota**: As sequências de texto permitem todas as operações aplicadas sobre sequências, mas são imutáveis, portanto não admitem as operações sobre sequências mutáveis (como as substituições ou a remoção de elementos).
    """)
    return


@app.cell
def _():
    print('Olá "pessoal"' + ", " + """tudo bem?""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.6.2 Algumas funções ("métodos") sobre cadeias de caracteres

    É possível realizar operações específicas de texto sobre um `str`. A lista completa de métodos está disponível [aqui](https://docs.python.org/3/library/stdtypes.html#string-methods).

    * `str.capitalize()`: Retorna uma cópia da cadeia com seu primeiro caractere em maiúscula e o restante em minúscula.
    * `str.endswith( sufixo [ , início [ , fim ] ] )`: Retorna `True` se a cadeia termina com o sufixo especificado, caso contrário retorna `False`.
    * `str.lower()`: Retorna uma cópia da cadeia com todos os caracteres em maiúscula convertidos para minúsculas.
    """)
    return


@app.cell
def _():
    text = "hElLo, gOoD mOrnInG"

    print(text)
    print(text.capitalize())
    print(text.lower().endswith("ing"))
    print(text.upper())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.6.3 Formatação de texto ao imprimir

    Um [método](https://docs.python.org/3/library/string.html#formatstrings) importante aplicado em cadeias de caracteres permite inserir valores em um texto, com certas especificações.

    * `str.format(*args, **kwargs)`: Realiza uma operação de formatação da cadeia. A cadeia para a qual este método é chamado pode conter texto literal ou **campos de substituição** delimitados por chaves `{}`. Cada campo de substituição contém o índice numérico de um argumento posicional ou o nome de um argumento de palavra-chave. `str.format` retorna uma cópia da cadeia onde cada campo de substituição é substituído pelo valor de cadeia do argumento correspondente.

    **Nota 1**: `*args` é um número variável de argumentos que são passados a uma função. Por exemplo, uma função `multiplicar(*args)` que multiplica todos os argumentos passados pode ser `multiplicar(3,3,2,7)` ou `multiplicar(2,3)`. Os `*args` são _posicionais_, ou seja, devem estar na ordem exata em que a função os requer. Por exemplo:

    ```python
    c = dividir(a, b)
    # c = a/b
    ```

    **Nota 2**: ``**kwargs`` é um número variável de argumentos do tipo `chave=argumento`. Os `**kwargs` não são posicionais, podem ser inseridos em qualquer posição.

    ```python
    c = dividir(den=b, num=a)
    # c = a/b
    ```

    #### Recomendação: *f-strings*

    Uma sintaxe alternativa para incorporar variáveis em um texto é por meio da notação de *f-strings*, que é do tipo:

    ```python
    a = 1600
    texto = f'Nos anos {a}...'
    ```
    """)
    return


@app.cell
def _():
    word = "world"
    x, y = (5, 3)
    z = x / y
    w = 1600
    print("Hello {}!".format(word))
    print("{} entre {} é cerca de {:0.2f}".format(x, y, z))
    print(f"Nos anos {w}...")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.7 - Dicionários

    Um dicionário é um tipo especial de sequência mutável que faz um *mapeamento* de valores a uma chave, do tipo `chave: valor` (usualmente em inglês como `key: value`). O nome é uma analogia com os dicionários que têm pares **palavra: definição**.

    ### 0.7.1 Criação de dicionários

    * Os dicionários podem ser criados colocando uma lista de pares separados por vírgulas entre chaves `{}`.
    * Com o construtor `dict()`.

    **Nota**: A ordem dos pares não importa. Se dois ou mais dicionários compartilham exatamente os mesmos pares (mesmo que tenham sido criados em ordem diferente) então são iguais.
    """)
    return


@app.cell
def _():
    # Com as chaves
    a = {"um": 1, "dois": 2, "tres": 3}
    b = dict(um=1, dois=2, tres=3)

    # Com a função dict()
    c = dict(zip(["um", "dois", "tres"], [1, 2, 3]))
    d = dict([("dois", 2), ("um", 1), ("tres", 3)])

    # Com a função zip() que "emparelha" duas listas
    e = dict({"tres": 3, "um": 1, "dois": 2})
    print(a == b == c == d == e)

    # Com uma lista de tuplas (ordem diferente)
    # Criação redundante, com dict({})
    # Verificar igualdade
    # Mostrar algum dos dicionários
    print(c)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.7.2 Algumas funções úteis em dicionários

    * `list(d)`: Retorna uma lista de todas as chaves utilizadas no dicionário `d`.

    * `len(d)`: Retorna o número de elementos no dicionário `d`.

    * `d[key]`: Retorna o item de `d` com a chave `key`. Gera um `KeyError` se não está no mapa (dicionário).
    """)
    return


@app.cell
def _():
    d = {
        "IE0247": "Sinais e Sistemas I",
        "IE0347": "Sinais e Sistemas II",
        "IE0405": "Modelos Probabilísticos de Sinais e Sistemas",
    }
    print(list(d))
    print(len(d))
    print(d["IE0405"])
    print("MA1001" in d)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.8 - Controles de fluxo

    Os controles de fluxo determinam as ações do programa diante da avaliação de "declarações" como comparações. A documentação [oficial](https://docs.python.org/3/tutorial/controlflow.html) explica seus detalhes.

    ### 0.8.1 Controles de fluxo `if` - `elif` - `else`

    Possivelmente o mais importante ou conhecido, `if` avalia uma declaração e prossegue com linhas de execução distintas conforme o resultado. Em Python sua sintaxe é:

    ```python
    if <declaracao>:
         <acao quando eh verdadeiro>
    ```

    Quando o resultado é `False` pode haver outra ação possível, e a sintaxe é:

    ```python
    if <declaracao>:
        <acao quando eh verdadeiro>
    else:
        <acao quando eh falso>
    ```

    Se ao avaliar a primeira declaração há outras possibilidades então devem ser avaliadas outras declarações com a sintaxe:

    ```python
    if <declaracao_1>:
        <acao quando 1 eh verdadeiro>
    elif <declaracao_2>:
        <acao quando 1 eh falso e 2 eh verdadeiro>
    else:
        <acao quando 1 e 2 sao falsos>
    ```

    **Nota**: a *indentação* é **obrigatória** em Python, e é também suficiente para delimitar o que está contido dentro de um curso de ação. Por exemplo, no seguinte fragmento, `print(a)` está dentro do `if` e `print(b)` não.

    ```python
    if a < b:
        print(a)

    print(b)
    ```

    **Nota**: este exemplo inclui uma **biblioteca** de Python (`datetime`) para obter a hora atual. O uso e importação de bibliotecas é apresentado em `Py1`.
    """)
    return


@app.cell
def _():
    import datetime

    # Hora atual
    H = datetime.datetime.now().hour

    # Saudação conforme a hora do dia
    if H < 12:
        print("Bom dia")
    elif H < 18:
        print("Boa tarde")
    else:
        print("Boa noite")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.8.2 Controles de fluxo `try` - `except` para tratamento de erros

    Python encerra a execução de um programa quando encontra um erro. Isso diferente de uma linguagem compilada (como C e C++) que não executa o programa até descartar erros em uma compilação prévia.

    Frequentemente é necessário evitar que o programa **não** pare quando há um erro. Quando uma instrução pode conter um erro com certa probabilidade, é possível fazer um teste com a instrução `try`.

    O comando `except` permite agir em caso de erro.

    Outras opções com `else` e `finally` podem ser encontradas [aqui](https://www.w3schools.com/python/python_tryexcept.asp).
    """)
    return


@app.cell
def _():
    x1 = 3

    # Se a definição de x1 está "comentada"
    try:
        print(f"A variável existe e é {x1}.")
    except:
        print("Opa! A variável não existe")

    # Agora pode-se testar "descomentando" x1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 0.8.3 Controle de fluxo `match - case`

    Uma alternativa para usar uma lógica `if` no caso em que há várias opções possíveis, é a comparação de uma variável de interesse com seus valores possíveis e executar ações para cada caso, como:

    ```python
    match variable:
        case "a":
            print("It's a!")
        case "b":
            print("It's b!")
        case "c":
            print("It's c!")
        case _:
            print("It was something else")
    ```
    """)
    return


@app.cell
def _():
    variable = "a"

    match variable:
        case "a":
            print("It's 'a'!")
        case "b":
            print("It's 'b''!")
        case "c":
            print("It's 'c'!")
        case _:
            print("It was something else")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.9 - Laços

    Um tipo especial de controles de fluxo são os que **repetem** uma ação em "laço" ou "loop" (*loop*).

    ### 0.9.1 Laço `while`

    Repete uma operação **indefinidamente** enquanto uma condição se cumpra.

    ```python
    while <declaracao>:
        <acao enquanto for verdadeiro>
    ```

    ### 0.9.2 Laço `for`

    Repete uma operação por **um número determinado de vezes**, ao iterar *sobre* uma sequência de dados.

    ```python
    for i in (a, b, c, d, e, f):
        <acao para i = a, depois i = b, depois i = c...>
    ```

    **Nota 1**: a sequência `range()` é útil quando se quer iterar sobre uma longa sequência de números (por exemplo, de 10 até 100).

    **Nota 2**: O operador `a += n` é equivalente a `a = a + n`. Também existem `-=` e `*=`.
    """)
    return


@app.cell
def _():
    print("Primeiro:")
    i = 1
    while i % 5 != 0:
        print(i)
        i += 1

    print("Segundo:")
    for j in (8, 13, 21, 34):
        print(j)

    print("Terceiro:")
    for k in range(5):
        print(k)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Outros comandos especiais

    * `break`: Sai do ciclo atual.
    * `yield`: Continua com a próxima iteração do laço.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 0.10 - Algumas funções nativas

    Já são conhecidas algumas funções da [Biblioteca Padrão do Python](https://docs.python.org/3/library/functions.html) como `print()`, `type()`, `int()`, `len()`, `list()`. Algumas outras funções úteis de interesse são:

    * `abs(a)`: Valor absoluto de um número.
    * `all()`: `True` se todos os elementos de uma sequência são `True`.
    * `enumerate(iterable[, start=n])`: "adere" numeração a uma sequência iterável, começando em `start=n` (por padrão `start=0`).
    * `help()`: Invoca a ajuda de um objeto (função ou comando ou variável).
    * `input([prompt])`: Habilita a entrada de dados com um texto `[prompt]` quando o programa é executado em um terminal de comandos ou aqui no Jupyter também.
    * `map(função, iterable)`: Aplica a `função` sobre cada elemento de `iterable`.
    * `round(n[, dígitos])`: Arredonda `n` com uma precisão de `dígitos`.
    * `zip(*iterables)`: Cria um novo iterador com a união de tantos `*iteradores` quanto forem adicionados. O `i`-ésimo elemento de `zip(*iterables)` é uma tupla com os `i`-ésimos elementos de cada argumento iterável.

    **Nota**: O Jupyter às vezes não exibe a entrada de dados. Para isso pode-se tentar no menu Kernel > Restart (as variáveis armazenadas serão apagadas).
    """)
    return


@app.cell
def _():
    name = input("Digite seu nome: ")

    print("Hi {}.".format(name))
    print('This is the help for function "abs":\n')
    help(abs)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ### Isso é tudo por agora!

    Os conceitos vistos até agora em Py0 são poderosos e permitem a programação de soluções para uma grande quantidade de problemas computacionais. Mesmo em tarefas muito mais complexas no futuro, essas bases continuarão sendo essenciais.

    No entanto, o verdadeiro segredo do Python são os muitos pacotes que lhe dão "poderes especiais" para quase todo tipo de tarefas, desenvolvidos por uma comunidade ativa ao redor do mundo.

    O restante dos PyX será um guia introdutório para algumas dessas ferramentas em [computação científica](https://pt.wikipedia.org/wiki/Computa%C3%A7%C3%A3o_cient%C3%ADfica).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Filosofia do Python

    *Tim Peters*

    Este "zen" é uma coleção de princípios de programação (ou de vida?) que guiam as boas práticas em Python.

    - Bonito é melhor que feio.
    - Explícito é melhor que implícito.
    - Simples é melhor que complexo.
    - Complexo é melhor que complicado.
    - Plano é melhor que aninhado.
    - Esparso é melhor que denso.
    - A legibilidade conta.
    - Os casos especiais não são especiais o bastante para quebrar as regras.
    - O prático vence o puro.
    - Os erros nunca devem passar silenciosamente.
    - A menos que sejam explicitamente silenciados.
    - Diante da ambiguidade, recuse a tentação de adivinhar.
    - Deveria haver uma — e preferencialmente apenas uma — maneira óbvia de fazer.
    - Embora essa maneira possa não ser óbvia à primeira vista, a menos que você seja holandês.
    - Agora é melhor que nunca.
    - Embora nunca frequentemente seja melhor que *agora mesmo*.
    - Se a implementação é difícil de explicar, é uma má ideia.
    - Se a implementação é fácil de explicar, pode ser uma boa ideia.
    - Os espaços de nomes (*namespaces*) são uma grande ideia, vamos fazer mais!

    **Nota**: Um *namespace* é uma forma de garantir que não há nomes de variáveis ou funções ou métodos repetidos entre o *script* e as bibliotecas e módulos utilizados.
    """)
    return


@app.cell
def _():
    # Estes princípios estão escondidos aqui:
    import this

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ### Mais informações

    * [Documentação oficial do Python](https://docs.python.org/3/)
    * [RealPython](https://realpython.com/)
    * [w3schools](https://www.w3schools.com/python/)
    * [Wikibook de Python](https://en.wikibooks.org/wiki/Python_Programming)
    * (...muitas outras referências na web e livros...)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    **Universidade Federal da Paraíba** | Centro de Informática | Departamento de Computação Científica

    **Universidade da Costa Rica** | Faculdade de Engenharia | Escola de Engenharia Elétrica

    &copy; 2020 - 2026

    ---
    """)
    return


if __name__ == "__main__":
    app.run()
