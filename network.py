import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hostname = socket.gethostname()
        self.server = socket.gethostbyname(self.hostname)
        self.port = 5555
        self.obj = self.connect()
        print(self.obj)

    def getObject(self):
        return self.obj

    def connect(self):
        try:
            self.client.connect((self.server, self.port))
            return pickle.loads(self.client.recv(2048))
        except:
            print("Could not get any data from server")
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(str(e))


