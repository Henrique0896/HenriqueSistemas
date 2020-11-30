
from Rede import Rede
from Varredura import VarreduraPortas
from os import system

if __name__ == '__main__':
    system('clear')
    print("Analisando sua Rede...")
    minhaRede = Rede()
    system('clear')

    hosts = minhaRede.mostrarHostsAtivos()

    #print(hosts)

#hosts = ['172.217.162.142']

h = VarreduraPortas(hosts)
h.varrerPortas()
