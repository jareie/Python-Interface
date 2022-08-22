import msg_base as Base

# if this is as standardized as it seems
# I might combine it with a generation system to remove
# some of the writing (which is what i am aiming for)

class Header(Base.TypeBase):
    #initialize the values and say what they are
    def __init__(self):
        super().__init__()
        self.id = Base.MsgInt()
        self.size = Base.MsgInt()
        self.time = Base.MsgInt()
        self.bif = Base.MsgInt()
        self.extra = Base.MsgInt()

class Test( Base.TypeBase ):
    def __init__(self):
        super().__init__()
        self.dat = Base.MsgFloat()
        self.ray = Base.MsgIndexArray()

# tyo = Header()

# print( tyo.id )
# tyo.id = 12
# print( tyo.id )
# print( tyo.decode( bytes("HOla amigoasasas", encoding="ascii") ) )

# print( tyo.bif.value )
# print(tyo)