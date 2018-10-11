# SWAMI KARUPPASWAMI THUNNAI
import socket
from threading import Thread

def handle_client(client,type):
    if type==0:
        receive = client.recv(1024)
        print("[*] Received message from client: %s"%str(receive))
    else:
        receive = client.recvfrom(1024)
        print("[*] Received message from client: "%str(receive))
    if type==0:
        print("[*] Bazooka is on TCP mode")
        client.send(b"You just connected to NetWorkers Server")
    else:
        print("[*] Bazooka is on UDP mode")
        client.send(b"you've just connected to networker's server")
    client.close()

def handle_client_wolf(client,type,location):
    x = open(location,"rb")
    file = x.readlines()
    if type==0:
        receive = client.recv(1024)
        print("[*] Received message from client: %s"%str(receive))
    else:
        receive = client.recvfrom(1024)
        print("[*] Received message from client: %s"%str(receive))
    if type==0:
        print("[*] Bazooka is on TCP mode")
        for i in file:
            client.send(i)
    else:
        print("[*] Bazooka is on UDP mode")
        client.send(b"you've just connected to networker's server")
    client.close()
def handle_client_wolf_save(client,type):
    if type==0:
        receive = client.recv(1024)
        print("[*] Received message from client: %s"%str(receive))
        file = open("logs.txt","a")
        file.write("\n")
        file.write(str(receive))
        file.close()
    client.close()
def handle_client_wolf_send(client,type):
    if type==0:
        msg = input("[*] Message : \n")
        client.send(msg.encode("UTF-8"))
        receive = client.recv(1024)
        print("[*] Received message from client: %s"%str(receive))
    client.close()

class Servers:
    def tcp_basic(self,listen_on,listen_port):
        print("[*] NetWorker - The Network Bazooka Basic TCP server")
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((listen_on,listen_port))
        server.listen(5)
        print("[*] server is listening on %s:%d" %(listen_on,listen_port))
        while True:
            client,addr = server.accept()
            print("[*] Accepted connection from %s %d"%(addr[0],addr[1]))
            client_handler = Thread(target=handle_client,args=(client,0,))
            client_handler.start()
    def udp_basic(self,listen_on,listen_port):
        print("[*] NetWorker - The Network Bazooka Basic UDP server")
        server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        server.sendto(b"You have attempted to connect to Netoworker's UDP server",(listen_on,listen_port))
        server.bind((listen_on,listen_port))
    def tcp_cat(self,listen_on,listen_port):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((listen_on,listen_port))
        print("""
        =========================>NetWorker - The NetWork Bazooka's NetWolf<==========================
        Commands:
        --index to display an html file
        --inform to send some packets
        --save  saves the message sent by the client into a file
        """)
        option = input("Your Option: ")
        server.listen(5)
        if "--index" in option:
            location = input("Enter the location of the file")
            while True:
                client,addr = server.accept()
                print("[*] Accepted connection from %s %d"%(addr[0],addr[1]))
                client_handler = Thread(target=handle_client_wolf,args=(client,0,location,))
                client_handler.start()
        if "--save" in option:
            print("Output will be saved in logs.txt")
            while True:
                client,addr = server.accept()
                print("[*] Accepted connection from %s %d"%(addr[0],addr[1]))
                client_handler = Thread(target=handle_client_wolf_save,args=(client,0,))
                client_handler.start()
        if "--inform" in option:
            print("[*] Packets sending session - Bazooka is ready waiting for a connection")
            while True:
                client,addr = server.accept()
                print("[*] Accepted connection from %s %d"%(addr[0],addr[1]))
                client_handler = Thread(target=handle_client_wolf_send,args=(client,0,))
                client_handler.start()
