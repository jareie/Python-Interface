
import struct
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

class BaseValue:
    def __init__(self):
        self.value = -1
        self.format = ""
        self.order = ">"

    def decode( self, data ):
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

class MsgIndexArray(BaseValue):
    def __init__(self):
        super().__init__()
        self.arraySize = 0
        self.value = []

    # def decode(self, data):
        
