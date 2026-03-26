import socket

host = "scanme.nmap.org"
puerto_inicio = 1
puerto_fin = 100

print(f"Escaneando {host} del puerto {puerto_inicio} al {puerto_fin}...")
print("-" * 45)

for port in range(puerto_inicio, puerto_fin + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    resultado = s.connect_ex((host, port))

    if resultado == 0:
        print(f"Puerto {port} → ABIERTO")

    s.close()

print("-" * 45)
print("Escaneo completado.")