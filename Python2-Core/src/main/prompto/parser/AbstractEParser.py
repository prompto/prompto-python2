from prompto.parser.AbstractParser import AbstractParser

# this is just to enable per dialect downcasting in the Java/C# runtimes
class AbstractEParser(AbstractParser):

    def __init__(self, input_, output):
        super(AbstractEParser, self).__init__(input_, output)
