# Agenda de Contatos em Python

Aplicação de terminal desenvolvida como desafio do módulo **Introdução ao Python** da Rocketseat.

O programa permite cadastrar, visualizar, editar e apagar contatos, além de marcar ou desmarcar contatos como favoritos.

## Funcionalidades

- adicionar um contato com nome, telefone e e-mail;
- listar todos os contatos cadastrados;
- editar um contato existente;
- marcar e desmarcar um contato como favorito;
- listar somente os contatos favoritos;
- apagar um contato;
- validar opções e números de contatos inválidos.

## Requisitos

Para executar o projeto, é necessário ter instalado:

- [Python](https://www.python.org/downloads/) 3.10 ou superior;
- um terminal, como PowerShell, Prompt de Comando ou Git Bash.

O projeto utiliza apenas recursos nativos do Python. Portanto, não é necessário instalar bibliotecas ou executar `pip install`.

## Programas recomendados

- [Visual Studio Code](https://code.visualstudio.com/): editor usado para abrir e editar o projeto;
- [Git](https://git-scm.com/downloads): necessário somente para clonar o repositório ou enviar alterações ao GitHub.

O Visual Studio Code e o Git são recomendados, mas não são obrigatórios para executar o programa.

## Extensões recomendadas para o VS Code

Abra a aba de extensões do VS Code com `Ctrl + Shift + X` e procure por:

- **Python**, publicada pela Microsoft (`ms-python.python`);
- **Pylance**, publicada pela Microsoft (`ms-python.vscode-pylance`);
- **Python Debugger**, publicada pela Microsoft (`ms-python.debugpy`).

A extensão **Python** permite selecionar o interpretador e executar o arquivo pelo VS Code. Pylance e Python Debugger auxiliam na escrita e depuração, mas não são necessários para executar pelo terminal.

## Como baixar o projeto

Com o Git instalado, execute:

```bash
git clone https://github.com/MarioCarlaibe/Agenda-de-Contatos-Python.git
cd Agenda-de-Contatos-Python
```

Também é possível baixar o projeto pelo botão **Code > Download ZIP** no GitHub e extrair o arquivo em uma pasta de sua preferência.

## Como verificar a instalação do Python

Abra um terminal e tente um dos comandos abaixo:

```bash
python --version
```

ou, no Windows:

```bash
py --version
```

Se a versão instalada for exibida, o Python está pronto para uso.

## Como executar

No terminal, entre na pasta do projeto e execute:

```bash
python agenda_de_contatos.py
```

Se o comando `python` não estiver disponível no Windows, tente:

```bash
py agenda_de_contatos.py
```

Em uma instalação feita com `uv`, usando o Git Bash, também pode ser necessário executar:

```bash
~/.local/bin/python3.15.exe agenda_de_contatos.py
```

### Execução pelo VS Code

1. Abra a pasta do projeto no VS Code.
2. Abra o arquivo `agenda_de_contatos.py`.
3. Pressione `Ctrl + Shift + P`.
4. Procure por **Python: Select Interpreter** e escolha a versão instalada.
5. Clique no botão de execução no canto superior direito.
6. Escolha **Executar Arquivo do Python**.

## Menu da aplicação

Ao iniciar o programa, será apresentado o seguinte menu:

```text
Agenda de contatos:
1. Adicionar contato
2. Listar contatos
3. Editar contato
4. Marcar/desmarcar contato como favorito
5. Listar contatos favoritos
6. Apagar contato
7. Sair
```

Digite o número da operação desejada e pressione `Enter`.

## Estrutura do projeto

```text
Agenda-de-Contatos-Python/
├── agenda_de_contatos.py
└── README.md
```

## Observação

Os contatos são mantidos em memória enquanto o programa está aberto. Ao encerrar a aplicação, os contatos cadastrados não são salvos, pois persistência em arquivo ou banco de dados não faz parte dos requisitos deste desafio.

## Autor

Desenvolvido por [Mario Carlaibe](https://github.com/MarioCarlaibe) durante os estudos de Python na Rocketseat.
