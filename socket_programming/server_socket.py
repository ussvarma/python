# server socket
import socket
# importing thread module
from _thread import *
import threading

lock = threading.Lock()


# thread function
def threaded(client):
    while True:
        # Below function returns longest increasing/decreasing sequence
        def long_seq(seq):
            print(seq)
            l = list(map(int, seq.split()))
            len_list = len(l)
            consq_great_list = []
            consq_small_list = []
            for i in range(len_list):
                inner_list = []
                for j in range(i, len_list - 1):
                    if l[j] < l[j + 1]:
                        inner_list.append(l[j])
                        # print(inner_list)
                    else:
                        break
                if (l[-2] < l[-1]) and l[j] == l[-2]:
                    inner_list.append(l[-1])
                else:
                    inner_list.append(l[j])
                if len(inner_list) > len(consq_great_list) and len(inner_list) > 1:
                    # print(inner_list)
                    consq_great_list = inner_list
            for i in range(len_list):
                inner_list = []
                for j in range(i, len_list - 1):
                    if l[j] > l[j + 1]:
                        inner_list.append(l[j])
                        # print(inner_list)
                    else:
                        break
                if (l[-2] > l[-1]) and l[j] == l[-2]:
                    inner_list.append(l[-1])
                else:
                    inner_list.append(l[j])
                if (len(inner_list) > len(consq_small_list)) and len(inner_list) > 1:
                    # print(inner_list)
                    consq_small_list = inner_list
                    # print(consq_small_list)

            if len(consq_great_list) < len(consq_small_list):
                return sum(consq_small_list)
            elif len(consq_great_list) > len(consq_small_list):
                return sum(consq_great_list)
            else:
                if consq_great_list.index(consq_great_list[0]) < consq_small_list.index(consq_small_list[0]):
                    return sum(consq_great_list)
                else:
                    return sum(consq_small_list)

            # print(consq_great_list)
            # print(consq_small_list)

        # data received from client
        data = client.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit
            lock.release()
            break

        # sum of longest sequence
        output = str(long_seq(data))

        # send back reversed string to client
        client.sendall(output.encode('utf-8'))

    # connection closed
    client.close()


def main():
    host = ""

    # reverse a port on your computer
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket bound to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        client, address = s.accept()

        # lock acquired by client
        lock.acquire()
        print('Connected to :', address[0], ':', address[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (client,))
    s.close()


if __name__ == '__main__':
    main()
