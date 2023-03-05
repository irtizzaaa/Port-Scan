import socket

target = input("Enter the target IP address: ")
port_range = input("Enter the range of ports to scan (e.g. 1-1024): ")

# split the port range into a start and end port number
start_port, end_port = port_range.split("-")
start_port = int(start_port)
end_port = int(end_port)

# loop through each port in the range and attempt to connect to it
for port in range(start_port, end_port + 1):
    # create a new socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) # set a timeout of 1 second for each connection attempt
    
    # attempt to connect to the target IP address and port
    result = sock.connect_ex((target, port))
    
    # if the connection attempt succeeds, print a message to the console
    if result == 0:
        print(f"Port {port} is open!")
    
    # close the socket connection
    sock.close()
