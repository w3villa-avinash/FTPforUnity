from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import threading
import os 


class MyHandler(FTPHandler):
        UNITY_IP = "127.0.0.1"
        UNITY_PORT = 5555

def on_file_received(self, file):
        print(f"File received: {file}")
        self.notify_unity("File received: {}".format(file))

def on_file_sent(self, file):
        print(f"File sent: {file}")
        self.notify_unity("Mesh Generation {}".format(file))

def notify_unity(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((self.UNITY_IP, self.UNITY_PORT))
                s.sendall(message.encode("utf-8"))
            except Exception as e:
                print(f"Failed to notify Unity: {e}")

def run_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "password", "/Users/apple/Documents/Python/LocalData", perm="elradfmw")

    handler = MyHandler
    handler.authorizer = authorizer

    server = FTPServer(("127.0.0.1",21 ), handler)
    print("127.0.0.1:21 FTP Server ")
    server.serve_forever()

if __name__ == "__main__":
    ftp_thread = threading.Thread(target=run_ftp_server)
    ftp_thread.start()
    ftp_thread.join()