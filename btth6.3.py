class Nguoi(object):
    def getGender( self):
       return "UnKnown"


class Nam( Nguoi):
    def getGender(self):
       return "Nam"

class Nu( Nguoi ):
    def getGender( self ):
       return "Nữ"

aNam = Nam ()
aNu= Nu()
print (aNam.getGender())
print (aNu.getGender())
