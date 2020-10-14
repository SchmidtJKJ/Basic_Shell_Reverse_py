import socket
import sys

# creating the socket with exception handling
def socketing():
    try:
        global host
        global port
        global skt
        host = ""
        port = 9879
        skt = socket.socket()
    except socket.error as message:
        print("socket creation says: "+str(message))

# Binding the socket to it's parameters
    try:
        skt.bind((host, port))
        skt.listen(5)
    except socket.error as message:
        print("socket binding says: " + str(message)+"\nRe run the program")


# this function will be accepting the  connection
def accept_connection():
    connection, ipaddress = skt.accept()
    print("Here we have a connection with client IP "+ipaddress[0]+" on Port Number "+str(ipaddress[1]))
    dosomething(connection)
    connection.close()


def dosomething(conn):
    while 1:
        cmd = input()
        if cmd == "exit":
            conn.close()
            skt.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


if __name__ == '__main__':
    socketing()
    accept_connection()

