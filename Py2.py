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

    # `Py2` - *Biblioteca de manipulação e análise de dados do Pandas*

    > **Pandas** é uma biblioteca útil e popular de manipulação de dados que oferece estruturas de dados para análise de tabelas numéricas e séries temporais. Pelas suas capacidades, é comparável ao Excel ou outras planilhas, mas de forma *programática*. Esta é uma introdução ao objeto `DataFrame` e suas características básicas.

    *Fabian Abarca Calderón* \
    *Jonathan Rojas Sibaja*

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Biblioteca Pandas

    Para trabalhar com um grande número de dados, é desejável ter um conjunto de ferramentas que nos permita realizar operações comuns de forma intuitiva e eficiente. Pandas, uh, é resolvido por padrão fazer isso em Python e faz parte do ecossistema SciPy. Ele vem instalado com o Anaconda.

    **Nota 0**: A documentação oficial está em [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/).Este guia é baseado em "[Tutoriais de primeiros passos](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)".**Nota 1**: Para todo este guia será feita a seguinte importação de biblioteca.

    **Nota 2**: Por convenção, o *alias* do Pandas é `pd`.
    """)
    return


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import datetime

    return np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Estruturas de Dados Pandas

    O Pandas permitirá a criação de novas estruturas de dados `Series` e `DataFrame`, que são classes otimizadas para manipulação de dados. Embora sejam semelhantes em forma às estruturas Python, como listas e dicionários, na verdade incorporam um grande número de novos atributos e métodos:

    | Classe | Atributos | Métodos |
    |------------|------------|---------|
    | `Série` | 20+ | 180+ |
    | `DataFrame` | 10+ | 210+ |

    - [Documentação](https://pandas.pydata.org/docs/reference/series.html)de `Série`
    - [Documentação](https://pandas.pydata.org/docs/reference/frame.html)de `DataFrame`
    ---
    ##3.1. - `Série`

    Em Python, `Series` corresponde a um array de **uma** dimensão que suporta vários tipos de dados (inteiros, palavras, números flutuantes, objetos Python, etc.) e que também são rotulados por um índice que o usuário pode definir ou permitir que o Python crie por padrão.

    Para criar listas ou `Séries` de valores, é utilizada a seguinte sintaxe:

    ```python
    pandas.Series(data=None, index=None,
                  dtype=None, name=None, copy=False, fastpath=False)
    ```

    onde `data` é uma sequência ou estrutura de dados iterável do Python, como uma lista, uma tupla, um dicionário, um intervalo, etc. O exemplo a seguir possui indexação automática.
    """)
    return


@app.cell
def _(np, pd):
    s = pd.Series([1, 3, 5, np.nan, "modelos", 8.5])

    # Ver objeto Series
    print(s)

    # Utilizar atributo .count
    print("Número de elementos no nulos: {}.".format(s.count()))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Usando o comando NumPy `random.randn` é possível gerar dados aleatórios para a lista. Também é possível adicionar índices diferentes dos numéricos, usando o argumento `index` e uma lista de índices do mesmo tamanho dos indicados.
    """)
    return


@app.cell
def _(np, pd):
    s_1 = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
    print(s_1)
    p = pd.Series([1, "!", 5, "?", "hola", 13], index=[6, 5, 4, 3, 2, 1])
    print(p)
    q = pd.Series(range(5), index=["a", "b", "c", "d", "e"])
    print(q)
    return q, s_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    É possível inspecionar os atributos e métodos de dois objetos `Series` criados anteriormente com a função `dir()` do Python, e descritores estatísticos como correlação ou média podem ser vistos.
    """)
    return


