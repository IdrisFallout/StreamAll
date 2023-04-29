import socket

server_address = ('192.168.1.100', 5000)
chunk_size = 1024 * 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)


def receive_data():
    filename = client_socket.recv(1024).decode()
    file_path = 'destination/' + filename
    print("(Receiving)")
    count = 0
    with open(file_path, 'wb') as file:
        while True:
            data = client_socket.recv(chunk_size)
            if not data:
                break
            file.write(data)
            count += 1
            print(".", end="")
            if count % 50 == 0:
                print("")


    client_socket.close()
    print("\nFile received successfully")


receive_data()
