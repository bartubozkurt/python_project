import socket
hostname = socket.gethostname()
IpAddress = socket.gethostbyname(hostname)
print("My IP Address is : " + IpAddress)