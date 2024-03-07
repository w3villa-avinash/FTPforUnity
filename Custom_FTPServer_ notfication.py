import os 
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from watcher import monitor_directory ,deletefile

class MyHandler(FTPHandler):

    def on_connect(self):
        print("%s:%s connected" % (self.remote_ip, self.remote_port))

    def on_disconnect(self):
        # do something when client disconnects
        pass

    def on_login(self, username):
        # do something when user login
        pass

    def on_logout(self, username):
        # do something when user log
        pass

    def on_file_sent(self, file):
        deletefile(file)
        pass

    def on_file_received(self, file):
        monitor_directory(directory_to_monitor , required_files , shell_script_path)
        pass

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        deletefile(file)
        import os
        os.remove(file)
def main():
    # INstantiate a dummy authorizer for managing " virtual" Users
    authorizer = DummyAuthorizer()

    #define a new user having dfull r/w permission and a read-only

    authorizer.add_user('user', '12345' , '.', perm= 'elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    handler =MyHandler
    handler.authorizer =authorizer
    #Define a customized banner ( string returned when client connects)
    handler.banner = " Pyftpdlib based ftp reday."
    #Passive conntect . Decomment in case you're behind a NAT.abs
    #handler.masquerade_address = 152.25.42.11'
    # #handler.passive_ports =range(60000 , 65535)

    #Instatiate FTP server class and listen on 0.0.0.0:2121
    address = ('', 2121)
    server = FTPServer(address , handler)

    #set a limit for connections 

    server.max_cons =256
    server.max_conc_per_ip =5

    #start ftp server
    server.serve_forever()


if __name__ =='__main__':
    shell_script_path = "/Users/apple/Documents/Python/LocalData/CreateModel.sh"
    directory_to_monitor = "/Users/apple/Documents/Python/LocalData/Input"
    required_files = ["trigger.txt"]
    
    main()


