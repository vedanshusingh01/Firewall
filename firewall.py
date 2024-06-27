import socket

class Firewall:
    def __init__(self, host='0.0.0.0', port=12345):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.connections = []

    def start(self):
        self.sock.listen(5)
        print(f"Firewall listening on {self.host}:{self.port}...")
        while True:
            client_sock, client_addr = self.sock.accept()
            self.connections.append((client_sock, client_addr))
            print(f"Connection established with {client_addr}")
            self.handle_connection(client_sock, client_addr)

    def handle_connection(self, client_sock, client_addr):
        try:
            data = client_sock.recv(1024)
            if data:
                print(f"Received data from {client_addr}: {data.decode()}")
                # Implement packet filtering logic based on source IP and port
                src_ip = client_addr[0]
                src_port = client_addr[1]
                if self.is_allowed(src_ip, src_port):
                    print(f"Allowed connection from {client_addr}")
                    client_sock.send(b"Connection allowed.\n")
                else:
                    print(f"Blocked connection from {client_addr}")
                    client_sock.send(b"Connection blocked.\n")
            else:
                print(f"No data received from {client_addr}")
        except Exception as e:
            print(f"Error handling connection from {client_addr}: {str(e)}")
        finally:
            client_sock.close()

    def is_allowed(self, src_ip, src_port):
        # Example filtering rule: Allow connections only from localhost on port 8080
        allowed_ips = ['127.0.0.1']
        allowed_ports = [8080]
        if src_ip in allowed_ips and src_port in allowed_ports:
            return True
        return False

if __name__ == "__main__":
    firewall = Firewall()
    firewall.start()
