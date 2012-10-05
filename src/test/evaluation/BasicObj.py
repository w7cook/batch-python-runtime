class BasicObj :

    def __init__(self, inc) :
        self.inc = inc
        self.y = 3
    
    def foo(self) :
        return self.inc

    def getImage(self, name) :
        img = open("tcp/" + name + '.jpg', "rb")
        buff = []
        try :
            byte = img.read(1)
            while byte != "" :
                buff.append(byte)
                byte = img.read(1)
        finally :
            img.close()
        
        return buff
    
    def call(self) :
        print "Call"
    
    def hello(self) :
        print "Hello"
    
    def bye(self) :
        print "Bye"


