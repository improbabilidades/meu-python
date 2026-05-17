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

    # `Py6` - *Troca de dados com serviços web*

    > Interfaces de programação de aplicativos **API** permitem a aquisição e modificação de dados de servidores externos. No contexto do curso, esta é uma ferramenta útil para trabalhar com a imensa quantidade de dados disponíveis na Internet, muitos dos quais estão disponíveis na forma de *APIs RESTful* e são acessíveis com Python.

    *Fabian Abarca Calderón*

    ---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Serviços da Web de dados

    Com a filosofia de “dados abertos” ou outras motivações semelhantes, existem muitos serviços na Internet que oferecem acesso público aos seus dados – gratuitamente ou não, com registo ou não – em áreas tão diversas como dados ambientais, dados governamentais, dados de saúde, etc.

    - **DataHub**: possui um grande número de [coleções](https://datahub.io/collections)de dados incluindo indicadores económicos, alterações climáticas, cinema e televisão, demografia, futebol e outros dados de referência como listas de países, cidades, línguas, entre outros.
    - **Observatório Urbano**: eh "a maior [coleção](https://urbanobservatory.ac.uk/)dados urbanos em tempo real no Reino Unido", com mais de 50 tipos de dados de sensores, incluindo qualidade do ar, radiação solar, ruído, temperatura atmosférica e tráfego de veículos e pessoas.
    - **RECOPE**: tem alguns [dados](https://dadosabiertos.recope.go.cr/servicio-api)de interesse relacionados aos hidrocarbonetos, como o preço internacional do petróleo e os preços ao consumidor de cada produto comercializado na Costa Rica, ou seja, supergasolina, gasolina mais 91 (“normal”), diesel e querosene.

    **Observação**: Este guia é baseado em "[APIs Python e REST: Interagindo com Serviços Web](https://realpython.com/api-integration-in-python/)".
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ## 6.1 - API com arquitetura REST

    Uma Interface de Programação de Aplicativo (API) permite que operações sejam realizadas entre um cliente (por exemplo, um programa Python) e um servidor remoto, no qual o servidor processa uma solicitação do cliente relacionada aos seus recursos e retorna uma resposta. Esta solicitação pode ser para consulta, criação, atualização ou exclusão de dados (**CRUD**, *Criar, Ler, Atualizar, Excluir*), entre outros.

    Neste contexto, um “recurso” é um determinado documento identificado por uma URL (endereço web).

    #### REST (transferência de estado representacional)

    > ...eh um **estilo de arquitetura de software** que define um padrão para comunicações de cliente e servidor em uma rede. REST fornece um conjunto de restrições para arquitetura de software para promover desempenho, escalabilidade, simplicidade e confiabilidade no sistema ([Real Python](https://realpython.com/api-integration-in-python/)).Uma API web que obedece às restrições REST é informalmente descrita como **RESTful**. APIs web RESTful geralmente dependem de métodos HTTP para acessar recursos por meio de *parâmetros codificados em URL* e do uso de JSON ou XML para transmitir dados ([Wikipedia](https://en.wikipedia.org/wiki/Representational_state_transfer)).#### O que uma API nos permite fazer então?

    Existem dezenas ou centenas de serviços disponíveis. Exemplos:

    - Obtenha informações sobre a temperatura ambiente medida em uma estação próxima
    - Obtenha informações musicais do Spotify
    - Descubra a localização da Estação Espacial Internacional
    - Preveja dados com algoritmos de inteligência artificial
    - Conheça os dados do terremoto em tempo real

    Esta [lista](https://github.com/public-apis/public-apis)de APIs públicas eh imensas.

    ### 6.1.1. Métodos HTTP

    A comunicação entre o cliente e o servidor com uma API normalmente acontece via protocolo **HTTP** (*Hypertext Transfer Protocol*), que permite as seguintes solicitações:

    | Método HTTP | Descrição |
    |-------------|---------------------------------------|
    | `OBTER` | Extraia um recurso disponível.                |
    | `POSTAR` | Crie um novo recurso.                       |
    | `COLOCAR` | Atualize um recurso existente.              |
    | `PATCH` | Atualize parcialmente um recurso existente. |
    | `EXCLUIR` | Exclua um recurso existente.                |

    E [outros](https://developer.mozilla.org/eh/docs/Web/HTTP/Methods).### 6.1.2. Códigos de status HTTP

    As respostas do servidor às solicitações dos clientes se enquadram em diversas categorias:

    | Código | Categoria |
    |--------|------|
    | 1XX | Informação |
    | 2XX | Operação bem sucedida |
    | 3XX | Redirecionar |
    | 4XX | Erro do cliente |
    | 5XX | Erro no servidor |

    Alguns exemplos típicos são:

    | Código | Significado | Descrição |
    |---------|-------------------------|----------------------------------------------------------------------|
    | 200 | `OK` | A solicitação solicitada foi realizada com sucesso.                  |
    | 201 | `Criado` | Um novo recurso foi criado.                                   |
    | 204 | `Sem conteúdo` | A solicitação foi bem-sucedida, mas a resposta não tem conteúdo. |
    | 401 | `Não autorizado` | O cliente não está autorizado a realizar o serviço solicitado. |
    | **404** | `Não encontrado` | O recurso solicitado não foi encontrado.                       |
    | 500 | `Erro interno do servidor` | O servidor retornou um erro ao processar a solicitação.   |

    <img src="https://media0.giphy.com/media/jkZtSdwKOx05BOlapR/giphy.gif?cid=ecf05e47zpqivnrg65ywkr5luxl2hqk1n34qzoqbi3rbsg46&rid=giphy.gif&ct=g"largura="250">

    A [lista completa](https://eh.wikipedia.org/wiki/Anexo:C%C3%B3digos_de_estado_HTTP)uh, mais de 50 códigos.

    ### 6.1.3. API *pontos de extremidade*

    > Uma API REST expõe um conjunto de **URLs públicos** que os aplicativos cliente usam para acessar os **recursos** de um serviço web. Essas URLs, no contexto de uma API, são chamadas de ***endpoints*** ([Real Python](https://realpython.com/api-integration-in-python/)).##### Exemplo de uma API hipotética no UCR

    Suponha que a Universidade da Costa Rica possua uma API com as informações de dois cursos que ministra e de seus professores. Seus *pontos finais* poderiam ser:

    - URL base:```http
    https://api.ucr.ac.cr/
    ```| Método HTTP | *Ponto final* | Descrição |
    |----------|-----------------------------------|
    | `OBTER` | `cursos` | Lista de cursos e seus dados básicos. |
    | `POSTAR` | `cursos` | Crie um novo curso.                |
    | `OBTER` | `cursos/<acrônimo>` | Informações sobre um curso específico.  |
    | `COLOCAR` | `cursos/<acrônimo>` | Atualize um curso específico.      |
    | `EXCLUIR` | `cursos/<acrônimo>` | Exclua um curso específico.        |
    | `OBTER` | `professores` | Lista de professores.                 |

    então a exclusão de um curso específico, por exemplo, pode ser feita com a URL:```http
    DELETE https://api.ucr.ac.cr/cursos/AB1234
    ```*Pedidos específicos*

    Supondo que cada curso possua a informação do código do curso, poderia ser feita uma solicitação do tipo```http
    GET https://api.ucr.ac.cr/cursos?curso=420201
    ```que retorna uma lista de dois cursos que pertencem ao código do curso 420201 (Engenharia Elétrica).

    ##### Exemplo em um navegador e no terminal de comando

    É possível verificar a temperatura no Cairo com a API [Open-Meteo] (https://open-meteo.com/en/docs),usando a url:```http
    https://api.open-meteo.com/v1/forecast?latitude=30.0571&longitude=31.2272&hourly=temperature_2m
    ```duas maneiras seguintes:

    - No terminal de comando (Unix CLI) com `$curl <URL>`.
    - Na barra de navegação de qualquer navegador, digitar `<URL>` (a informação será de difícil leitura).
    - Com um cliente API de teste on-line, como [ReqBin](https://reqbin.com/).Como fazer isso programaticamente com Python será estudado mais tarde.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ## 6.2. Formatos de troca de dados

    > Como é enviada a informação de uma requisição, considerando que entre clientes e servidores existe uma grande heterogeneidade de linguagens de programação, sistemas operacionais, linguagens, etc.?

    Para isso existem vários formatos comuns, incluindo **JSON** e **CSV**, que são os mais usados ​​e quase *de fato*. Mas também é possível usar **XML** (*Extensible Markup Language*), **XLSX** (*MS Office Excel*), **ODS** (*Planilha OpenDocument*), **HDF** (*Formato de dados hierárquicos*), **SHP** (*ESRI Shapefile* para dados espaciais em sistemas de informação geográfica) e até mesmo **DataFrame** do Pandas.

    ### 6.2.1. JSON

    A grande maioria das APIs oferece JSON como um dos formatos de download.

    > "JavaScript Object Notation" **JSON** (*JavaScript Object Notation*) um formato leve de troca de dados. Ler e escrever é fácil para humanos, enquanto para máquinas é fácil interpretá-lo e gerá-lo ([JSON.org](https://www.json.org/json-eh.html)).O formato é [padronizado](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf):**ECMA-404** *O padrão de intercâmbio de dados JSON*.

    #### Como criar um objeto

    <img src="https://www.json.org/img/object.png"largura="450">

    ##### Exemplos de objetos JSON

    - Em branco```json
    { }
    ```- Um par chave/valor```json
    { "nombre" : "Modelos Probabilísticos de Sinais y Sistemas" }
    ```- Um conjunto de pares chave/valor```json
    {
        "nombre" : "Modelos Probabilísticos de Sinais y Sistemas",
        "sigla" : "IE0405",
        "creditos" : 3,
        "curso" : 420201
    }
    ```#### Como criar uma matriz

    <img src="https://www.json.org/img/array.png"largura="450">

    O valor (*valor*) pode ser uma string com aspas duplas, ou um número, ou `true` ou `false` ou `null`, ou um objeto ou uma matriz. Essas estruturas podem ser aninhadas ([JSON.org](https://www.json.org/json-eh.html)).##### exemplos de matriz JSON

    - Um conjunto de objetos aninhados```json
    [
        {
            "nombre" : "Modelos Probabilísticos de Sinais y Sistemas",
            "sigla" : "IE0405",
            "creditos" : 3,
            "curso" : 420201,
            "topicos" : {
                "topico_1" : "Introducao a la probabilidade",
                "topico_2" : "Variables aleatorias",
                "topico_3" : "Variables aleatorias múltiples",
                "topico_4" : "Procesos aleatorios",
                "topico_5" : "Cadenas de Markov"
            },
            "obrigatorio" : true,
            "laboratorio" : false
        },
        {
            "nombre" : "Circuitos Lineales I",
            "sigla" : "IE0309",
            "creditos" : 3,
            "curso" : 420201,
            "topicos" : {
                "topico_1" : "Introducao",
                "topico_2" : "Análisis de circuitos resistivos",
                "topico_3" : "Técnicas para o analise dos circuitos lineales",
                "topico_4" : "Elementos almacenadores de energía",
                "topico_5" : "El circuito de primer orden",
                "topico_6" : "El circuito de segundo orden"
            },
            "obrigatorio" : true,
            "laboratorio" : false
        }
    ]
    ```#### biblioteca `json`

    Python fornece ferramentas para manipular estruturas de dados e convertê-las de ou para JSON. O formato do JSON é semelhante ao de um dicionário Python (um recurso de sintaxe que ele compartilha com o JavaScript).""")
    return


@app.cell
def _():
    import json

    _d = {"título": "Don Quijote de La Mancha", "autor": "Miguel de Cervantes"}
    # Crear um diccionario de Python
    _j = json.dumps(_d)
    # Convertir a JSON
    print(_j)
    return (json,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Observe que os acentos são transformados e as aspas simples tornam-se aspas duplas.

    **Observação**: Existem páginas para formatar textos JSON, como [JSON Formatter](https://jsonformatter.curiousconcept.com/).Também é possível converter um JSON na forma de *string* para um objeto Python""")
    return


@app.cell
def _(json):
    _j = '{ "sigla" : "IE0405" }'
    _d = json.loads(_j)
    print(type(_d))
    print(_d)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Observe a mudança nas convenções para aspas e espaços em torno de `:`, `{` e `}`.

    Para inserir *strings* de múltiplas linhas com `'''`, faça:""")
    return


@app.cell
def _(json):
    _j = '\n    { \n        "nombre" : "Modelos Probabilísticos de Sinais y Sistemas",\n        "sigla" : "IE0405",\n        "creditos" : 3,\n        "curso" : 420201\n    }\n\n'
    _d = json.loads(_j)
    print(type(_d))
    print(_d)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Como extrair informações do JSON

    Como um arquivo JSON pode ter estruturas de dados complexas, a indexação para solicitar dados merece cuidado especial.

    ##### Exemplo de dois cursos ministrados pela UCR

    Neste exemplo, o JSON possui um array com dois objetos: `[ { }, { } ]`, e cada objeto por sua vez possui outros objetos e arrays aninhados. Para extrair, por exemplo, o `"topic_2"` do curso Circuitos Lineares preciso fazer:""")
    return


@app.cell
def _(json):
    _cursos = '\n    [\n        { \n            "nombre" : "Modelos Probabilísticos de Sinais y Sistemas",\n            "sigla" : "IE0405",\n            "creditos" : 3,\n            "curso" : 420201,\n            "topicos" : {\n                "topico_1" : "Introducao a la probabilidade",\n                "topico_2" : "Variables aleatorias",\n                "topico_3" : "Variables aleatorias múltiples",\n                "topico_4" : "Procesos aleatorios",\n                "topico_5" : "Cadenas de Markov"\n            },\n            "obrigatorio" : true,\n            "laboratorio" : false\n        },\n        { \n            "nombre" : "Circuitos Lineales I",\n            "sigla" : "IE0309",\n            "creditos" : 3,\n            "curso" : 420201,\n            "topicos" : {\n                "topico_1" : "Introducao",\n                "topico_2" : "Análisis de circuitos resistivos",\n                "topico_3" : "Técnicas para o analise dos circuitos lineales",\n                "topico_4" : "Elementos almacenadores de energía",\n                "topico_5" : "El circuito de primer orden",\n                "topico_6" : "El circuito de segundo orden"\n            },\n            "obrigatorio" : true,\n            "laboratorio" : false\n        }\n    ]\n'
    _a = json.loads(_cursos)
    _q = _a[1]["topicos"]["topico_2"]
    print(type(_a))
    print("Tema:", _q)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""onde `[1]` refere-se ao segundo objeto (Circuitos Lineares I) e `['topicos']` e `['topico_2']` são os índices ou "chaves" nos pares chave/valor pesquisados.

    É possível modificar um pouco o JSON para tornar a busca mais intuitiva, criando dois objetos identificados pela sigla do curso, para que a requisição agora seja, por exemplo:```python
    a['IE0405']['topicos']['topico_3']
    ```
    """)
    return


@app.cell
def _(json):
    _cursos = '\n    {\n        "IE0405" : { \n            "nombre" : "Modelos Probabilísticos de Sinais y Sistemas",\n            "creditos" : 3,\n            "curso" : 420201,\n            "topicos" : {\n                "topico_1" : "Introducao a la probabilidade",\n                "topico_2" : "Variables aleatorias",\n                "topico_3" : "Variables aleatorias múltiples",\n                "topico_4" : "Procesos aleatorios",\n                "topico_5" : "Cadenas de Markov"\n            },\n            "obrigatorio" : true,\n            "laboratorio" : false\n        },\n        "IE0309" : { \n            "nombre" : "Circuitos Lineales I",\n            "sigla" : "IE0309",\n            "creditos" : 3,\n            "curso" : 420201,\n            "topicos" : {\n                "topico_1" : "Introducao",\n                "topico_2" : "Análisis de circuitos resistivos",\n                "topico_3" : "Técnicas para o analise dos circuitos lineales",\n                "topico_4" : "Elementos almacenadores de energía",\n                "topico_5" : "El circuito de primer orden",\n                "topico_6" : "El circuito de segundo orden"\n            },\n            "obrigatorio" : true,\n            "laboratorio" : false\n        }\n    }\n'
    _a = json.loads(_cursos)
    _q = _a["IE0405"]["topicos"]["topico_3"]
    print("Tema:", _q)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 6.2.2. CSV

    Outro formato popular para troca de dados é **CSV** ou Valores Separados por Vírgula*. Isto representa uma tabela com colunas e registros e é escrito da forma mais compacta possível:

    - Cada coluna é separada por vírgula ou tabulação.
    - Cada registro é separado por uma nova linha.

    ##### Exemplo de informações do curso

    *Como mesa*

    |curso |sigla |créditos|curso|
    |--------------------------------------------|------|--------|-------|
    |Modelos Probabilísticos de Sinais e Sistemas|IE0405|3 |420201 |
    |Circuitos Lineares I |IE0309|3 |420201 |
    |Análise de Sistemas |IE0409|3 |420201 |

    *Como CSV*```
    curso,sigla,creditos,curso
    Modelos Probabilísticos de Sinais y Sistemas,IE0405,3,420201
    Circuitos Lineales I,IE0309,3,420201
    Análisis de Sistemas,IE0409,3,420201
    ```**Nota 1**: Não é possível “aninhar” tabelas dentro de outras, ressaltando que elas devem ser planas. CSV, portanto, não permite estruturas de dados tão complexas quanto JSON.

    **Observação 2**: Quando uma coluna inclui uma vírgula, aspas são usadas em todo o conteúdo, por exemplo:```
    curso,sigla,creditos,curso
    "Cultura, Sociedad y Economía",CS0605,3,254986
    "Spinoza, Descartes y los Racionalistas",VM0339,3,302145
    ```**Nota 3**: Editores de planilhas como Microsoft Excel, Google Spreadsheets ou LibreOffice Calc permitem a edição e exportação em CSV mas, por sua natureza, sem qualquer tipo de formatação ou fórmulas, apenas os valores.

    #### biblioteca `csv`

    Python também possui ferramentas padrão para criar ou ler arquivos CSV.""")
    return


@app.cell
def _():
    import csv
    from os.path import getmtime
    import time

    _lista = [
        ["curso", "sigla", "creditos", "curso"],
        ["Modelos Probabilísticos de Sinais y Sistemas", "IE0405", 3, 420201],
        ["Circuitos Lineales I", "IE0309", 3, 420201],
        ["Análisis de Sistemas", "IE0409", 3, 420201],
    ]
    # Crear lista com los dados de cursos
    with open("arquivo.csv", "w", newline="") as CSV:
        w = csv.writer(CSV)
        for _i in _lista:
            w.writerow(_i)
    _lapso = time.time() - getmtime("arquivo.csv")
    # Crear "arquivo.csv" y escribir cada uma das líneas da lista
    # Prueba de criacao de arquivo
    print("Archivo foi criado hace {} segundos.".format(_lapso))
    return getmtime, time


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Manipulação de CSV com Pandas

    Geralmente será preferível utilizar Pandas para gerir estes documentos, devido à simplicidade e versatilidade dos seus métodos. Para fazer o mesmo que no caso anterior:""")
    return


@app.cell
def _(getmtime, time):
    import pandas as pd

    _lista = [
        ["curso", "sigla", "creditos", "curso"],
        ["Modelos Probabilísticos de Sinais y Sistemas", "IE0405", 3, 420201],
        ["Circuitos Lineales I", "IE0309", 3, 420201],
        ["Análisis de Sistemas", "IE0409", 3, 420201],
    ]
    # Crear lista com los dados de cursos
    df = pd.DataFrame(_lista)
    df.to_csv("pandas.csv", index=False)
    _lapso = time.time() - getmtime("pandas.csv")
    # Convertir en DataFrame de Pandas
    # Crear arquivo "pandas.csv" desde el DataFrame
    # Prueba de criacao de arquivo
    print("Archivo foi criado hace {} segundos.".format(_lapso))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ## 6.3 - biblioteca `requests`

    Esta é a ferramenta Python mais popular para gerenciamento de API. Não é padrão, mas, de acordo com sua documentação,

    > ...o módulo `urllib2` encontrado no padrão Python oferece a maior parte das funcionalidades necessárias para HTTP, mas sua API está completamente quebrada. Foi construído para outra época – e para um site diferente. Requer muito trabalho (incluindo a reimplementação de métodos) para executar as tarefas mais simples. As coisas não deveriam ser assim. Não em Python.

    **Nota 1**: A documentação oficial `requests` está em [https://docs.python-requests.org/](https://docs.python-requests.org/eh/latest/).**Nota 2**: É necessário verificar a presença da biblioteca `requests` com `$ pip list` e instalar com `$ pip install requests` se ela não estiver lá.

    ##### Exemplo de dados de usuário no GitHub

    GitHub disponibiliza uma API com informações aos usuários. Pode ser usado aqui para demonstrar algumas ações típicas.""")
    return


@app.cell
def _():
    import requests

    usuario = "fabianabarca"
    # Usuario(a) de GitHub
    api_url = "https://api.github.com/users/" + usuario
    _r = requests.get(api_url)
    # Construir la URL
    dados = _r.json()
    # Hacer la solicitacao GET y guardar um "Response" en la variable r
    # Convertir la informacao obtenida en JSON
    # Extraer y mostrar algún dato particular com la llave "company"
    print("Compañía:", dados["company"])
    return (requests,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Para ver todas as informações obtidas, basta fazer```python
    info.json()
    ```Outros dados disponíveis neste objeto de resposta são: “login”, “url”, “nome”, “bio”, de um total de 32.

    ### 6.3.1. *Esquemas* e parâmetros de solicitação (*consultas*)

    > Ao receber uma resposta de uma determinada API, como sabemos quais categorias estão presentes, como no caso anterior com “login”, “url”, “nome”, “bio”, “empresa” e outras?

    É necessário consultar a documentação da API, que geralmente traz um resumo de suas informações.

    A estrutura de uma base de dados pode ser formalmente descrita por um *esquema*, que é uma espécie de mapa com dois dados incluídos.

    Por exemplo, no caso hipotético da API UCR, os seguintes campos (*fields*) são definidos no *endpoint* `courses`:

    - "nome"
    - "acrônimo"
    - "créditos"
    - "curso"
    - "tópicos"
    - "obrigatório"
    - “laboratório”.

    É importante saber essas informações com antecedência para saber o que encontrar e como extrair dados específicos da resposta da API.

    #### Solicitações de submontagem

    Da mesma forma, as APIs estabelecem regras para a seleção de **subconjuntos** (*subsets*) de seus dados, classificados de acordo com um ou vários parâmetros, por exemplo, segundo `course=420201`, conforme visto. É preciso saber em quais pode ser classificado, pois não são todos, isso depende de cada API. Essas solicitações ou *consultas* possuem sintaxe como no exemplo:```http
    GET https://api.ucr.ac.cr/cursos?curso=420201&laboratorio=true
    ```que retorna os cursos que são cursos de Engenharia Elétrica **e** que são cursos de laboratório.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 6.4 *Observatório Urbano* Dados

    A imensa quantidade de dados disponíveis no Observatório Urbano da Universidade de Newcastle pode ser acessada com sua [API](https://newcastle.urbanobservatory.ac.uk/api_docs/).As informações foram extraídas em diversos formatos: JSON, CSV, XLSX e outros. Existem as seguintes categorias, ou *endpoints*:

    - O URL base:```http
    http://uoweb3.ncl.ac.uk/api/v1.1/
    ```| *Ponto final* | Descrição |
    |----------------------------------|----------------------------------|
    | `sensores` | Lista de sensores |
    | `sensores/tipos` | Tipos de sensores |
    | `sensores/dados` | Dados de sensor bruto |
    | `sensores/{nome_do_sensor}` | Sensores individuais |
    | `sensores/{nome_do_sensor}/dados` | Dados dois sensores individuais |
    | `variáveis` | Nomes das variáveis ​​medidas |
    | `temas` | Classificação temática |

    Assim, por exemplo, para obter a lista com a classificação temática (***temas***) de dois sensores utilizados, é necessária a URL onde esta informação está localizada, seguida da especificação do formato desejado:```http
    GET http://uoweb3.ncl.ac.uk/api/v1.1/themes/json/
    ```Implementado com `requests` isto, huh:""")
    return


@app.cell
def _(requests):
    api_url_1 = "http://uoweb3.ncl.ac.uk/api/v1.1/themes/json/"
    _r = requests.get(api_url_1)
    _r.json()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##### Exemplo de solicitação de variáveis por tópico

    Como visto anteriormente, é possível fazer solicitações específicas de categorias modificando a URL. Por exemplo, em ***variáveis***, estes são os dados incluídos (seu *esquema*):```json
    {
        'Upper Limit': [],
        'Lower Limit': [],
        'Units': [],
        'Name': [],
        'Theme': []
    }
    ```Você pode então solicitar uma resposta apenas com as variáveis ​​dentro do tema `Soil`, por exemplo. Para fazer isso, você deve modificar a URL da solicitação com os parâmetros específicos:```http
    GET http://uoweb3.ncl.ac.uk/api/v1.1/variables/json/?theme=Soil
    ```Em Python, isso pode ser feito assim:""")
    return


@app.cell
def _(requests):
    api_url_2 = "http://uoweb3.ncl.ac.uk/api/v1.1/variables/json/?theme=Soil"
    _r = requests.get(api_url_2)
    _r.json()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Que subconjuntos podemos obter?

    No exemplo anterior, os resultados foram obtidos a partir de ***variáveis*** classificadas por ***tema***.

    > Cada API define quais subconjuntos podem ser obtidos nas solicitações. Por exemplo, no Observatório Urbano você pode classificar suas ***variáveis*** apenas de acordo com o ***tema***. Por outro lado, ***sensores*** (dos quais existem milhares) podem ser classificados por ***sensor_type***, ***theme*** e outros, ou uma combinação deles.

    Com `requests` é possível solicitar informações criando um dicionário de parâmetros, o que simplifica a construção da URL.

    ##### Exemplo de seleção de sensor

    Para a seleção dos sensores, a API define os seguintes campos:

    - `tipo_de_sensor`
    - `tema`
    - `corretor`
    - `polígono_wkb`
    - coordenar o retângulo dentro dos dias em que o sensor está
    - região (código postal).

    O exemplo a seguir solicita o tópico **velocidade do vento**, **qualidade do ar** e sensores do fabricante **Sensor AURN**.""")
    return


@app.cell
def _(requests):
    api_url_3 = "http://uoweb3.ncl.ac.uk/api/v1.1/sensors/json/"
    _parametros = {
        "sensor_type": "Wind Speed",
        "theme": "Air Quality",
        "broker": "AURN Sensor",
    }
    _r = requests.get(api_url_3, _parametros)
    print("La URL consultada eh:\n{}".format(_r.url))
    _r.json()
    return (api_url_3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Agora você pode fazer uma nova busca por sensores de **velocidade do vento**, referentes à **qualidade do ar** e que estejam **dentro de um retângulo de coordenadas** de latitude e longitude (nas proximidades de Newcastle upon Tyne, Inglaterra)."""
    )
    return


@app.cell
def _(api_url_3, requests):
    import pprint

    _parametros = {
        "sensor_type": "Wind Speed",
        "theme": "Air Quality",
        "bbox_p1_x": -1.62,
        "bbox_p1_y": 54.9,
        "bbox_p2_x": -1.61,
        "bbox_p2_y": 55.1,
    }
    _r = requests.get(api_url_3, _parametros)
    print("La URL consultada eh:\n{}\n".format(_r.url))
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(_r.json())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 6.5. APIs bônus

    Alguns pedidos de dados.""")
    return


@app.cell
def _(requests):
    _r = requests.get("https://api.chucknorris.io/jokes/random")
    joke = _r.json()["value"]
    print("----\nJoke\n----")
    print(joke + "\n")
    word = "random"
    _r = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
    definition = _r.json()
    print("----------\nDefinition\n----------")
    print(
        "{}: {}\n".format(
            word, definition[0]["meanings"][0]["definitions"][0]["definition"]
        )
    )
    api_key = "095Vm6CuWfIGTCfhYyoo4ibDhZGg2Ge6"
    api_url_4 = "https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key="
    _r = requests.get(api_url_4 + api_key)
    news = _r.json()
    num_results = news["num_results"]
    print("----\nNews\n----")
    for _i in range(num_results):
        print("- ", news["results"][_i]["title"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Para uma piada de um terminal Unix (possivelmente você terá que instalar `jq`, um processador JSON na linha de comando):```bash
    curl -s https://api.chucknorris.io/jokes/random | jq -C '.value'
    ```ou então```bash
    curl -H "Accept: text/plain" https://icanhazdadjoke.com/
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---
    ###Mais informações

    - [`solicitações`]( documentaçãohttps://docs.python-requests.org/eh/latest/)- [Observatório Urbano](https://newcastle.urbanobservatory.ac.uk/)- Ferramenta de teste de API [ReqBin](https://reqbin.com/)
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
