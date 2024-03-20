import socket
import time


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(("localhost", 8082))
        data_payload = 1024
        message = input("Tudo Ok?: ")
        sock.sendall(message.encode("utf-8"))
        while True:
            data = sock.recv(data_payload)
            if data:
                print(data.decode("utf-8"))
                response = input("Resposta: ")  # Solicita a entrada do usuário após receber as opções
                if response.lower() == 'sair':  # Se o usuário digitar 'sair', quebre o loop
                    break
                sock.sendall(response.encode("utf-8"))  # Envia a resposta do usuário para o servidor
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        sock.close()  # Remove o time.sleep(10) para fechar imediatamente após o loop

if __name__ == "__main__":
    client()