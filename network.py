import socket
import pickle

class Network:
    def __init__(self, nickname):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hostname = socket.gethostname()
        self.server = socket.gethostbyname(self.hostname)
        self.port = 5555
        self.nickname = nickname
        self.obj = self.connect()
        print(self.obj)

    def getObject(self):
        return self.obj

    def connect(self):
        try:
            self.client.connect((self.server, self.port))
            self.client.send(str.encode(self.nickname))
            return pickle.loads(self.client.recv(2048))
        except:
            print("Could not get any data from server")
            pass

    def send(self, data):
        data = pickle.dumps(data)
        self.client.send(data)
        dataa = self.client.recv(2048)
        if not dataa:
            return None
        return pickle.loads(dataa)
