import socket
import concurrent.futures

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] {ip}:{port} - AÇIK")
            s.close()
    except Exception as e:
        print(f"[-] Hata: {e}")

if __name__ == "__main__":
    target = input("Hedef IP: ")
    port_range = input("Port Aralığı (örn: 70-100): ").split('-')
    
    start_port = int(port_range[0])
    end_port = int(port_range[1])
    
    print(f"[*] {target} taraması başlatıldı...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port+1):
            executor.submit(scan_port, target, port)
