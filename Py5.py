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

    # `Py5` - *Curvas de ajuste de dados*

    > Modelos para descrever um fenômeno e seus parâmetros podem ser obtidos a partir de uma amostra de dados. Devido ao grande número de modelos probabilísticos disponíveis, muitas vezes é necessário fazer uma comparação adequada entre muitos deles.

    *Fabian Abarca Calderón* \
    *Jonathan Rojas Sibaja*

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5.1. Ajuste de modelo com SciPy/Stats

    Objetos criados com SciPy/Stats possuem vários métodos, incluindo:

    | Método | Descrição |
    |----------------------------------|------------------------------------------------------------|
    | `rvs()` | Gerador de números aleatórios.                            |
    | `pdf(x)` | Função densidade de probabilidade |
    | `cdf(x)` | Função de probabilidade cumulativa |
    | `stats(momentos=’mv’)` | Média('m'), variância('v'), inclinação('s'), curtose('k'). |
    | `ajustar(dados)` | Estimativa dos parâmetros de melhor ajuste.                   |
    | `mediana()` | Distribuição mediana.                                 |
    | `média()` | Meio dia distribuído.                                   |
    | `var()` | Variância distributiva.                                |
    | `std()` | Desvio padrão da distribuição.                     |

    A função `fit()`, especificamente, encontra os parâmetros de melhor ajuste para um determinado conjunto de dados.

    #### Exemplo

    A seguir, será gerada uma distribuição exponencial com parâmetro $\lambda = 2$ e obtidos os parâmetros de melhor ajuste para os dados aleatórios.

    **Nota**: SciPy/Stats nem sempre usa os mesmos parâmetros teóricos usuais. Exemplo: na função exponencial diz:

    > Uma parametrização comum para expon é em termos do parâmetro de taxa lambda, tal que pdf = lambda * exp(-lambda * x). Esta parametrização corresponde ao uso de escala = 1/lambda.

    Portanto, neste caso o valor $\lambda$ procurado é `lambda = 1/scale` e, portanto, `scale = 1/lambda = 1/2 = 0,5`, para este exemplo.
    """)
    return


@app.cell
def _():
    from scipy import stats

    # Crear objeto aleatorio de ejemplo
    X = stats.expon(0, 1 / 2)

    # Generar números aleatorios a partir de X
    data = X.rvs(400)

    # Estimar parametros de ajuste de dados aleatorios
    params = stats.expon.fit(data)

    print("Los parametros son: loc = {}, scale = {}.".format(params[0], params[1]))
    return (stats,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    É possível perceber que o valor da `escala` está razoavelmente próximo do valor esperado de 0,5.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5.2. Pacote de ajuste

    O pacote `fitter` automatiza e simplifica a obtenção de modelos de melhor ajuste para um conjunto de dados, usando todas as distribuições SciPy/Stats disponíveis (ou algumas, dependendo da especificação).

    Sejam `dados` um conjunto de dados com medidas numéricas de alguma variável de interesse. com

    ```python
    from fitter import Fitter

    f = Fitter(data)
    f.fit()
    ```

    O programa percorrerá todas as distribuições SciPy/Stats e encontrará os parâmetros mais adequados.

    **Observação**: Como há muitas distribuições possíveis, isso pode levar um tempo considerável.

    Então, com:

    ```python
    f = Fitter(data, distributions=['expon', 'norm', 'gamma'])
    ```

    É possível limitar o ajuste a apenas algumas distribuições.

    Com:
          
    ```python
    f.summary()
    ```
          
    É possível obter uma tabela com o ranking de melhor ajuste (baseado no critério da soma dos quadrados do erro) e um gráfico Matplotlib com o histograma dos dados juntamente com as curvas das funções de densidade (PDF) das distribuições da tabela.

    Para obter os parâmetros dessas distribuições, eles estão acessíveis via:
    
    ```python
    f.fitted_param
    ```
    que eh dá forma:
    
    ```python
    {'expon': (1.5516548212580765, 3.837313054949372), 'norm': (5.388967876207449, 2.6612762163716237), 'gamma': (2.059695507081982, 1.4639030411838343, 1.9056503608256832)}
    ```
          
    Ou seja, um dicionário com o nome da distribuição e seus parâmetros de melhor ajuste. Caso seja necessário obter os parâmetros de uma distribuição específica, é possível escrever, por exemplo:
          
    ```python
    f.fitted_param['gamma']
    ```
    e obtenha:
          
    ```python
    (2.059695507081982, 1.4639030411838343, 1.9056503608256832)
    ```
          
    **Nota**: observe que o número de parâmetros varia dependendo da distribuição. Além disso, os parâmetros SciPy/Stats não são necessariamente os mesmos que aparecem na teoria.

    É ainda possível obter os parâmetros da curva de melhor ajuste indicando apenas:```python
    f.get_best()
    ```que retorna o nome da distribuição com melhor ajuste e seus parâmetros como um dicionário.

    No exemplo a seguir será gerada uma amostra de 1000 pontos com uma distribuição de exemplo, e então será utilizado o `fitter`, que irá revisar as mais de 80 distribuições SciPy e exibir um resumo com as distribuições e seus parâmetros.
    """)
    return


