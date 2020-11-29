from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
from multiprocessing import Queue, Process
from os import devnull, system
from subprocess import check_call
from time import sleep

class Rede:
    def __init__(self):
        self.meuIP = '' #vai ser preenchido por obterMeuIP() no construtor
        self.hostsAtivos = [] #vai ser preenchido por obterHostsAtivos() no construtor
        self.portasAbertas = []#só vai ser preenchido se chamar varrerportas()
        self.obterMeuIP()#obtem IP
        self.obterHostsAtivos()#Obtem hosts ativos

    def obterMeuIP(self):
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        meuIP = sock.getsockname()[0]
        sock.close()
        self.meuIP = meuIP
    
    def baseIP(self):
        ipPart = self.meuIP.split('.')
        baseIP = ipPart[0] + '.' + ipPart[1] + '.' + ipPart[2] + '.'
        return baseIP

    def ping(self, tarefas, resultados):
        DEVNULL = open(devnull, 'w')
        while True:
            ip = tarefas.get()
            if ip is None:
                break
            try:
                check_call(['ping', '-c1', ip], stdout=DEVNULL)
                resultados.put(ip)
            except:
                pass

    def obterHostsAtivos(self, poolSize=255):
        baseIP = self.baseIP()
        tarefas = Queue()
        resultados = Queue()
        pool = [Process(target=self.ping, 
        args=(tarefas, resultados)) for i in range(poolSize)]
        for p in pool:
            p.start()
        for i in range(1, 255):
            tarefas.put(baseIP + '{0}'.format(i))
        for p in pool:
            tarefas.put(None)
        for p in pool:
            p.join()
        while not resultados.empty():
            ip = resultados.get()
            self.hostsAtivos.append(ip)

    def varrerPortas(self):
        try:
            print("\nDigite o intervalo de portas que vai ser coberto na varredura:")
            portaInicial = int(input("Porta Inicial: "))
            portaFinal = int(input("Porta Final: "))
            if(portaInicial > portaFinal or portaInicial < 0 or portaFinal > 65535):
                raise Exception
            system('clear')
        except:
            print('Erro! Verifique e tente novamente!')
            exit()
        for ip in self.hostsAtivos:
            try:
                portasAbertas = []
                for porta in range(portaInicial, portaFinal+1):
                    print("Varrendo o host: %s" %(ip))
                    print("Verificando porta: %d" %(porta))
                    sock = socket(AF_INET, SOCK_STREAM)
                    res = sock.connect_ex((ip,  porta))
                    system('clear')
                if (res == 0):
                    print("%d" %(porta))
                    portasAbertas.append(porta)
            except:
                print('Erro! Verifique e tente novamente')
                exit()
            print("Varredura encerrada no host: %s" %(ip))
            print("%d porta(s) aberta(s)" %(len(portasAbertas)))
            self.portasAbertas.append(portasAbertas)
            sleep(3)
            system('clear')
        self.mostrarPortasAbertas(portaInicial, portaFinal)

    def mostrarHostsAtivos(self):
        i=1
        print("Os seguintes hosts estão ativos na sua rede: ")
        for ip in self.hostsAtivos:
            print("%d -> %s" %(i,ip))
            i+=1
    
    def mostrarPortasAbertas(self, portaInicial, portaFinal):
        system('clear')
        print("Relatorio de Portas Abertas: ")
        print("Numéro de Portas Abertas no Intervalo %d - %d" %(portaInicial, portaFinal))
        print(" |      HOST           |    PORTAS ABERTAS |")
        i=0
        for ip in self.hostsAtivos:
            sizePortas = len(self.portasAbertas[i])  
            print(" | %s       |          %d        | " %(ip,sizePortas))
            i+=1
        i=0
        for ip in self.hostsAtivos:
            if( len(self.portasAbertas[i]) > 0):
                print("\nLista de Portas Abertas do host: %s"%(ip))
                for porta in self.portasAbertas[i]:
                    print(porta)
                print("\n")
            i+=1





    