@app.cell
def _(s_1):
    print(dir(s_1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Uma vez criado o objeto `Series`, podemos executar operações vetoriais com ele ou adicionar outros atributos, como um nome.
    """)
    return


@app.cell
def _(pd, q):
    _d = pd.Series(q + q, name="soma")
    print(_d)
    e = pd.Series(q**2, name="potencia")
    print(e)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ##3.2. - `DataFrame`

    No Pandas, um `DataFrame` corresponde a um array **bidimensional** rotulado, semelhante à concatenação de várias `Series`. Tambem suporta vários tipos de dados.

    > Um `DataFrame` possui funcionalidade equivalente a uma planilha ou tabela SQL e permite que os dados sejam manipulados de forma versátil e eficiente.

    A sintaxe de criação de um `DataFrame` eh:```python
    pandas.DataFrame(data=None, index=None,
                     columns=None, dtype=None, copy=None)
    ```onde `data` normalmente é um dicionário no qual cada chave/valor descreve uma coluna. No entanto, ele pode ser criado de diversas outras maneiras, como a partir de arquivos JSON ou CSV importados.

    A atribuição dos rótulos pode ser decidida pelo usuário e o Python corresponderá aos valores, caso haja diferenças nos tamanhos das listas agregadas, preencherá esses espaços seguindo regras de bom senso.

    Vamos seguir um exemplo de duas ‘Séries’ de tamanhos diferentes. Observe as diferenças na ordem dos dois índices.
    """)
    return


@app.cell
def _(pd):
    # Creación de um diccionario com las series indexadas
    _d = {
        "esta": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
        "otra": pd.Series([1.0, 2.0, 3.0, 4.0], index=["c", "a", "d", "b"]),
    }
    df = pd.DataFrame(_d)
    # Creación del DataFrame a partir del diccionario
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Com `dir()` também é possível consultar atributos e métodos disponíveis de `DataFrame`.

    ##### Exemplo com tipo de índice "timestamp"

    Os índices podem ser um carimbo de data/hora (*timestamp*). Este é um caso útil em que, por exemplo, um registro de diversas variáveis ​​(as colunas) é mantido em uma sucessão de momentos diferentes (o índice):
    """)
    return


@app.cell
def _(np, pd):
    # Creación de um rango de fechas
    fechas = pd.date_range("20200101", periods=6)
    df_1 = pd.DataFrame(np.random.randn(6, 4), index=fechas, columns=list("ABCD"))
    # Creación de um DataFrame com las fechas como índices
    df_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Exemplo com diferentes tipos de dados

    Assim como em `Series`, `DataFrames` podem usar diferentes tipos de dados em cada coluna e ser atribuídos como dicionários.
    """)
    return


@app.cell
def _(np, pd):
    df_2 = pd.DataFrame(
        {
            "A": 1.0,
            "B": pd.Timestamp("20200101"),
            "C": pd.Series(1, index=list(range(4))),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["norte", "sur", "este", "oeste"]),
            "F": "hola",
        }
    )
    df_2
    return (df_2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Modificações no `DataFrame`

    Uma vez inicializado o `DataFrame`, ações como extrair, excluir e inserir colunas podem ser executadas, com uma sintaxe semelhante à de dois [dicionários](https://www.w3schools.com/python/python_dictionaries.asp).
    """)
    return


@app.cell
def _(df_2):
    # Extraer uma columna
    df_2["E"]
    return


@app.cell
def _(df_2):
    # Eliminar columna 'F'
    del df_2["F"]
    # Mostrar nuevo DataFrame sin columna 'F'
    df_2
    return


@app.cell
def _(df_2, np, pd):
    # Asignar nuevos dados a la columna 'A'
    df_2["A"] = pd.Series(np.random.randn(4), index=list(range(4)))
    df_2
    return


@app.cell
def _(df_2):
    # Crear nueva columna 'A+' y agregar valores segundo criterio
    df_2["A+"] = df_2["A"] > 0
    # Mostrar nuevo DataFrame
    df_2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ##3.3. - Inspecione os dados

    É possível (e útil) “dar uma olhada” no primeiro e no último dado. Por exemplo, no `DataFrame` chamado `df` você pode ver as primeiras ***N*** linhas de dados com o comando `head`.
    """)
    return


@app.cell
def _(df_2):
    df_2.head(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Se você deseja exibir apenas as três últimas linhas, use o comando `tail`:
    """)
    return


@app.cell
def _(df_2):
    df_2.tail(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Para exibir os índices, use:
    """)
    return


@app.cell
def _(df_2):
    df_2.index
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Exemplo de conversão para NumPy

    Quando desejar, você pode transformar o `DataFrame` em um `array` NumPy.
    """)
    return


@app.cell
def _(df_2):
    df_2.to_numpy()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Acima se o `DataFrame` possui um único tipo ou vários tipos de dados.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Exemplo de manipulação para um único tipo de dado

    Se todos os elementos forem do mesmo tipo, algumas funções específicas de análise e manipulação podem ser executadas, principalmente se forem dados numéricos.

    A seguir, um array do tipo `DataFrame` 6$\times$4 de números aleatórios é criado.
    """)
    return


@app.cell
def _(np, pd):
    df_num = pd.DataFrame(
        np.random.randn(6, 4),
        columns=list("ABCD"),
        index=["a", "b", "c", "d", "e", "f"],
    )

    df_num
    return (df_num,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    É possível obter um resumo de dois descritores estatísticos principais de cada coluna, neste caso: a contagem de elementos, a média, o desvio padrão, o valor mínimo, o primeiro, segundo e terceiro quartil, e o valor máximo.
    """)
    return


@app.cell
def _(df_num):
    df_num.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Reordenar dados

    É comum querer reordenar os dados com alguma coluna de referência:
    """)
    return


