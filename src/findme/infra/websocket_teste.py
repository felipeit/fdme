import socket
from typing import NoReturn

def main() -> NoReturn:
    # Configuração do servidor
    HOST = 'localhost'  # Endereço do servidor
    PORT = 1234        # Porta em que o servidor estará escutando

    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associa o socket a uma porta
    server_socket.bind((HOST, PORT))

    # Fica escutando por conexões
    server_socket.listen(5)

    print("Servidor TCP iniciado e escutando em", (HOST, PORT))

    while True:
        # Aceita a conexão
        client_socket, addr = server_socket.accept()
        print('Conexão de', addr)

        # Recebe os dados do cliente
        data = client_socket.recv(1024)
        print('Mensagem recebida:', data)

        # Ecoa a mensagem de volta para o cliente
        client_socket.sendall(data)

        # Fecha a conexão com o cliente
        client_socket.close()

if __name__ == "__main__":
    main()
