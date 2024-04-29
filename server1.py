import socket
import errno
import sys
from os import execve


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
            server_socket.listen(1)
            conn, address = server_socket.accept()  # accept new connection
            print("Connection from: " + str(address))
            while True:
                # receive data stream. it won't accept data packet greater than 1024 bytes
                data = conn.recv(1024).decode()
                if not data:
                    # if data is not received break
                    break
                print("from connected user: " + str(data))
                try:
                    if data == 'Hi':
                        data = 'Hello'
                    else:
                        data = str(eval(data))

                except:
                    data = "Please send a proper statement"
                conn.send(data.encode())  # send data to the client

            conn.close()  # close the connection
        except socket.error as e:
            if e.errno == errno.EADDRINUSE:
                print("Port {} is already in use".format(port))
            else:
                # something else raised the socket.error exception
                print(e)


if __name__ == '__main__':
    server_program()
