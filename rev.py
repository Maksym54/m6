# Приклад коду для перевірки доступності порту 5432 в Windows
import socket

def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

if is_port_open("localhost", 5432):
    print("Port 5432 is open.")
else:
    print("Port 5432 is closed.")
