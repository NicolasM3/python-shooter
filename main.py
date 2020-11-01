from game import game
from player import Player
import socket
import threading
import time
import pickle
import errno
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

def server_sender():
    while True:
        player = game.get_player()
        player = pickle.dumps(player.as_dict())

        client_socket.send(player)  

        time.sleep(10)

def server_reciver():
     while True:
        try:
            while True:
                dump_message = client_socket.recv(1234)
                message = pickle.loads(dump_message)

                print(message)

                if not len(username_header):
                    print('Connection closed by the server')
                    sys.exit()

                print(username_header)

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()
                
            continue

        except Exception as e:
            # Any other exception - something happened, exit
            print('Reading error: '.format(str(e)))
            sys.exit()


if __name__ == "__main__":
    server_communication = threading.Thread(target= server_sender)
    server_reciver = threading.Thread(target=server_reciver)
    game_thread = threading.Thread(target= game.run)

    server_communication.start()
    game_thread.start()
    server_reciver.start()
