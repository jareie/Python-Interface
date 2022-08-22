import struct
import msg_base as Base

class Header(Base.TypeBase):
    #initialize the values and say what they are
    def __init__(self):
        super().__init__()
        self.id = Base.MsgInt()
        self.size = Base.MsgInt()
        self.time = Base.MsgInt()
        self.bif = Base.MsgInt()
        self.extra = Base.MsgInt()


# tyo = Header()

# print( tyo.id )
# tyo.id = 12
# print( tyo.id )
# print( tyo.decode( bytes("HOla amigoasasas", encoding="ascii") ) )

# print( tyo.bif.value )
# print(tyo)