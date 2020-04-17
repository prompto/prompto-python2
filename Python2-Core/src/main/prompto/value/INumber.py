from prompto.value.IValue import IValue

class INumber( IValue):
    
    def IntegerValue(self):
        raise Exception("Should never get there")


    def DecimalValue(self):
        raise Exception("Should never get there")