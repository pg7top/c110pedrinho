import random

def desenhar_dado(numero):
    """
    Esta função recebe um número entre 1 e 6 e retorna uma representação visual de um dado em ASCII.
    """
    if numero == 1:
        dado_ascii = [
            "+-------+",
            "|       |",
            "|   0   |",
            "|       |",
            "+-------+"
        ]
    elif numero == 2:
        dado_ascii = [
            "+-------+",
            "| 0     |",
            "|       |",
            "|     0 |",
            "+-------+"
        ]
    elif numero == 3:
        dado_ascii = [
            "+-------+",
            "| 0     |",
            "|   0   |",
            "|     0 |",
            "+-------+"
        ]
    elif numero == 4:
        dado_ascii = [
            "+-------+",
            "| 0   0 |",
            "|       |",
            "| 0   0 |",
            "+-------+"
        ]
    elif numero == 5:
        dado_ascii = [
            "+-------+",
            "| 0   0 |",
            "|   0   |",
            "| 0   0 |",
            "+-------+"
        ]
    elif numero == 6:
        dado_ascii = [
            "+-------+",
            "| 0 0 0 |",
            "|       |",
            "| 0 0 0 |",
            "+-------+"
        ]
    else:
        dado_ascii = [
            "Número inválido",
            "+-------+",
            "|       |",
            "|   X   |",
            "|       |",
            "+-------+"
        ]
    
    return "\n".join(dado_ascii)

while True:
    response = input("Bora jogar o dado meu consagrado? (y/n): ").lower()
    
    if response != 'y':
        if response == 'n':
            print("Obrigado por jogar meu bom! Até depois!")
        else:
            print("Opção inválida meu mano, escolhe n ou y que ai vai dar bom.")
        break
    
    numero = random.randint(1, 6)
    print(desenhar_dado(numero))