import os
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.1.100'
port = 5000

client_socket.bind((host, port))


def make_request(file_path, conn):
    filename = os.path.basename(file_path)
    conn.sendall(filename.encode())
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            conn.send(data)
        print("File sent successfully")
    client_socket.close()


def parse_data():
    client_socket.listen(1)
    conn, addr = client_socket.accept()
    print("Connected by", addr)

    make_request('D:\Multimedia\The Lion King (2019) [BluRay] [1080p] [YTS.LT]\The.Lion.King.2019.1080p.BluRay.x264-[YTS.LT].mp4', conn)


parse_data()