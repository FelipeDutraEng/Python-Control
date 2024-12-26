from time import sleep

# Definição de cores
cores = {
    'limpa': '\033[m',
    'azul': '\033[44m',
    'verde': '\033[42m',
    'vermelho': '\033[41m',
    'branco': '\033[7m'
}

def ajuda(comando):
    """
    Exibe o manual de um comando ou biblioteca do Python.
    :param comando: Nome do comando ou biblioteca.
    """
    print(f"{cores['azul']}Acessando o manual do comando '{comando}'...{cores['limpa']}")
    sleep(1)
    print(f"{cores['branco']}", end="")
    help(comando)
    print(f"{cores['limpa']}", end="")

def cabecalho(msg, cor='limpa'):
    """
    Exibe um cabeçalho formatado com cores.
    :param msg: Mensagem a ser exibida.
    :param cor: Cor do cabeçalho.
    """
    print(f"{cores[cor]}{'~' * (len(msg) + 4)}")
    print(f"  {msg}")
    print(f"{'~' * (len(msg) + 4)}{cores['limpa']}")

# Programa principal
while True:
    cabecalho("SISTEMA DE AJUDA PyHELP", "verde")
    comando = input("Função ou Biblioteca > ").strip()
    if comando.upper() == "FIM":
        cabecalho("ATÉ LOGO!", "vermelho")
        break
    else:
        ajuda(comando)