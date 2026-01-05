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

players = [
    Player("Bob", (0,0,255)),
    Player("Thomas", (255,0,0))
]
def thr_client(connection, currentPlayer):
    connection.send(pickle.dumps(players[currentPlayer]))
    reply = ""
    while True:
        try:
            data = pickle.loads(connection.recv(2048))
            if not data:
                '''
                print("No reply")
                '''
                break
            else:
                '''
                print(currentPlayer)
                '''
                players[currentPlayer] = data
                if currentPlayer == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                '''
                print("Data: ", data)
                print("Reply: ", reply)
                '''
            connection.sendall(pickle.dumps(reply))
        except:
            print(f"{currentPlayer} has disconnected")
            break

    print(f"Connection with {currentPlayer} lost")
    connection.close()

currentPlayer = 0
while True:
    connection, address = s.accept()
    #print("Connected to:", address)
    print(f"{currentPlayer} joined this server")

    start_new_thread(thr_client, (connection, currentPlayer))
    currentPlayer += 1
