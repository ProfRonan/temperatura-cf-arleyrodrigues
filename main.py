"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    c = float(input("Quala temperatura em graus Celsius?\n"))
    j = c *9/5 + 32
    print(f'A temperatura em Fahrenheit é {j}')


if __name__ == '__main__':
    main()
