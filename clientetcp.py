import socket
import sys

def main():
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    except socket.error as e:
        print("A conexão falhou!")
        print("Erro: {}".format(e))
        sys.exit()
    print("Sucesso!")

    HostAlvo = input("Digite o Host ou Ip a ser conectato: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Conectado com sucesso!")
        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou!")
        print("Favor tentar colocar o Host ou Ip corretamente!")
        print("Erro: {}".format(e))
        sys.exit()
if __name__ == "__main__":
    main()





