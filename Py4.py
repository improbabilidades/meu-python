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

    # `Py4` - *Introdução ao módulo de funções estatísticas*

    > O módulo **stats** do SciPy oferece ferramentas para manipular a distribuição estatística. Entre eles: identificação de parâmetros de ajuste de dados, cálculo de probabilidades em um intervalo, representação gráfica de funções de distribuição, geração de dados aleatórios com determinada distribuição, etc.

    *Fabian Abarca Calderón*

    ---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## módulo `estatísticas````python
    from scipy import stats
    ```> Este módulo contém um grande número de distribuições de probabilidade, bem como uma biblioteca crescente de funções estatísticas.

    Com mais de 100 distribuições estatísticas diferentes, provavelmente aquela de que precisamos está lá. Tem uma variedade de:

    *Distribuições contínuas
    * Distribuições multivariadas
    * Distribuições discretas
    *Descritores estatísticos (*estatísticas resumidas*)
    *...

    A documentação oficial está em [Funções estatísticas (scipy.stats)](https://docs.scipy.org/doc/scipy/reference/stats.html).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ## 4.1. - Criação de um “objeto aleatório”

    Para iniciar a manipulação de distribuições, existem *classes* gerais de variáveis aleatórias que são:

    * `rv_continuous`: Uma classe genérica de variável aleatória **contínua**.
    * `rv_discrete`: Uma classe genérica de variável aleatória **discreta**.
    * `rv_histogram`: Gera uma distribuição dada por um histograma.

    (`rv` vem de *variável aleatória*). Por sua vez, existem **subclasses** dessas categorias que representam as distribuições a serem utilizadas. Por exemplo:```python
    from scipy import stats

    W = stats.uniform(0,1)  # distribuicao uniforme
    X = stats.expon(0,1)    # distribuicao exponencial
    Y = stats.norm(0,1)     # distribuicao normal
    Z = stats.rayleigh(0,1) # distribuicao Rayleigh
    ```Aqui, `W`, `X`, `Y` e `Z` são objetos que herdam as propriedades das distribuições indicadas. Diz-se também que são uma versão "congelada" de uma variável aleatória.

    A lista completa está em [Funções estatísticas (scipy.stats)](https://docs.scipy.org/doc/scipy/reference/stats.html).
    """)
    return


@app.cell
def _():
    from scipy import stats

    _X = stats.uniform(0, 1)
    print(type(_X))
    return (stats,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ## 4.2. - Geração aleatória de dados

    Muitas vezes é necessário gerar dados aleatórios com uma distribuição de probabilidade específica. Em `stats` o método é `rvs` (de *variáveis ​​aleatórias*), aplicado a um objeto aleatório predefinido.""")
    return


@app.cell
def _(stats):
    _X = stats.uniform(0, 1)
    _a = _X.rvs()
    _b = _X.rvs(5)
    print(_a)
    print(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ## 4.3. - Funções de distribuição

    Os objetos aleatórios disponibilizam as duas funções de distribuição associadas a cada modelo probabilístico.

    As funções de distribuição são relevantes para calcular probabilidades, calcular momentos e fazer gráficos, entre outras coisas.

    ### 4.3.1. - Função densidade de probabilidade

    O método `pdf` retorna a *função de densidade de probabilidade* $f_X(x)$, que pode ser avaliada para qualquer valor específico $x$.

    ### 4.3.2. - Função de probabilidade de massa

    O método `pmf` retorna a *função de massa de probabilidade* $f_X(x) = P_X(x)$ para uma variável aleatória **discreta** e pode ser avaliada em valores $x$ discretos.

    ### 4.3.3. - Função de probabilidade cumulativa

    O método `cdf` retorna a *função de distribuição cumulativa* $F_X(x)$, que pode ser avaliada para qualquer valor $x$ específico.

    *Exemplo*

    Para a distribuição [log-normal] (https://en.wikipedia.org/wiki/Log-normal_distribution)`estatísticas` [amostra](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lognorm.html#scipy.stats.lognorm)a seguinte função de densidade de probabilidade:

    $$
    \displaystyle f_X(x,s) = {\frac{1}{s x {\sqrt {2\pi }}}}\ \exp \left(-{\frac {\left(\ln x \right)^{2}}{2 s^{2}}}\right)
    $$

    Uma avaliação numérica em $f_X(2,1)$, com parâmetro $s = 1$ resulta em $f_X(2,1) \approx 0,15687$.""")
    return


@app.cell
def _(stats):
    _X = stats.lognorm(1)
    _a = _X.pdf(2)
    print(_a)
    Y = stats.norm(0, 1)
    _b = Y.pdf(0)
    c = Y.cdf(0)
    print(_b, c)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 4.3.4. - Função quantil

    O método `ppf` retorna a *função de ponto de probabilidade* $Q_X(p)$, que pode ser avaliada para qualquer valor de probabilidade $0 \leq p \leq 1$.

    A função quantil eh o inverso fornece a função cumulativa (e, portanto, às vezes sua notação eh $F_X^{-1}(p)$) e indica o valor $x$ em que $P(X \leq x) = p$. É útil porque permite saber onde os $100p$% são distribuídos. $Q_X(0.45)$ é interpretado como "em que valor de $x$ 45% da probabilidade distribuída é acumulada?"

    É frequentemente usado em gráficos para delimitar adequadamente o suporte que a curva possui.

    No exemplo abaixo, 1% de uma distribuição uniforme entre 0 e 1 é claramente 0,01 e 99% é 0,99, mas, exceto neste exemplo, raramente é tão fácil saber.""")
    return


@app.cell
def _(stats):
    import numpy as np

    _X = stats.uniform(0, 1)
    _a = _X.ppf(0.01)
    _b = _X.ppf(0.99)
    print(_a, _b)
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""###4.3.5. - Função de sobrevivência

    O método `sf` retorna a *função de sobrevivência* $S_X(x)$, que pode ser avaliada para qualquer valor específico $x$.

    A função de sobrevivência é o complemento da função cumulativa,

    $$
    S_X(x) = P(X > x) = 1 - P(X \leq x) = 1 - F_X(x)
    $$""")
    return


@app.cell
def _(stats):
    _X = stats.chi(10)
    _a = _X.cdf(3)
    _b = _X.sf(3)
    print(_a, _b, _a + _b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ## 4.4 - Gráficos de funções de distribuição

    Com a ajuda do Matplotlib é possível e desejável representar graficamente a forma das funções de distribuição. Por exemplo, com a função normal e lembrando que sua distribuição é dada por:

    $${\displaystyle f_X(x) = {\frac {1}{\sqrt {2\pi \sigma ^{2}}}}e^{-{\frac {(x-\mu )^{2}}{2\sigma ^{2}}}}}$$

    então são obtidos os gráficos da função densidade e da função cumulativa.""")
    return


@app.cell
def _(np, stats):
    import matplotlib.pyplot as plt

    _X = stats.norm(0, 1)
    _x = np.linspace(_X.ppf(0.01), _X.ppf(0.99), 100)
    plt.plot(_x, _X.pdf(_x))
    plt.title("Distribución normal")
    plt.ylabel("$f_X(x)$")
    plt.xlabel("$x$")
    plt.show()
    plt.figure()
    plt.plot(_x, _X.cdf(_x))
    plt.plot(_x, _X.sf(_x))
    plt.title("Distribución normal")
    plt.legend(["$F_X(x)$", "$S_X(x)$"])
    plt.xlabel("$x$")
    plt.show()
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ## 4.5 - Modificação dos parâmetros de distribuição

    Todas as variáveis aleatórias são definidas por parâmetros (com símbolos diferentes, como $\lambda$, $\mu$, $\alpha$, etc.). No módulo `stats`, entretanto, os parâmetros são geralmente especificados como "localização" e "escala". Sem alterar nenhum desses parâmetros, as distribuições são **normalizadas** ou **padronizadas**. O efeito que os parâmetros têm:

    * `loc` (*location*) mudará a média distribuída.
    * `scale` irá "dispersar" a distribuição.

    ### 4.5.1 - Exemplo com a distribuição Rayleigh

    A função de densidade de probabilidade Rayleigh

    $${\displaystyle f_X(x) = {\frac {x}{\sigma ^{2}}}e^{-x^{2}/\left(2\sigma ^{2}\right)}}$$

    Para $x \geq 0$. E normalizado ($\sigma = 1$) eh

    $${\displaystyle f_X(x) = {{x}}e^{-x^{2}/2}}$$

    Para modificá-lo em `stats`, faça

    * `rayleigh.pdf(x, loc, scale)`, que é equivalente a
    * `rayleigh.pdf(y) /escala` com `y = (x - loc) /escala`

    Isto é,

    $${ \displaystyle f_X(x) = {\frac {(x - \mathsf{loc})}{\mathsf{scale}^2}} e^{\frac{-(x - \mathsf{loc})^{2}}{(2~\cdot~ \mathsf{scale}^2)}} }$$

    E corresponde neste caso específico que $\sigma$ = `scale`. Às vezes `shift` = `loc` é usado como notação porque, na verdade, é uma mudança para $x_0$.""")
    return


@app.cell
def _(np, plt, stats):
    locs = range(1, 6)
    scales = range(1, 6)
    plt.figure()
    plt.title("Distribución de Rayleigh com varios parametros de escala")
    plt.ylabel("$f_X(x)$")
    plt.xlabel("$x$")
    for scale in scales:
        R = stats.rayleigh(0, scale)
        _x = np.linspace(0, 16, 100)
        plt.plot(_x, R.pdf(_x), label="$\\sigma$ = " + str(scale))
        plt.legend()
    plt.figure()
    plt.title("Distribución de Rayleigh com varios parametros de localizacao")
    plt.ylabel("$f_X(x)$")
    plt.xlabel("$x$")
    for loc in locs:
        R = stats.rayleigh(loc, 4)
        _x = np.linspace(loc, 20, 100)
        plt.plot(_x, R.pdf(_x), label="$x_0$ = " + str(loc))
        plt.legend()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ## 4.6. - Cálculo de probabilidades

    Normalmente, o cálculo de probabilidades é feito de duas maneiras:

    * Integração em uma região $\mathcal{R}$ dá a função de densidade $f_X(x)$.
    * Com a função cumulativa, ela tem a forma $P(a < X < b) = F_X(b) - F_X(a)$.

    ### 4.6.1. - Integração da função densidade

    A biblioteca oferece maneiras de fazer integração numérica

    $$
    \int_{\mathcal{R}} f_X(x) ~\mathrm{d}x
    $$

    #### Exemplo de probabilidade em uma distribuição exponencial

    A variável aleatória exponencial tem PDF:

    $$
    f_X(x) = \lambda e^{-\lambda x}
    $$

    onde é possível determinar que $E[X] = 1/\lambda$ e também $\sigma_X^2 = 1/\lambda^2$.

    O módulo `integrate` do `scipy` (informacao [aqui](https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html))realizar integrações numéricas com diferentes métodos, sejam funcoes ou amostras de dados. O método `quad` realiza integrações de uso geral.""")
    return


@app.cell
def _(np):
    from scipy.integrate import quad

    def exponencial(x, lbd):
        return lbd * np.exp(-lbd * _x)

    _a, _ = quad(exponencial, 1, 3, args=0.5)
    _b, _ = quad(exponencial, 4, np.inf, args=0.5)
    print(_a)
    print(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Alternativamente, com la [funcao](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.trapz.html)`trapz` pode integrar uma função $f(x)$ em $x$, usando assim as funções de densidade de `stats`.

    **Nota**: não confunda `trapz` a integração de `scipy.integrate` com `trapz` a distribuição de probabilidade de `scipy.stats`.""")
    return


@app.cell
def _(np, stats):
    from scipy import trapz

    _X = stats.expon(0, 1 / 0.5)
    _x = np.linspace(1, 3, 100)
    _a = trapz(_X.pdf(_x), _x)
    _x = np.linspace(4, _X.ppf(0.999), 100)
    _b = trapz(_X.pdf(_x), _x)
    print(_a)
    print(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ### 4.6.2. - Subtração da função de probabilidade cumulativa

    Sabendo disso

    $$P(a < X < b) = F_X(b) - F_X(a)$$

    É fácil fazer a avaliação com as ferramentas 'estatísticas'.""")
    return


@app.cell
def _(np, stats):
    _X = stats.expon(0, 1 / 0.5)
    _a = _X.cdf(3) - _X.cdf(1)
    _b = _X.cdf(np.inf) - _X.cdf(4)
    print(_a)
    print(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ###Mais informações

    * [Funções estatísticas (scipy.stats)](https://docs.scipy.org/doc/scipy/reference/stats.html)
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
