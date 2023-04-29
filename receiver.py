import socket

server_address = ('192.168.1.100', 5000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)


def receive_data():
    filename = client_socket.recv(1024).decode()
    file_path = 'destination/' + filename
    print(file_path)
    with open(file_path, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)
            print(data)

    client_socket.close()
    print("File received successfully")


receive_data()
