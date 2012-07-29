class BasicObj :

    def __init__(self, inc) :
        self.inc = inc
    
    def foo(self, x) :
        return self.inc + x

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

