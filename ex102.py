def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    
    :param n: O número cujo fatorial será calculado.
    :param show: (Opcional) Se True, mostra o cálculo na tela.
    :return: O valor do fatorial de n.
    """
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i
        if show:  # Mostra os passos do cálculo
            print(i, end=' x ' if i > 1 else ' = ')
    return resultado


# Programa principal
num = int(input("Digite um número para calcular o fatorial: "))
mostrar = input("Deseja ver o cálculo detalhado? [S/N] ").strip().upper() == 'S'
print(fatorial(num, show=mostrar))
