# SWAMI KARUPPASWAMI THUNNAI

#####################################################################################################
# The Networker - The NetWork Knife
#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

import sys
import socket
from clients import Clients
from servers import Servers


def display():
    print("=============================>Networker Ver 1.0<===========================")
    print()
    print("-c => client")
    print("-s => server")
    print("-TCP => establish a TCP client or server")
    print("-UDP => establish a UDP client or server")
    print("--basic => Basic type of server of client which sends and receives the packets")
    print("--type=cat => Bit advanced to the --basic mode")

def about():
    print("""=============================>Networker Ver 1.0<===========================
 Networker the Network Bozooka
 Programmed by Visweswaran
 Product of India
 A standard all in 1 tool for performing pen-testing in an environment where other packages failed
 Do not worry if other tools aren't there now for you got a Bazooka with you""")


clients = Clients()
servers = Servers()
