# SWAMI KARUPPASWAMI THUNNAI
import socket

class Clients:
    def tcp_basic(self,host,port):
        print("[*] NetWorker report: creating sockets to establish a connection")
        try:
            client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print("[*] NetWorker report: sockets have been created")
        except socket.error:
            print("[*] NetWorker report: failed to create sockets")
        try:
            print("[*] NetWorker report: Connecting to the server")
            client.connect((host,port))
            print("[*] NetWorker report: Connection established!")
        except:
            print("[*] NetWorker report: failed to connect to the server")
        data = input("[*] NetWorker report: Enter the data to be sent => ")
        try:
           print("[*] NetWorker report: sending packets please wait...")
           client.send(data.encode("UTF-8"))
           print("[*] NetWorker report: sent the data! receiving response from the server")
        except socket.error:
            print("[*] NetWorker report: packets sending failed")
        print(client.recv(4096))

    def udp_basic(self,host,port):
        print("[*] NetWorker report: creating sockets to establish a connection")
        try:
            client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            print("[*] NetWorker report: sockets have been created")
        except socket.error:
            print("[*] NetWorker report: failed to create sockets")
        data = ("[*] NetWorker report: Enter the data to be sent => ")
        try:
           print("[*] NetWorker report: sending packets please wait...")
           client.sendto(data.encode("UTF-8"),(host,port))
           print("[*] NetWorker report: sent the data! receiving response from the server")
        except socket.error:
            print("[*] NetWorker report: packets sending failed")
        print(client.recvfrom(4096))