@app.cell
def _(df_num):
    df_num.sort_values(by="B")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ##3.4. - Selecione dados

    > Em Python, selecionar (ou pesquisar) dados usando Pandas é mais eficiente do que expressões para selecionar e obter dados em NumPy.

    Por exemplo, para localizar uma **linha** de dados, você pode usar o comando `loc`, que possui diversas opções de busca por índices, conforme [documentacao](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html).
    """)
    return


@app.cell
def _(df_2):
    df_2.loc[2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Você também pode selecionar um intervalo de linhas (registros) ao mesmo tempo:
    """)
    return


@app.cell
def _(df_2):
    df_2[0:3]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Para obter uma posição específica, você deve indicar a linha e a coluna usando o comando `at`:
    """)
    return


@app.cell
def _(df_2):
    df_2.at[2, "E"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Você pode localizar esse mesmo elemento pela posição de meio dia e não pelos índices, usando o comando `iloc`:
    """)
    return


@app.cell
def _(df_2):
    df_2.iloc[2, 4]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Podemos localizar os dados que atendem a uma determinada condição booleana:
    """)
    return


@app.cell
def _(df_2):
    df_2[df_2["A"] > 0]
    return


@app.cell
def _(df_2):
    df_2[df_2["E"] == "sur"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ##3.5. - Operações em dados

    Em Python, as operações são executadas em todos os dados, retornando o valor de saída por linhas ou colunas.

    Por exemplo, para calcular a média estatística de dois dados de cada coluna, é usado o comando `mean`, que percorre a dimensão `0` (linhas) da seguinte forma:
    """)
    return


@app.cell
def _(df_num):
    df_num.mean(0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Se, porém, você deseja saber a média de dois valores por linha, utiliza-se a seguinte variação, onde `1` é a dimensão das colunas:
    """)
    return


@app.cell
def _(df_num):
    df_num.mean(1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Exemplo de contagem de ocorrências de valores únicos

    Para a seguinte série de exemplos:
    """)
    return


@app.cell
def _(np, pd):
    letras = ["a", "b", "c", "d", "e"]
    serie = pd.Series(np.random.choice(letras, size=15))
    serie
    return (serie,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Você pode aplicar operações como contagem (ou "ocorrências de cada um") em `Series` ou `DataFrame` e retornar um resultado classificado do maior para o menor número de ocorrências.
    """)
    return


@app.cell
def _(serie):
    serie.value_counts()
    return


@app.cell
def _(df_2):
    df_2.value_counts(df_2["A+"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Operações em personagens

    Existem também operações que podem ser aplicadas a 'Séries' de palavras:
    """)
    return


@app.cell
def _(pd):
    G = pd.Series(["ÁRbOL", "BLanCO", "AvE", "BuRRo"])
    g = G.str.lower()

    pd.DataFrame({"G": G, "g": g})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ##3.6. - Mesclar dados

    No Pandas, para concatenar dados você usa o comando `concat()` onde```python
    pandas.concat(objs, axis=0, join='outer', ignore_index=False,
                  keys=None, levels=None, names=None, verify_integrity=False,
                  sort=False, copy=True)[source]
    ```onde `axis=` determina ao longo de qual dimensão eles são concatenados: `0` linhas (vertical) e `1` colunas (horizontal) têm a seguinte forma:
    """)
    return


@app.cell
def _(np, pd):
    # Crear DataFrame de ejemplo
    df_a = pd.DataFrame(np.random.randn(5, 2))
    df_b = pd.DataFrame(np.random.randn(5, 2))

    # Extraer fragmentos y concatenarlos
    fragmentos = [df_a[:], df_b[:]]
    pd.concat(fragmentos, axis=0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Nota**: Observe que é necessário extrair os fragmentos primeiro porque você não pode concatenar `DataFrame` diretamente.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ##3.7. - Dados de grupo

    Em Pandar, "grupo" refere-se a:

    - Separe os dados em grupos com base em critérios.
    - Aplicar uma função a cada grupo de forma independente.
    - Combine os resultados em uma estrutura de dados.

    Abaixo está um exemplo de agrupamento aplicando uma soma às colunas numéricas associadas por um determinado critério:
    """)
    return


