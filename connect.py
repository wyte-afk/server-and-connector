import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

message = s.recv(1234)
print(message.decode("utf-8"))