START_OBJECT = "{".encode()
END_OBJECT = "}".encode()
START_ARRAY = "[".encode()
END_ARRAY = "]".encode()
VALUE_SEPARATOR = ":".encode()
FIELD_SEPARATOR = ",".encode()
DOUBLE_QUOTE = '"'.encode()

class State(object):
    NONE = 0
    BEGIN_OBJECT = 1
    WITHIN_OBJECT = 2
    BEGIN_VALUE = 3
    BEGIN_ARRAY = 4
    WITHIN_ARRAY = 5

# we use our own generator because we need a simple way
# to populate binaries and JSON simultaneously
# plus we want to write to a stream, not a string
class JSONGenerator(object):

    def __init__(self, stream):
        self.stream = stream
        self.states = []
        self.state = State.NONE


    def writeStartObject(self):
        if self.state in [State.BEGIN_OBJECT, State.WITHIN_OBJECT]:
            raise Exception("Invalid state: " + str(self.state))
        if self.state is State.WITHIN_ARRAY:
            self.stream.write(FIELD_SEPARATOR)
        self.states.append(self.state)
        self.stream.write(START_OBJECT)
        self.state = State.BEGIN_OBJECT


    def writeEndObject(self):
        if not self.state in [State.BEGIN_OBJECT, State.WITHIN_OBJECT]:
            raise Exception("Invalid state: " + str(self.state))
        self.stream.write(END_OBJECT)
        self.state = self.states.pop()
        if self.state is State.BEGIN_VALUE:
            self.state = State.WITHIN_OBJECT
        elif self.state is State.BEGIN_ARRAY:
            self.state = State.WITHIN_ARRAY


    def writeStartArray(self):
        if self.state in [State.BEGIN_ARRAY, State.WITHIN_ARRAY]:
            raise Exception("Invalid state: " + str(self.state))
        self.states.append(self.state)
        self.stream.write(START_ARRAY)
        self.state = State.BEGIN_ARRAY

    def writeEndArray(self):
        if not self.state in [State.BEGIN_ARRAY, State.WITHIN_ARRAY]:
            raise Exception("Invalid state: " + str(self.state))
        self.stream.write(END_ARRAY)
        self.state = self.states.pop()
        if self.state is State.BEGIN_VALUE:
            self.state = State.WITHIN_OBJECT

    def writeFieldName(self, name):
        if not self.state in [State.BEGIN_OBJECT, State.WITHIN_OBJECT]:
            raise Exception("Invalid state: " + str(self.state))
        if self.state==State.WITHIN_OBJECT:
            self.stream.write(FIELD_SEPARATOR)
        self.stream.write(DOUBLE_QUOTE)
        self.stream.write(name.encode())
        self.stream.write(DOUBLE_QUOTE)
        self.stream.write(VALUE_SEPARATOR)
        self.state = State.BEGIN_VALUE


    def writeString(self, value):
        if self.state in [State.BEGIN_OBJECT, State.WITHIN_OBJECT]:
            raise Exception("Invalid state: " + str(self.state))
        if self.state is State.WITHIN_ARRAY:
            self.stream.write(FIELD_SEPARATOR)
        self.stream.write(DOUBLE_QUOTE)
        self.stream.write(value.encode())
        self.stream.write(DOUBLE_QUOTE)
        if self.state is State.BEGIN_VALUE:
            self.state = State.WITHIN_OBJECT
        elif self.state is State.BEGIN_ARRAY:
            self.state = State.WITHIN_ARRAY

    def writeLong(self, value):
        if self.state in [State.BEGIN_OBJECT, State.WITHIN_OBJECT]:
            raise Exception("Invalid state: " + str(self.state))
        if self.state is State.WITHIN_ARRAY:
            self.stream.write(FIELD_SEPARATOR)
        self.stream.write(str(value).encode())
        if self.state is State.BEGIN_VALUE:
            self.state = State.WITHIN_OBJECT
        elif self.state is State.BEGIN_ARRAY:
            self.state = State.WITHIN_ARRAY

    def writeNull(self):
        if self.state in [State.BEGIN_OBJECT, State.WITHIN_OBJECT]:
            raise Exception("Invalid state: " + str(self.state))
        if self.state is State.WITHIN_ARRAY:
            self.stream.write(FIELD_SEPARATOR)
        self.stream.write(str("null").encode())
        if self.state is State.BEGIN_VALUE:
            self.state = State.WITHIN_OBJECT
        elif self.state is State.BEGIN_ARRAY:
            self.state = State.WITHIN_ARRAY


