
from Rede import Rede
from os import system

if __name__ == '__main__':
    system('clear')
    print("Analisando sua Rede...")
    minhaRede = Rede()
    system('clear')

    minhaRede.mostrarHostsAtivos()

    minhaRede.varrerPortas()
