import struct
import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = struct.pack( ">flllll", 1.1,4,2,1,7,10 )
print(data)
mySock.sendto( data, ("localhost", 20002) )
