from antlr4 import Parser, Token

class AbstractParser(Parser):

    def __init__(self, input_, output):
        super(AbstractParser, self).__init__(input_, output)
        self.path = ""

    def isText(self, token, text):
        return text==token.text

    def was(self, type):
        return self.lastHiddenTokenType()==type

    def wasNot(self, type):
        return self.lastHiddenTokenType()!=type

    def wasNotWhiteSpace(self):
        return self.wasNot(getattr(self, "WS"))

    def willBe(self, type):
        return self._input.LA(1)==type

    def willBeIn(self, *types):
        return self._input.LA(1) in types

    def afterWillBeIn(self, skipType, *types):
        idx = 1
        next = self._input.LA(idx)
        while next == skipType:
            next = self._input.LA(idx)
        return next in types

    def willNotBe(self, type):
        return self._input.LA(1)!=type

    def nextHiddenTokenType(self):
        hidden = self._input.getHiddenTokensToRight(self._input.index-1)
        if hidden is None or len(hidden)==0:
            return 0
        else:
            return hidden[0].type

    def willBeAOrAn(self):
        return self.willBeText("a") or self.willBeText("an")

    def willBeText(self, text):
        return text==self._input.LT(1).text

    def lastHiddenTokenType(self):
        hidden = self._input.getHiddenTokensToLeft(self._input.index)
        if hidden is None or len(hidden)==0:
            return 0
        else:
            return hidden[-1].type

