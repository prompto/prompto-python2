from prompto.parser.AbstractParser import AbstractParser

# this is just to enable per dialect downcasting in the Java/C# runtimes
class AbstractOParser(AbstractParser):

    def __init__(self, input_, output):
        super(AbstractOParser, self).__init__(input_, output)
