import socket
import threading
import requests
API = "https://worldtimeapi.org/api/timezone/america"

OPS = {
    "1": "/Sao_Paulo",
    "2": "/Maceio",
    "3": "/Recife",
    "4": "/Bahia",
    "5": "sair",
}
def client_handler(client_socket, client_address):
    """
    Gerencia a conexão com um cliente.

    Recebe messagens de um cliente e imprime no cosolo do servidor.

    Args:
        client_socket (socket.socket): Socket do cliente.
        client_address (tuple): O endereço do cliente conectado, consistindo em (host, port).
    """

    while True:
        try:
            options = "Escolha uma opção para visualizar o time zone:\n1. Sao_Paulo \n2. Maceio\n3. Recife\n4. Bahia\n".encode('utf-8')
            data_payload = 1024  # Definindo o tamanho máximo do payload
            client_socket.sendall(options)
            message = client_socket.recv(data_payload).decode("utf-8")
            # if message == '5':
            #     client_socket.close()
            #     # Se o usuário escolher sair
            #     break
            if message in OPS:
                api_url = API + OPS[message]
                response = requests.get(api_url)
                if response.status_code == 200:
                    datetime_info = response.json().get('datetime', 'Não disponível')
                    client_socket.sendall(f'Retorno: {datetime_info}\n\n'.encode("utf-8"))
                else:
                    client_socket.sendall("Erro ao acessar a API".encode("utf-8"))
        except:
            break
    client_socket.close()


def chat_server():
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    )  # Criando um socket  ipv4 TCP

    server_host = "localhost"
    server_port = 8082
    server_address = (server_host, server_port)

    server_socket.bind(server_address)  # Associa o socket ao endereço

    server_socket.listen()  # Aguarda por um cliente

    print("Servidor de chat iniciado, aguardando conexões...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexão recebida de {client_socket}")
        client_socket.send("Conectado ao servidor\n".encode("utf-8"))
        threading.Thread(
            target=client_handler, args=(client_socket, client_address)
        ).start()


if __name__ == "__main__":
    chat_server()
