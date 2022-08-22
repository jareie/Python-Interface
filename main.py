import socket
import msg_types as MSGS

# example program. Should be able to make a sender as well
# not only a receiver

#only UDP for now
#since it is simple :P
other_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
other_socket.bind( ( "", 20002 ) )

# ideally only define the header once, and take care of
# the handling in the main code, as different msgs might
# have different structures
header = MSGS.Header()
testMsg = MSGS.Test()

while True:
    msg = other_socket.recvfrom(2000)
    # header.decode( msg[0] )
    # print( header )

    #Currently working on my base array
    testMsg.decode( msg[0] )
    print( testMsg )