@app.cell
def _(stats):
    from fitter import Fitter

    data_1 = stats.gamma.rvs(2, loc=1.5, scale=2, size=1000)
    f = Fitter(data_1, distributions=["expon", "norm", "rayleigh", "uniform"])
    # Crear los dados de ejemplo
    f.fit()
    # Definir cuáles distribuiÃ§Ãµeh va a evaluar
    # Realizar el ajuste para las distribuiÃ§Ãµeh seleccionadas
    # Mostrar principales resultados y grafico
    f.summary()
    return (f,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Os parâmetros de melhor ajuste de todas as distribuições utilizadas estão em:
    """)
    return


@app.cell
def _(f):
    params_1 = f.fitted_param
    print(params_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5.3. Polinômio se ajusta ao módulo `numpy`

    Embora não sejam uma distribuição de probabilidade em si, às vezes funções polinomiais genéricas podem ser usadas para descrever alguns dados. Isto pode ser particularmente útil em distribuições "multimodais", ou seja, que possuem mais de uma concentração de valores, como as seguintes:

    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e2/Bimodal.png"largura="300px">

    Com a função `polyfit()` da biblioteca `numpy` é possível ajustar dados experimentais a polinômios de qualquer ordem. Esta função retorna os parâmetros da linha para um modelo linear na forma:

    $$
    f(x) = mx + b
    $$

    Isto é no caso de um polinômio de grau 1. Um exemplo de utilização deste método é o seguinte:
    """)
    return


app._unparsable_cell(
    r"""
    from numpy import *
    import matplotlib.pyplot as plt

    # Dados experimentales
    x = array([ 0.,  1.,  2.,  3.,  4.])
    y = array([ 10.2 ,  12.1,  15.5 ,  18.3,  20.6 ])

    # Ajustar a uma recta (polinomio de grado 1)
    p = polyfit(x, y, 1)

    # Crear la recta de ajuste obtenida.
    y_ajuste = p[0]*x + p[1]

    # Graficar los dados experimentales
    p_dados, = plt.plot(x, y, 'b.')

    # Agregar la recta de ajuste
    p_ajuste, = plt.plot(x, y_ajuste, 'r-')

    plt.title('Ajuste linear por mÃ­nimos quadrados')
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    plt.legend(('Dados experimentales', 'Ajuste linear'), loc="upper left")
    plt.show()
    """,
    name="_",
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5.4. Métricas de desempenho

    **(Opcional)**

    Para avaliar o ajuste de dois modelos probabilísticos, normalmente são usados um ou mais dos seguintes indicadores de erro.

    Nas definições a seguir, $\hat{x}$ são os dados previstos ou valor previsto e $x$ são os dados medidos ou valor verdadeiro.

    ### Erro máximo

    O erro máximo (ME) captura o maior valor absoluto de erro entre todas as previsões e medições.

    \começo{equação}
        \mathrm{ME} = \max_{1 \leq i \leq n} \{ | \hat{x}_i - x_i | \}
    \label{E:eu}
    \fim{equação}

    ### Erro médio absoluto

    O erro médio absoluto (MAE) encontra a magnitude média do erro para cada medição.

    \começo{equação}
        \mathrm{MAE} = \frac{1}{n} \sum _{i = 1}^n | \hat{x}_i - x_i |
    \label{E:mae}
    \fim{equação}

    ### Erro mediano absoluto

    O erro absoluto mediano (MedAE) encontra o valor médio de dois valores de erro ordenados para cada medição.

    \começo{equação}
        \mathrm{MedAE} = \mathrm{mediana} (| \hat{x}_1 - x_1 |, \ldots, | \hat{x}_i - x_i |)
    \label{E:medae}
    \fim{equação}

    ### Erro percentual médio absoluto

    O erro percentual médio absoluto (MAPE), também chamado de erro relativo médio \acrdef{mre}, é uma modificação do erro absoluto médio que é calculado em termos relativos (porcentagem) ao valor verdadeiro.

    \começo{equação}
        \mathrm{MAPE} = \frac{1}{n} \sum _{i = 1}^n \left| \frac{\hat{x}_i - x_i}{x_i} \right|
    \label{E:mapa}
    \fim{equação}

    ### Erro médio percentual absoluto simétrico

    O erro percentual médio absoluto simétrico (SMAPE) fornece resultados entre 0\% e 200\%.

    \começo{equação}
        \mathrm{SMAPE} = \frac{200\%}{n} \sum _{i = 1}^n \frac{|\hat{x}_i - x_i|}{|\hat{x}_i| + |x_i|}
    \label{E:smape}
    \fim{equação}

    ### Erro quadrático médio

    O erro quadrático médio (MSE) é a média aritmética do quadrado do erro. Penaliza erros grandes com mais rigor do que erros pequenos, dependendo do quadrado da sua magnitude.

    \começo{equação}
        \mathrm{MSE} = \frac{1}{n} \sum _{i = 1}^n ( \hat{x}_i - x_i )^2
    \label{E:mse}
    \fim{equação}

    ### Raiz do erro quadrático médio

    A raiz do erro quadrático médio (RMSE) é sempre positiva e menos sensível que o MSE a valores atipicamente grandes.

    \começo{equação}
        \mathrm{RMSE} = \sqrt{\frac{1}{n} \sum _{i = 1}^n ( \hat{x}_i - x_i )^2}
    \label{E:rmse}
    \fim{equação}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ###Mais informações

    * [Estatísticas SciPy](https://docs.scipy.org/doc/scipy/reference/stats.html)* [Ajustador](https://fitter.readthedocs.io/en/latest/index.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    **Universidade da Costa Rica** | Faculdade de Engenharia | Escola de Engenharia Elétrica

    &copy; 2022

    ---
    """)
    return


if __name__ == "__main__":
    app.run()
