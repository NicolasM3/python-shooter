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

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.bind((IP, 3000))
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

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

                if(message["identifier"] == "start"):
                    server_communication.start()
                    game_thread.start()       
   

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                sys.exit()
                
            continue

        except Exception as e:
            # Any other exception - something happened, exit
            print("Reading error: {}".format(str(e)))
            sys.exit()


if __name__ == "__main__":
    server_communication = threading.Thread(target= server_sender)
    server_reciver = threading.Thread(target=server_reciver)
    game_thread = threading.Thread(target= game.run)

    server_reciver.start()
