import socket
import sys


def client_program():
    if len(sys.argv) == 3:
        s = socket.socket
        host = sys.argv[1]
        port = int(sys.argv[2])

        # Creating an IPv4 TCP socket
        client_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        client_socket.connect((host, port))  # connect to the server

        client_socket.settimeout(2)
        try:
            client_socket.send("Hi".encode())
            data = client_socket.recv(1024).decode()  # receive response

            print('Received from server: ' + data)

            message = input("Please Enter The Equation: ")  # take input

            while message.lower().strip() != 'bye':
                client_socket.send(message.encode())  # send message
                data = client_socket.recv(1024).decode()  # receive response

                print('Received from server: ' + data)  # show in terminal

                # again take input
                message = input("Please Enter The Equation: ")

            client_socket.close()  # close the connection
        except:
            print('not Possible to connect to the server right now! Try Later.')

    else:
        print("Invalid Arguments: python client.py 'host' 'port' 'equation'")


if __name__ == '__main__':
    client_program()
