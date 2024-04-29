import socket
from _thread import *
import threading
import sys
import errno

# print_lock = threading.Lock()


def threaded(conn, address):
    while True:
        data = conn.recv(1024).decode()
        if data:
            print("Data received: {}".format(data))
        else:
            break
        try:
            if data.lower().strip() == 'hi':
                message = 'hello'
            elif data.lower().strip() == 'bye':
                sys.exit()
            else:
                message = str(eval(data))
        except:
            message = "INVALID STATEMENT"
        conn.sendall(message.encode())
        print("Response sent to {} = {}".format(address, message))

    # connection closed
    conn.close()


def server_program():
    if len(sys.argv) == 3:
        # get the hostname
        host = sys.argv[1]
        # get the port number
        port = int(sys.argv[2])

        # Creating an IPv4 TCP socket
        server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # get instance
        try:
            # The bind() function takes tuple as argument
            # bind host address and port together
            server_socket.bind((host, port))

            # configure how many client the server can listen simultaneously
            # 0, max unaccepted connections before refusing
            server_socket.listen(0)

            while True:
                # receive data stream. it won't accept data packet greater than 1024 bytes
                conn, address = server_socket.accept()  # accept new connection
                print("Connection from: " + str(address))
                threading.Thread(
                    target=threaded, args=(conn, address)).start()
        except socket.error as e:
            if e.errno == errno.EADDRINUSE:
                print("Port {} is already in use".format(port))
            else:
                # something else raised the socket.error exception
                print(e)
        server_socket.close()


# def Main():
#     if len(sys.argv) == 3:
#         s = socket.socket
#         host = sys.argv[1]
#         port = int(sys.argv[2])

#         # AF_INET for ipv4 and SOCK_STREAM for TCP
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

#             try:
#                 # Associate the socket with a specific network interface and port number
#                 # Accepts a two-touple (host,port)
#                 # Host can be a hostname, IP address, or empty string
#                 # Port 1-65535 Unpriviledge ports >1024
#                 s.bind((host, port))
#                 print("Socket binded to port:", port)

#                 # listen() enables a server to accept() connections.
#                 # It makes it a “listening” socket
#                 # Backlog parameter as 0, max unaccepted connections before refusing
#                 s.listen(0)
#                 print("{}:{} is listening".format(host, port))

#                 # a forever loop until client wants to exit
#                 while True:

#                     # returns a new socket object and a tuple holding the (host, port) of the client
#                     c, addr = s.accept()
#                     print("Connected to {}".format(addr))
#                     threading.Thread(target=threaded, args=(c, addr)).start()
#             except socket.error as e:
#                 if e.errno == errno.EADDRINUSE:
#                     print("Port {} is already in use".format(port))
#                 else:
#                     # something else raised the socket.error exception
#                     print(e)

#         s.close()
    else:
        print("Invalid Arguments: python server4.py 'address' 'port'")


if __name__ == "__main__":
    server_program()
