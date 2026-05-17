import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---

    **Universidade da Costa Rica** | Escola de Engenharia Elétrica

    *IE0405 - Modelos Probabilísticos de Sinais e Sistemas*

    ### `PyX` - Série de tutoriais em Python para análise de dados

    # `Py7` - *Gráficos estatísticos*

    > A visualização dos resultados é fundamental na análise de dados. Python possui bibliotecas complementares como **Matplotlib** e **Seaborn**, entre outras, que oferecem ferramentas avançadas para diversos tipos de gráficos comumente usados ​​em diversos contextos acadêmicos e profissionais.

    *Fabian Abarca Calderón*

    ---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Tipos de gráficos

    Para começar, revisaremos os tipos de gráficos comuns em estatística e análise de dados.

    [Seaborn](https://seaborn.pydata.org/tutorial/function_overview.html)Classifica seus gráficos da seguinte maneira:

    <img src="https://seaborn.pydata.org/_images/function_overview_8_0.png"largura="350">""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Gráficos relacionais

    O mapeamento fornece relações entre duas variáveis em um plano cartesiano.

    - **Scatter plot** (*scatter plot*): diagrama que mostra a relação de duas variáveis ​​como pares ordenados em um plano cartesiano.

    <img src="https://seaborn.pydata.org/_images/scatterplot_5_0.png"largura="300">

    - **Gráfico de linhas** (*gráfico de linhas, gráfico de linhas*): diagrama que mostra a relação de duas variáveis como pares ordenados em um plano cartesiano, conectados por uma linha para denotar uma sequência.

    <img src="https://seaborn.pydata.org/_images/lineplot_9_0.png"largura="300">""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Gráficos de distribuição

    Representação distribuída de um conjunto de valores ao longo de um eixo.

    - **Histograma** (*histograma*): diagrama que agrupa valores numéricos dentro de pequenos intervalos de valores (*bins*) e mostra a distribuição do número de vezes que um valor aparece dentro de cada intervalo, criando uma densidade de probabilidade aproximada.

    <img src="https://seaborn.pydata.org/_images/histplot_1_0.png"largura="300">

    - **Gráfico de estimativa de densidade do kernel** (*Gráfico KDE*): assim como o histograma, é útil para estimar a distribuição da ocorrência de valores amostrais, mas ao estimar $\hat{f}_h(x)$ dá funcionalidade à densidade de probabilidade $f_X(x)$, através de um "[kernel](https://en.wikipedia.org/wiki/Kernel_(statistics))".<img src="https://seaborn.pydata.org/_images/kdeplot_5_0.png"largura="300">

    - **Função de distribuição cumulativa empírica** (*gráfico ECDF*): é uma aproximação da função de distribuição cumulativa (CDF) que representa a proporção ou contagem de observações localizadas abaixo de cada valor em um conjunto de dados.

    <img src="https://seaborn.pydata.org/_images/ecdfplot_1_0.png"largura="300">

    - **Rug plot** (*rug plot*): uma visualização da distribuição marginal de dois dados em um eixo real, como um gráfico de dispersão unidimensional.

    <img src="https://seaborn.pydata.org/_images/rugplot_1_0.png"largura="300">""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Gráficos categóricos

    Representação da distribuição de um conjunto de valores ao longo de um eixo para diferentes variáveis categóricas.

    - **Strip plot** (*strip plot*): um gráfico de dispersão onde uma variável categórica.

    <img src="https://seaborn.pydata.org/_images/seaborn-stripplot-2.png"largura="300">

    - **Swarm plot** (*swarm plot*): um gráfico de dispersão onde uma variável categórica, semelhante a um strip plot, mas os pontos não se sobrepõem.

    <img src="https://seaborn.pydata.org/_images/seaborn-swarmplot-2.png"largura="300">

    - **Box plot ou box and whisker plot** (*box plot*, *box-and-whisker plot*): uma visualização de grupos de dados categóricos por meio de seus *quartis*: o valor mínimo e o maior valor são os "bigodes", a mediana é a linha dentro da caixa, e o primeiro quartil e o terceiro quartil são as bordas da caixa. Seguindo determinados critérios, os valores discrepantes são excluídos, mostrados aqui como pontos.

    <img src="https://seaborn.pydata.org/_images/seaborn-boxplot-2.png"largura="300">

    - **Violin plot** (*violin plot*): tem um papel semelhante ao box plot ao mostrar a distribuição de dados numéricos por quartis em uma categoria, mas combina-o com um gráfico do KDE para representar também a distribuição de ocorrências.

    <img src="https://seaborn.pydata.org/_images/seaborn-violinplot-2.png"largura="300">

    - **Point plot** (*point plot*): o ponto representa a média (ou outro estimador) de dois dados de uma variável categórica e a linha horizontal representa um intervalo de confiança para a estimativa. Fornece menos informações que os gráficos anteriores, mas pode ser útil para representar as mudanças nas medidas de tendência central (média, mediana ou moda) entre uma variável categórica e outra.

    <img src="https://seaborn.pydata.org/_images/seaborn-pointplot-5.png"largura="300">

    - **Bar plot** (*bar plot*): mostra informações semelhantes às do dot plot: a média (ou outra medida de tendência central) e o intervalo de confiança fornecem a estimativa, mas a magnitude fornece a média em uma barra.

    <img src="https://seaborn.pydata.org/_images/seaborn-barplot-1.png"largura="300">""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ##Seaborn

    De acordo com seu [site oficial](https://seaborn.pydata.org/),> Seaborn é uma biblioteca de visualização de dados Python baseada em Matplotlib e compatível com estruturas de dados Pandas. Fornece uma interface de alto nível para desenhar gráficos estatísticos atraentes e informativos.

    <img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg"largura="350">

    **Nota**: Os princípios básicos do Matplotlib já foram abordados em `Py2` e posteriores.

    Com os tipos de gráficos mostrados na seção anterior, a Seaborn tem a capacidade de configurar uma [ampla variedade](https://seaborn.pydata.org/examples/index.html)de alternativas. Aqui mostraremos alguns exemplos básicos.

    Seaborn é importado por convenção como```python
    import seaborn as sns
    ```Abaixo estão alguns exemplos usando conjuntos de dados incluídos na biblioteca.""")
    return


@app.cell
def _():
    # Import seaborn
    import seaborn as sns

    # Apply the default theme
    sns.set_theme()

    # Load an example dataset
    tips = sns.load_dataset("tips")

    # Create a visualization
    sns.relplot(
        data=tips,
        x="total_bill",
        y="tip",
        col="time",
        hue="smoker",
        style="smoker",
        size="size",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ###Mais informações

    * [Página da Web](https://www.google.com/)*Livro ou algo assim
    *Tutorial [w3schools](https://www.w3schools.com/python/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    **Universidade da Costa Rica** | Faculdade de Engenharia | Escola de Engenharia Elétrica

    &copiar; 2021

    ---""")
    return


if __name__ == "__main__":
    app.run()
