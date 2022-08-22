
import struct

# One could probably make something more efficient
# such as gathering the data into bigger batches for
# the struct library ( this is only my assumption that there
# is an amount of settup by this library for each time it is used )
# Though with the introduction of arrays, i cant be bothered right now :P

# Base for all the types. Used for specifying things and stuff
class TypeBase:
    def __setattr__(self, __name: str, __value: any) -> None:
        # print( "Setting value:", __name,  __value )
        if __name not in self.__dict__:
            self.__dict__[ __name ] = __value
        else:
            self.__dict__[ __name ].value = __value
    
    def encode(self):
        return ""
    
    def decode(self, data):
        tempData = data
        for i in self.__dict__:
            tempData = self.__dict__[ i ].decode( tempData )
        return tempData

    def __str__(self):
        printable = ""
        for i in self.__dict__:
            printable += i + ": " + str( self.__dict__[ i ] ) + "\n"
        return printable


# This is the base for all my value types
# Is usefull for specifying other value types
class BaseValue:
    def __init__(self):
        self.value = -1
        self.format = ""
        self.order = ">"

    def decode( self, data ):
        print( self.format, data )
        size = struct.calcsize( self.order + self.format )
        self.value = struct.unpack( self.order + self.format, data[ : size ] )[0]
        return data[ size : ]

    def __str__(self):
        return str( self.value )

class MsgInt(BaseValue):
    def __init__(self):
        super().__init__()
        self.format = "l"
        self.value = 0

class MsgFloat(BaseValue):
    def __init__(self):
        super().__init__()
        self.format = "f"
        self.value = 0.0

# Expects an index in the message before the list
# ( Im intending one for end of message arrays,
# such that one does not need the size )
class MsgIndexArray(BaseValue):
    def __init__(self):
        super().__init__()
        self.format = "l"
        self.arraySize = 0
        self.sizeTest = MsgInt()
        self.value = []

    def decode(self, data):
        # print( struct.unpack( self.order + "l", data[0] )[0] )
        # self.arraySize = struct.unpack( self.order + "l", data[0] )[0]
        self.sizeTest.decode( data )
        print( self.sizeTest )
        for i in range( self.sizeTest.value ):
            print( i )
        return data
        
