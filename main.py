import socket
import msg_types as MSGS

other_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
other_socket.bind( ( "", 20002 ) )


header = MSGS.Header()
while True:
    msg = other_socket.recvfrom(2000)
    header.decode( msg[0] )
    print( header )
