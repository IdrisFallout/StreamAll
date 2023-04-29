import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.1.100'
port = 5000

client_socket.bind((host, port))


def make_request(message, conn):
    conn.sendall(message)
    print(message)


def parse_data():
    client_socket.listen(1)
    conn, addr = client_socket.accept()
    print("Connected by", addr)

    with open('source/Unknown Brain - Why Do I_ (feat. Bri Tolani) _NCS Release_ ( 256kbps cbr ).mp3', 'rb') as file:
        binary_data = file.read()
    # divide the data into chunks
    chunk_size = 1024
    chunks = [binary_data[i:i + chunk_size] for i in range(0, len(binary_data), chunk_size)]
    for chunk in chunks:
        make_request(chunk, conn)


parse_data()
