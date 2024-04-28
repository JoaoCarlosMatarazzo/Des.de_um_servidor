import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!")

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = 'Servidor: Olá usuario, bom dia!'

while True:
    dados, end = s.recvfrom(4096)
    if dados:
        print('Servidor enviando mensagem!')
        s.sendto(dados + mensagem.encode(), end)
