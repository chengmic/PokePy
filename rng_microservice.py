# ---------- RANDOM NUMBER GENERATOR MICROSERVICE ----------

import socket
import random

# create a socket at server side
socket_string = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind socket to port
server_address = ('localhost', 10000)
socket_string.bind(server_address)

#establish how many clients the server can listen to
socket_string.listen(1)

while True:
    conn, addr = socket_string.accept()

    random_num = random.randint(1, 1008)
    print (f'Your randomly generator number is: {random_num}\n')

    conn.sendall(str(random_num).encode())
    
    conn.close()