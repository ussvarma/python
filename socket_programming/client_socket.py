# client socket
# importing libraries
import socket


def main():
    host = '127.0.0.1'

    # Define the port on which you want to connect
    port = 12345

    # both parameters indicate address - family ipv4.
    # socket.SOCK_STREAM indicates connection-oriented TCP protocol.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host, port))

    while True:
        message = input("Enter space separated sequence: ")
        # message sent to server
        s.send(message.encode())

        # message received from server
        data = s.recv(1024)

        # print the received message
        print('Received from the server :', str(data.decode()))

        # ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break
    # close the connection
    s.close()


if __name__ == '__main__':
    main()
