import socket

s = socket.socket()
s.bind(("0.0.0.0", 4444))
s.listen(1)
client, addr = s.accept()
print(f"[+] Connection from {addr}")

while True:
    cmd = input(">> ")
    if cmd == "exit":
        break
    client.send(cmd.encode())
    print(client.recv(2048).decode())
