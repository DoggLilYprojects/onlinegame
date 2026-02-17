import socket
from _thread import * 
import sys
from player import Player
import pickle

hostname = socket.gethostname()
server = socket.gethostbyname(hostname)
port = 5555

print("Hostname: ", hostname)
print("Local IP: ", server)
print("Port:     ", port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Server started, listening for connection")

players = dict()
online_players = set()

def thr_client(connection):
    nickname = connection.recv(2048).decode("utf-8")
    print(f"{nickname} has joined this server")
    try:
        connection.send(pickle.dumps(players[nickname]))
    except:
        players[nickname] = Player(nickname, (255,0,0))
        connection.send(pickle.dumps(players[nickname]))
    online_players.add(nickname)

    reply = ""
    while True:
        try:
            data = pickle.loads(connection.recv(2048))
            #print(data)
            if not data:

                #print("No reply")

                break
            else:
                players[nickname] = data

                reply = {players[n] for n in online_players if n != nickname}
        
                #print("Data: ", data)
                                
            connection.sendall(pickle.dumps(reply))
            #print("Reply: ", reply)

        except:
            print(f"{nickname} has disconnected")
            break

    print(f"Connection with {nickname} lost")
    online_players.remove(nickname)
    connection.close()

while True:
    connection, address = s.accept()
    print("Connected to:", address)

    start_new_thread(thr_client, (connection,))
