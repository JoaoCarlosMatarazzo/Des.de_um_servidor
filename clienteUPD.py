import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente criado com sucesso!")
host = 'localhost'
porta = 5433
mensagem = ' Bem-vindo ao servidor!'
try:
    print('Cliente'+mensagem)
    s.sendto(mensagem.encode(),(host, 5432))

    dados, servidor=s.recvfrom(4096)
    dados = dados.decode()
    println("Cliente:"+dados)
finally:
    print("Cliente: Finalizando conexão!")
    s.close()


























