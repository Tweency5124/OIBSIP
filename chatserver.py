import socket
import threading

def handle_client(client_socket, client_address):
    print(f"[+] New connection from {client_address}")
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{client_address}] {message}")
            broadcast(message, client_socket)
        except:
            break
    
    print(f"[-] Connection closed from {client_address}")
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[+] Server started on {host}:{port}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

clients = []

if __name__ == "__main__":
    host = "127.0.0.1"  # Localhost
    port = 12345        # Port to listen on
    start_server(host, port)
