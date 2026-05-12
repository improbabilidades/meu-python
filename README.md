# Meu Python

Esse é um repositório de estudo de Python, com notebooks executaveis e exemplos práticos.

Professora Elizabet Medeiros

## Instalação do Python e o gerenciador de pacotes uv

Para instalar o Python, pode seguir primeiro as [instruções de instalação de **uv**](https://docs.astral.sh/uv/getting-started/installation/) para seu sistema operacional.

Depois da instalação do **uv**, basta rodar o comando abaixo para instalar o Python:

```bash
uv python install
```

## Instalação de Marimo para rodar os notebooks

Para rodar os notebooks, é necessário instalar [marimo](https://marimo.io/). Tem duas formas de instalar o marimo:

- Globalmente: accessível em qualquer lugar do sistema,

```bash
uv tool install marimo
```

- Localmente: acessível apenas dentro do projeto, recomendado para evitar conflitos de versões entre projetos diferentes.

```bash
uv add marimo
```

ou, para instalar também as dependências recomendadas para notebooks:

```bash
uv add "marimo[recommended]"
```

## Para clonar este repositório

A recomendacão é usar a ferramenta de linha de comando [GitHub CLI](https://cli.github.com/), o `gh`. Primeiro, instale o `gh` seguindo as [instruções de instalação](https://github.com/cli/cli#installation) para seu sistema operacional. Isso aqui vai instalar o Git, que é a ferramenta de controle de versão usada para clonar o repositório.

Depois de instalar o `gh`, faça login na sua conta do GitHub usando o comando:

```bash
gh auth login
```

Agora, navegue até a pasta onde deseja clonar o repositório e use o comando:

```bash
gh repo clone improbabilidades/meu-python
```

Isso vai criar uma pasta chamada `meu-python` com todo o conteúdo do repositório. Navegue até essa pasta usando o comando:

```bash
cd meu-python
```

## Rodando os notebooks

Para rodar os notebooks desde a terminal de comandos, deve primeiro navegar até a pasta do projeto (ver comandos básicos de terminal em baixo) e depois rodar o comando:

```bash
uv run marimo edit Py0.py
```

ou, se tiver instalado o marimo globalmente:

```bash
marimo edit Py0.py
```

## Comandos básicos de terminal

- `ls` ou `dir`: lista os arquivos e pastas no diretório atual.
- `cd nome_da_pasta`: muda para a pasta especificada.
- `cd ..`: sobe um nível na hierarquia de pastas.
- `pwd`: mostra o caminho completo do diretório atual.
- `mkdir nome_da_pasta`: cria uma nova pasta com o nome especificado.
- `rm nome_do_arquivo`: remove o arquivo especificado.
- `rm -r nome_da_pasta`: remove a pasta e todo o seu conteúdo (cuidado com esse comando!).
- `clear`: limpa a tela do terminal.
