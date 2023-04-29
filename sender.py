import os
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '0.0.0.0'
port = 5000
chunk_size = 1024 * 1024

client_socket.bind((host, port))


def make_request(file_path, conn):
    filename = os.path.basename(file_path)
    conn.sendall(filename.encode())
    print("(Sending)")
    count = 0
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            conn.send(data)
            count += 1
            print(".", end="")
            if count % 50 == 0:
                print("")

        print("\nFile sent successfully")
    client_socket.close()


def parse_data():
    client_socket.listen(1)
    conn, addr = client_socket.accept()
    print("Connected by", addr)

    make_request(r'D:\Multimedia\Rick.and.Morty.S06 Complete\Rick.and.Morty.S06E09.1080p.x265-ELiTE.mkv', conn)


parse_data()
