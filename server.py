import socket
import select
import pickle
import time
import threading
import sys
import errno

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()
sockets_list = []

print(f'Listening for connections on {IP}:{PORT}...')

def handler(client):
    while True:
        try:
            while True:
                dump_message = client.recv(1234)
                message = pickle.loads(dump_message)

                print(f'Received message from {client.getpeername()}')

                for client_socket in sockets_list:
                    if client_socket != client:
                        print(client_socket.getpeername())
                        resend_dump_message = pickle.dumps(message)
                        client_socket.send(resend_dump_message)

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()
                
            continue

        except Exception as e:
            # Any other exception - something happened, exit
            print("Reading error: {}".format(str(e)))
            sys.exit()

while True:

    client_socket, client_address = server_socket.accept()
    sockets_list.append(client_socket)

    print('Accepted new connection from {}:{}'.format(client_address[0], client_address[1]))

    client_handler = threading.Thread(target=handler,args=(client_socket,))
    client_handler.start()

    if len(sockets_list)  == 2:
        for i in sockets_list:
            response = {"identifier":"start"}
            dump_response = pickle.dumps(response)
            i.send(dump_response)   

            
            




