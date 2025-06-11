import socket
from datetime import datetime

def port_scan(ip):
    open_ports = []
    for port in range(70, 100):  # Hızlı tarama için
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target = "192.168.1.1"  # Örnek hedef
    print(f"[*] {target} taraması başlatıldı: {datetime.now()}")
    ports = port_scan(target)
    print(f"[+] Açık portlar: {ports if ports else 'Bulunamadı'}")
