import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234)) #wrong indentation here
s.listen(6)

while True:
  clientsocket, address = s.accept()
  print(f" {address} You are connected to the Akagami Server")
  clientsocket.send(bytes("THIS IS AKAGAMI DEV", "utf-8"))