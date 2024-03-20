# SocketSpeak

O SocketSpeak é uma aplicação simples de chat baseada em sockets em Python, projetada para demonstrar os conceitos fundamentais de comunicação cliente-servidor. Ele permite que clientes se conectem a um servidor para visualizar informações de fuso horário de diferentes cidades.

## Funcionalidades:

-   Estabelece uma conexão TCP entre cliente e servidor.
-   Permite que o cliente escolha uma opção para visualizar o fuso horário de cidades específicas.
-   Utiliza a API WorldTimeAPI para obter informações de fuso horário em tempo real.

## Como Executar:

Para executar o SocketSpeak, siga as etapas abaixo:

1. Certifique-se de que o Python esteja instalado em seu sistema.

2. Clone o repositório do SocketSpeak para o seu ambiente de desenvolvimento.

3. Crie um ambiente virtual Python usando o comando:

-   python3 -m venv env

4. Ative o ambiente virtual:

-   No Windows:
    ```
    env\Scripts\activate
    ```
-   No macOS/Linux:
    ```
    source env/bin/activate
    ```

5. Instale as dependências necessárias usando o arquivo `requirements.txt`:

    ```
    pip install -r requirements.txt
    ```

6. Inicie o servidor executando o seguinte comando:

```
    python3 server.py
```

7. Em outra janela do terminal, inicie o cliente executando:

    ```
    python3 client.py
    ```

8. Siga as instruções no cliente para escolher uma opção de cidade e visualizar o fuso horário correspondente.

Com essas etapas, você será capaz de iniciar o servidor e o cliente do SocketSpeak e realizar a comunicação entre eles. Divirta-se explorando as funcionalidades simples, porém educativas, deste projeto de sockets em Python!
