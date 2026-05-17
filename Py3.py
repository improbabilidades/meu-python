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

    # `Py2` - *Bibliotecas de Computação Científica*

    > Com bibliotecas externas é possível acessar poderosas ferramentas computacionais que tornam o Python comparável a outros programas de cálculo numérico, como Matlab, R, Mathematica e outros.

    *Fabian Abarca Calderón*

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Bibliotecas especializadas

    Ele também fornece bibliotecas vistas no PyX anterior e que pertencem à [The Python Standard Library](https://docs.python.org/3/library/),Existem outras bibliotecas específicas de aplicativos criadas por pessoas e organizações externas. Entre eles, alguns úteis para o estudo de probabilidades, estatística e análise de dados. Especificamente, estudaremos NumPy, SciPy e Matplotlib aqui.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 2.1 -NumPy

    De acordo com seu [site oficial](https://numpy.org/),> NumPy é o pacote fundamental para computação científica com Python.

    <img src="https://numpy.org/images/logo.svg"largura="150">

    * O NumPy foi projetado para ser rápido e é por isso que faz parte de aplicações críticas na análise de dados. Parte da razão para isso é que a biblioteca é escrita em Python e também em **C**.
    * Fornece muitas ferramentas para funções matemáticas comuns.
    * É a base para muitas outras bibliotecas Python, incluindo SciPy.
    * É orientado ao gerenciamento de matrizes, assim como o Matlab.

    ### 2.1.1. - Importar NumPy

    Por convenção, NumPy é importado sob o alias `np`.

    ```python
    import numpy as np
    ```

    NumPy vem com a instalação normal do [Anaconda] (https://www.anaconda.com/products/individual).Caso contrário, você pode instalá-lo com o [guia](https://numpy.org/install/)instalação.

    **Nota**: Em Python, *aliases* são um nome alternativo para se referir à mesma biblioteca, portanto as seguintes expressões seriam equivalentes, mas claramente mais abreviadas:```python

    # Sin el alias

    ```py
    matplotlib.pyplot.plot()
    ```

    # Com el alias

    ```py
    plt.plot()
    ```

    ### 2.1.2. - O contêiner `array`

    NumPy não usa listas, tuplas ou dicionários Python genéricos. Em vez disso, a estrutura de dados usual do NumPy é o `array`, que permite armazenar *valores numéricos* (exclusivamente) e realizar operações eficientes sobre eles na forma de arrays, como faria o Matlab. Sua criação eh sintaxe:

    ```python
    np.array([lista de numeros, separados, por, coma])
    ```

    O `array` é um contêiner **mutável** e, portanto, possui os mesmos métodos: inserção de elementos, exclusão, apêndice, concatenação, etc.
    """)
    return


@app.cell
def _():
    import numpy as np

    _arr = np.array([1, 2, 3, 4, 5, 6])
    # Creacción del array
    soma = np.sum(_arr)
    base2 = np.exp2(_arr)
    # Operación sobre todos los elementos
    print("Arreglo:          ", _arr)
    print("Tipo de dato:     ", type(_arr))
    # Operación sobre cada elemento
    print("Primer elemento:  ", _arr[0])
    print("Último elemento:  ", _arr[-1])
    print("Suma de elementos:", soma)
    print("2^(cada elemento):", base2)
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.1.3. - Generalização de objetos bidimensionais *n*

    #### Crie um objeto NumPy `ndarray`

    NumPy cria `array`s multidimensionais que representam arrays e são chamados de `ndarray`.

    É possível criar um objeto NumPy `ndarray` usando a função `array()`.
    """)
    return


@app.cell
def _(np):
    nd1 = np.array([1, 2, 3, 4, 5, 6])
    nd2 = np.array([[1, 2, 3], [4, 5, 6]])
    # Matriz unidimensional (vector)
    nd3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print("Matriz unidimensional\n", nd1, "\n")
    # Matriz bidimensional
    print("Matriz bidimensional\n", nd2, "\n")
    # Matriz tridimensional
    print("Matriz tridimensional\n", nd3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Como poderíamos interpretar ou visualizar este último arranjo tridimensional? Tente imaginar que `1, 2, ..., 8` são os vértices de um cubo.

    NumPy `array` fornece o atributo `ndim`, que retorna um número inteiro com o número de dimensões do array.
    """)
    return


@app.cell
def _(np):
    _a = np.array(42)
    _b = np.array([1, 2, 3, 4, 5])
    _c = np.array([[7, 7, 7], [6, 6, 6]])
    _d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print("nd(a) =", _a.ndim)
    print("nd(b) =", _b.ndim)
    print("nd(c) =", _c.ndim)
    print("nd(d) =", _d.ndim)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.1.4. - Acesso aos elementos de uma matriz

    É possível acessar um elemento do array referindo-se ao seu número **índice**. Para dimensões *n*, os índices de uma matriz são referenciados como:```python
    arr[i_1, i_2, ..., i_n]
    ```**Nota**: Os índices em arrays NumPy (como em Python) começam com 0.

    No exemplo a seguir queremos acessar o terceiro elemento da segunda matriz da primeira matriz da primeira dimensão. Isto é conseguido, para um array tridimensional `arr`, com:```python
    arr[0, 1, 2]
    ```Para o exemplo abaixo:

    * O primeiro número representa a primeira dimensão, que contém duas matrizes. Digitar 0 escolhe a primeira matriz.
    * O segundo número representa a segunda dimensão, que também contém duas matrizes. Escolher 1 escolhe a segunda matriz.
    * O terceiro número representa a terceira dimensão, que contém três valores. Com 2 o terceiro valor é escolhido.
    """)
    return


@app.cell
def _(np):
    _arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    print("Matriz tridimensional: \n", _arr)
    print("Primer elemento da primera dimensión: \n", _arr[0])
    print("Segundo elemento del primer elemento da primera dimensión: \n", _arr[0, 1])
    print(
        "Tercer elemento del segundo elemento del primer elemento da primera dimensión: \n",
        _arr[0, 1, 2],
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.1.5. - Operações em um `array` NumPy

    Da [multidão](https://numpy.org/doc/stable/reference/)das funções (rotinas) que o NumPy executa, estas podem operar:

    * Em cada elemento (*por elemento*), retornando um `array` do mesmo tamanho daquela dimensão.
    * Sobre todos os elementos de uma dimensão, retornando um único ou um conjunto de valores do mesmo tamanho dessa dimensão.
    * Entre dois ou mais `array`, que podem retornar um único valor ou um vetor, dependendo da operação.

    #### Operações em cada elemento de um `array`

    Algumas operações são:

    * Funções trigonométricas, exponenciais e logarítmicas
    * Funções "Diversas", como arredondamento, parte inteira, conversão de graus para radianos, etc.

    No exemplo a seguir, `sqrt`, `log10`, `ceil` e `round` são todos deste tipo.
    """)
    return


@app.cell
def _(np):
    _arr = np.array([1, 2, 3, 5, 8, 13])
    _a = np.sqrt(_arr)
    _b = np.log10(_arr)
    print("Raíces:", np.ceil(_a))
    print("Logaritmos:", np.round(_b, 2))
    print("Mismo tamaño:", len(_arr) == len(_a) == len(_b))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Operações em todos os elementos de um `array`

    O exemplo mais comum é o dia em que existem dois elementos. Em uma matriz unidimensional, a operação `sum` soma todos os elementos. Também em um array *n*-dimensional, mas você tem a opção de escolher um "eixo" (`axis`) para plotar.

    Por exemplo, nesta matriz, uma soma no eixo 0 (a primeira dimensão, as linhas) é a soma de dois elementos nas colunas, e uma soma ao longo do eixo 1 (a segunda dimensão, as colunas) é a soma de dois elementos nas linhas.

    | – | C0 | C1 | C2 | – |
    |----|--------|--------|--------|--------|
    | **F0** | *3* | *8* | *6* | **17** |
    | **F1** | *2* | *4* | *5* | **11** |
    | **F2** | *7* | *1* | *0* | **8** |
    | – | **12** | **13** | **11** | – |
    """)
    return


@app.cell
def _(np):
    _arr1 = np.array([-5, -3, 0, 1, 6, 9])
    _arr2 = np.array([[3, 8, 6], [2, 4, 5], [7, 1, 0]])
    _a = np.sum(_arr1)
    _b = np.sum(_arr2)
    _c = np.sum(_arr2, 0)
    _d = np.sum(_arr2, 1)
    print("Suma de todos los elementos:", _a)
    print("Suma de todos los elementos:", _b)
    print("Suma dos elementos en cada columna:", _c)
    print("Suma dos elementos en cada fila:", _d)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Operações entre dois ou mais `array`

    Na álgebra linear, por exemplo, existem operandos vetoriais e matriciais entre duas ou mais matrizes, todos presentes no NumPy. Mas também existem outras óperas “diversas”.
    """)
    return


@app.cell
def _(np):
    _a = np.array([1, 2, 3])
    _b = np.array([4, 5, 6])
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = np.add(A, B)
    D = np.multiply(A, B)
    E = np.vdot(_a, _b)
    print("Suma por elemento: \n", C)
    print("Multiplicación por elemento: \n", D)
    print("Producto punto: \n", E)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.1.6. - Polinômios

    Existem duas maneiras de lidar com polinômios 1-D no SciPy. A primeira é usar a classe `poly1d` do NumPy. Esta classe aceita coeficientes ou raízes polinomiais para inicializar um polinômio. O objeto polinomial pode ser manipulado em expressões algébricas, integrado, diferenciado e avaliado. Ele até imprime como um polinômio.
    """)
    return


@app.cell
def _():
    from numpy import poly1d

    p = poly1d([3, 4, 5])

    print("Polinomio: \n", p)
    print("Polinomio derivado: \n", p.deriv())
    print("Polinomio integrado: \n", p.integ())
    print("Polinomio al cuadrado: \n", p * p)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###2.1.7. - Tipos de dados em NumPy

    Abaixo está uma lista de todos os tipos de dados no NumPy e os caracteres usados para representá-los.

    | Símbolo | Tipo |
    | ------- | ---- |
    | `eu` | inteiro |
    | `b` | booleano |
    | `você` | inteiro sem sinal |
    | `f` | flutuante |
    | `c` | flutuante complexo |
    | `m` | delta do tempo |
    | `M` | data e hora |
    | `O` | objeto |
    | `S` | corda |
    | `U` | cadeia unicode |
    | `V` | fragmento de memória |

    **Nota**: O objeto array NumPy possui uma propriedade chamada `dtype` que retorna o tipo fornecido do array.
    """)
    return


@app.cell
def _(np):
    _arr1 = np.array([[1, 2, 3, 4], [9, 8, 7, 6]])
    _arr2 = np.array(["manzana", "banano", "fresa"])
    _arr3 = np.array([1.0, 2.0])
    print(_arr1.dtype)
    print(_arr2.dtype)
    print(_arr3.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Convertendo tipo de dado em arrays existentes

    A melhor maneira de alterar o tipo de dado de um array existente é fazer uma cópia do array com o método `astype()`, que permite especificar o tipo de dado como parâmetro.
    """)
    return


@app.cell
def _(np):
    _arr1 = np.array([1.4, 2.5, 3.6])
    _arr2 = _arr1.astype(str)
    _arr3 = _arr1.astype(int)
    print(_arr1, _arr1.dtype)
    print(_arr2, _arr2.dtype)
    print(_arr3, _arr3.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## 2.2 - SciPy

    De acordo com seu [site oficial](https://www.scipy.org/),> SciPy é um ecossistema de software de código aberto em Python para matemática, ciências e engenharia. SciPy é baseado em NumPy e para todas as necessidades básicas de gerenciamento de array você pode usar as funções do NumPy.

    <img src="https://scipy.org/images/logo.svg"largura="150px">

    SciPy oferece módulos especializados em vários tópicos de ciência e engenharia, incluindo:

    * Funções básicas - (usando NumPy)
    * Funções especiais - `scipy.special`
    * Integração - `scipy.integrate`
    * Otimização - `scipy.optimize`
    * Interpolação - `scipy.interpolate`
    * Transformadas de Fourier - `scipy.fft`
    * processamento de sinais - `scipy.signal`
    * Álgebra linear - `scipy.linalg`
    * Estruturas e algoritmos de dados espaciais - `scipy.spatial`
    * **Estatísticas** - `scipy.stats`
    * Processamento de imagem multidimensional - `scipy.ndimage`
    * Escrevendo e lendo arquivos - `scipy.io`

    O pacote `scipy.stats` será muito importante para o curso e será abordado em outro PyX.

    **Nota**: As estruturas de dados (ou contêineres) são iguais ao NumPy, como `array`, e aplicam todas as manipulações vistas acima.

    ### 2.2.1 - Importar SciPy

    Para importar um módulo inteiro```python
    from scipy import algun_modulo

    # Código aquí...

    algun_modulo.alguna_funcion()
    ```ou apenas um módulo funciona```python
    from scipy.algun_modulo import una_funcion, otra_funcion

    # Código aquí...

    una_funcion()
    otra_funcion()
    ```### 2.2.2. - Integração

    Para realizar o cálculo numérico de uma integral (definida ou indefinida) é possível usar as duas (de várias) funções SciPy a seguir:

    * `quad`: integração de propósito geral, conhecida a função e limites de integração.
    * `trapz`: integração de uma exibição de dados com a regra trapezoidal.

    A seguir, o cálculo fornece integral

    $$
    R = \int_{a}^{b} (rx^3 + s) ~ \mathrm{d}x
    $$

    usando```python
    (resultado, error) = quad(funcion, lim_inf, lim_sup, args=())
    ```
    """)
    return


@app.cell
def _():
    from scipy.integrate import quad

    def paraintegrar(x, r, s):
        return r * _x**3 + s

    _a = 0
    _b = 2
    r = 1
    s = 0
    _R = quad(paraintegrar, _a, _b, args=(r, s))
    print(_R)
    print("Resultado:", _R[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Quando, no entanto, temos uma amostra de pares ordenados dados $(x, y)$ então usamos `trapz` para fazer uma integração trapezoidal.

    A precisão da aproximação depende do número de amostras no intervalo de interesse:

    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Trapezium2.gif"largura="400">

    No exemplo a seguir observe que:

    * Os dados não são necessariamente `array` (na documentação eles são conhecidos como *array-like*, e incluem listas ou tuplas).
    * Os pontos no eixo $x$ não são necessariamente espaçados uniformemente.
    * Os pares ordenados são extraídos da mesma função $rx^3 + s$ usada acima, para que se saiba que com os limites de integração a = 0, b = 2 e parâmetros r = 1, s = 0, o resultado dá integração eh 4.
    """)
    return


@app.cell
def _():
    from scipy.integrate import trapz

    _x = (0.0, 0.5, 0.9, 1.2, 1.7, 2.0)
    _y = (0.0, 0.125, 0.729, 1.728, 4.913, 8.0)
    _R = trapz(_y, _x)
    print("Resultado:", _R)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 2.3 - Matplotlib

    De acordo com seu [site oficial](https://matplotlib.org/),> Matplotlib é uma biblioteca completa para criação de visualizações estáticas, animadas e interativas em Python.

    <img src="https://matplotlib.org/_static/images/documentation.png"largura="150">

    Nesta primeira abordagem do Matplotlib, estudaremos gráficos bidimensionais estáticos.

    ### 2.3.1. -Pyplot

    Pyplot é uma interface "que faz o Matplotlib funcionar como o Matlab", e nesta primeira abordagem ao Matplotlib será o módulo a utilizar.

    De acordo com [tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html)oficial:

    > Cada função `pyplot` faz alguma alteração em uma figura: por exemplo, cria uma figura, cria uma área de plotagem (tela) em uma figura, desenha algumas linhas em uma área de plotagem, decora a plotagem com rótulos, etc.

    Para importar Pyplot usamos:```python
    import numpy as np
    import matplotlib.pyplot as plt
    ```### 2.3.2. - Primeiro gráfico

    **Nota**: É possível adicionar código $\mathrm{\LaTeX}$ com tags como `'$...$'`.
    """)
    return


@app.cell
def _(np):
    import matplotlib.pyplot as plt

    _x = np.linspace(0, 4 * np.pi, 60)
    _y = np.cos(_x)
    plt.plot(_x, _y)
    plt.ylabel("$\\cos(\\omega)$")
    plt.xlabel("$\\omega$")
    plt.show()
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    No exemplo acima, `np.linspace(start, stop, num)` é uma função que cria uma sequência uniformemente espaçada de elementos `num` entre `start` e `stop`, mas não incluindo o último, ou seja, $[start, stop)$. É necessário criar um domínio, ou conjunto de números no qual a função (no caso anterior, cosseno) será avaliada. A quantidade `num` é escolhida com base em vários critérios, mas geralmente "suficiente" para parecer "boa" (outras razões têm a ver com a taxa de amostragem de Nyquist).

    Veja em continuidade três escolhas diferentes de `num`, ou seja, diferentes amostragens de funcao.

    **Nota**: Apenas as funções `pi`, `cos` e `linspace` do NumPy são importadas aqui e, portanto, a notação `np.pi` pode ser alterada para `pi`.
    """)
    return


@app.cell
def _(plt):
    from numpy import pi, cos, linspace

    x1 = linspace(0, 2 * pi, 25)
    x2 = linspace(0, 2 * pi, 15)
    x3 = linspace(0, 2 * pi, 5)
    y1 = cos(x1)
    y2 = cos(x2 + pi / 6)
    y3 = cos(x3 + pi / 3)
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    plt.title("Gráficas com distinto número de puntos de amostra")
    plt.ylabel("$\\cos(\\omega)$")
    plt.xlabel("$\\omega$")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.3.3. - Vários gráficos de funções

    Combinando as ferramentas NumPy, SciPy e Pyplot, é possível representar graficamente inúmeras formas, incluindo suas próprias funções criadas em Python.

    Há uma lista muito extensa de funções matemáticas no NumPy [aqui](https://numpy.org/doc/stable/reference/routines.math.html).
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 2, 100)

    def hola(x):
        _y = np.log(_x + 1)
        return _y

    plt.plot(_x, np.sqrt(_x))
    plt.plot(_x, np.power(_x, 1.2))
    plt.plot(_x, hola(_x))
    plt.title("Algunas funcoes")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(left=0, right=2)
    plt.ylim(bottom=0)
    plt.grid()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.3.4. - Modificação da aparência das curvas

    É possível alterar a cor e o layout das funções com instruções simples. Para fazer isso, os argumentos da função `plt.plot` são modificados como quaisquer dois "argumentos de palavra-chave" (*argumentos de palavra-chave* ou **\*\*kwargs**) (lista completa [aqui](https://matplotlib.org/tutorials/introductory/pyplot.html#controlling-line-properties)):| Propriedade | Valor |
    |--------------------|------------------------------------------|
    | `cor` ou `c` | qualquer cor Matplotlib |
    | `rótulo` | qualquer texto |
    | `linestyle` ou `ls` | ('-' ou '--' ou '-.' ou ':' ou 'passos' ou ...) |
    | `largura de linha` ou `lw` | valor do ponto decimal |
    | `marcador` | ('+' ou ',' ou '.' ou '1' ou '2' ou '3' ou '4') |

    As opções para especificar cores estão [aqui](https://matplotlib.org/3.1.0/gallery/color/named_colors.html).Ao especificar um rótulo para cada curva, uma legenda pode então ser invocada.
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, np.pi, 100)
    plt.plot(
        _x,
        np.sqrt(_x),
        label="Raíz cuadrada",
        color="darkmagenta",
        linestyle="--",
        linewidth=2.3,
    )
    plt.plot(_x, np.cos(_x), label="Coseno", c="midnightblue", ls="-.", lw=1.6)
    plt.plot(_x, np.sin(_x), label="Seno", c="firebrick", ls=":", lw=3.1)
    plt.xlabel("$x$")
    plt.ylabel("$f(x)$")
    plt.title("Distintas opciones de línea")
    plt.legend()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.3.5. - Exportar imagens

    Já temos gráficos, como podemos utilizá-los em outras aplicações? A maneira mais simples é exportar a imagem em um formato específico. Os formatos recomendados são:

    * JPG: imagem “rasterizada” (sem perdas).
    * PNG: imagem “rasterizada” (com perdas) que permite transparência.
    * SVG: arquivo vetorial (sem perdas) suportado em navegadores web, LaTeX e outros.
    * PDF: arquivo vetorial portátil não modificável.

    A função Matplotlib para fazer isso é `savefig`, cuja documentação está [aqui](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.savefig.html).Exemplo:```python
    import matplotlib.pyplot as plt

    # Crear grafico aquí

    plt.savefig('/imágenes/sinais', format='png', transparent=True)
    ```onde

    * `/images/` eh a pasta (dentro do diretório atual) onde será salvo
    * `sinais` é o nome do arquivo
    * `format='png'` eh o tipo de arquivo
    * `transparent=True` se as transparências devem ou não ser habilitadas

    ### 2.3.6. - Exportar imagens para $\mathrm{\LaTeX}$

    A biblioteca [TikZplotlib](https://anaconda.org/conda-forge/tikzplotlib)Aqui está uma ferramenta para converter um gráfico Matplotlib em $\mathrm{\LaTeX}$ por meio dos PGFplots do TikZ. É fácil de usar e só precisa ser instalado no terminal antes de usar```bash
    $ pip install tikzplotlib
    ```Semelhante ao caso `savefig` discutido, o procedimento eh:```python
    import tikzplotlib

    # Crear grafico aquí

    tikzplotlib.save('sinais.tex')
    ```onde

    * `sinais.tex` é o nome do arquivo

    O arquivo `.tex` gerado pode então ser compilado em um projeto $\mathrm{\LaTeX}$, criando gráficos nativos, vetoriais e responsivos que parecem ótimos.

    ###2.3.7. - Folhas de estilo Matplotlib

    Matplotlib [permite configurar](https://matplotlib.org/stable/tutorials/introductory/customizing.html)a aparência de gráficos com folhas de estilo que modificam mais de 300 [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams).Por exemplo, um arquivo `mpss.mplstyle` criado para o curso inclui certas configurações:```python
    lines.linewidth     : 4
    axes.prop_cycle     : cycler('color', ['005DA4', '00C0F3', '6DC067', 'FFE06A'])
    axes.spines.right   : False
    axes.spines.top     : False
    ```- a largura das linhas é 4 px
    - Cores UCR em hexadecimal
    - sem eixo direito
    - sem eixo superior

    Por fim, insira o código com:```python
    plt.style.use('./mpss.mplstyle')
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ###Mais informações

    * [Tutorial NumPy](https://unipython.com/numpy-algebra/)* [Tutorial SciPy](https://riptutorial.com/eh/scipy)* [Tutorial Pyplot](https://pybonacci.org/2012/05/14/manual-de-introduccion-a-matplotlib-pyplot-i/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    **Universidade da Costa Rica** | Faculdade de Engenharia | Escola de Engenharia Elétrica

    &copiar; 2021

    ---
    """)
    return


if __name__ == "__main__":
    app.run()
