import socket

HOST = '192.168.1.100'  # The server's hostname or IP address
PORT = 5000  # The port used by the server


def read_chunks(conn):
    # Set the chunk size to be the same as the one used by the client
    chunk_size = 1024

    # Read the data in chunks until all data is received
    data = b''
    while True:
        chunk = conn.recv(chunk_size)
        if not chunk:
            break
        data += chunk

    return data


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Read the data sent by the client in chunks
    binary_data = read_chunks(s)

    # Do something with the data
    # ...
    with open('destination/Unknown Brain - Why Do I_ (feat. Bri Tolani) _NCS Release_ ( 256kbps cbr ).mp3', 'wb') as file:
        file.write(binary_data)
