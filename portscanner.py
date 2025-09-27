import socket
from IPy import IP

class PortScanner:
    banners=[]
    open_ports=[]

    def __init__(self,target,port):
        self.target=target
        self.port=port

    def scan(self):
        for port in range(1,self.port):
            self.port_scanner(port)

    def ipaddr(self):
        try:
            IP(self.target)
            return self.target
        except ValueError:
            return socket.gethostbyname(self.target)

    def port_scanner(self,port):
        try:
            converted_ip = self.ipaddr()
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip("\n").strip("\r")
                self.banners.append(banner)
            except:
                self.banners.append(" ")
        except:
            pass