@app.cell
def _(np, pd):
    df_foo = pd.DataFrame(
        {
            "A": ["foo", "bar", "foo", "bar", "foo"],
            "B": ["uno", "dos", "dos", "tres", "dos"],
            "C": np.random.randn(5),
            "D": np.random.randn(5),
        }
    )
    df_foo
    return (df_foo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    O resultado a seguir agrupa as linhas com os elementos em `A` e adiciona os resultados de colunas não categóricas (ou seja, numéricas), que neste caso são `C` e `D`.
    """)
    return


@app.cell
def _(df_foo):
    df_foo.groupby("A").sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Os resultados a seguir agrupam primeiro por `A` e depois por `B`, para finalmente adicionar as colunas associadas `C` e `D`.
    """)
    return


@app.cell
def _(df_foo):
    df_foo.groupby(["A", "B"]).sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ##3.8. - Reorganizar dados

    ##### Pilha

    No Pandas, uma forma de reorganizar os dados é usando o comando `stack`:
    """)
    return


@app.cell
def _(df_2):
    pila = df_2.stack()
    pila
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Tabela dinâmica

    Você também pode alterar a forma como os dados são organizados como tabelas dinâmicas:
    """)
    return


@app.cell
def _(np, pd):
    df_piv = pd.DataFrame(
        {
            "A": ["uno", "uno", "dos", "tres"] * 3,
            "B": ["A", "B", "C"] * 4,
            "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
            "D": np.random.randn(12),
            "E": np.random.randn(12),
        }
    )
    df_piv
    return (df_piv,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A tabela a seguir resumirá os valores em `D` associados ao agrupamento em relação a `A` e `B`, para cada categoria em `C`. É uma ferramenta **poderosa**.
    """)
    return


@app.cell
def _(df_piv, pd):
    v = pd.pivot_table(df_piv, values="D", index=["A", "B"], columns=["C"])
    v
    return (v,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Como extrair um elemento de uma tabela dinâmica?
    """)
    return


@app.cell
def _(v):
    v["bar"]["dos"]["B"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ##3.9. - Série Tempo

    No Pandas, as séries de andamento permitem gerar sequências com uma frequência fixa durante um período de andamento, como:
    """)
    return


@app.cell
def _(pd):
    # Tres ciclos horarios que inician el 1 de enero de 2020
    dti = pd.date_range("1-1-2020", periods=3, freq="H")
    dti
    return (dti,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cuja hora pode ser convertida para um fuso horário diferente:
    """)
    return


@app.cell
def _(dti):
    dti_1 = dti.tz_localize("America/Costa_Rica")
    dti_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Você também pode converter uma série de andamento para uma frequência específica:
    """)
    return


@app.cell
def _(pd):
    idx = pd.date_range("2020-01-01", periods=5, freq="H")
    ts = pd.Series(range(len(idx)), index=idx)
    ts
    return (ts,)


@app.cell
def _(ts):
    ts.resample("2H").mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ##3.10. - Gráficos

    Em Python, o mapeamento padrão é usado para usar os comandos da API `matplotlib` como métodos `Series` e `DataFrame`. Assim, por exemplo, você pode representar graficamente uma `série` de dados:
    """)
    return


@app.cell
def _(np, pd):
    import matplotlib.pyplot as plt

    plt.close("all")
    ts_1 = pd.Series(
        np.random.randn(1000), index=pd.date_range("1/1/2020", periods=1000)
    )
    ts_1 = ts_1.cumsum()
    # Crear serie temporal
    ts_1.plot()
    plt.xlabel("Días")
    # Suma acumulada
    # Método .plot() de Matplotlib sobre la serie temporal
    plt.ylabel("Valor")
    return plt, ts_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Arranjos do tipo `DataFrame` também podem ser representados graficamente de forma que várias curvas sejam representadas no mesmo gráfico, conforme mostrado abaixo:
    """)
    return


@app.cell
def _(np, pd, plt, ts_1):
    # Crear números aleatorias com el mísmo índice de ts
    df_3 = pd.DataFrame(
        np.random.randn(1000, 4), index=ts_1.index, columns=["A", "B", "C", "D"]
    )
    df_3 = df_3.cumsum()
    plt.figure()
    df_3.plot()
    # Graficar las curvas
    plt.legend(loc="best")
    plt.xlabel("Días")
    plt.ylabel("Valor")
    return (df_3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ##3.11. - Dados de importação e exportação

    Pandas é um excelente “gerenciador” de arquivos de dados externos, como `.xls` ou `.csv`. Por exemplo, para criar um arquivo `models.csv` a partir de dois dados anteriores:
    """)
    return


@app.cell
def _(df_3):
    df_3.to_csv("modelos")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cujo conteúdo pode ser "chamado" novamente usando o comando a continuidade, que o salva como um `DataFrame`.
    """)
    return


@app.cell
def _(pd):
    pd.read_csv("modelos")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ###Mais informações

    * [Página oficial do Pandas](https://pandas.pydata.org/)
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
