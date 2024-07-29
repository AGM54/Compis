# Generated from TerraformSubset.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,85,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,5,0,25,8,0,10,0,12,0,28,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,5,2,39,8,2,10,2,12,2,42,
        9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,5,4,52,8,4,10,4,12,4,55,9,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,6,5,6,64,8,6,10,6,12,6,67,9,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,8,5,8,76,8,8,10,8,12,8,79,9,8,1,9,1,9,1,9,1,9,
        1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,82,0,26,1,0,0,0,2,31,1,0,
        0,0,4,40,1,0,0,0,6,43,1,0,0,0,8,53,1,0,0,0,10,56,1,0,0,0,12,65,1,
        0,0,0,14,68,1,0,0,0,16,77,1,0,0,0,18,80,1,0,0,0,20,25,3,2,1,0,21,
        25,3,6,3,0,22,25,3,10,5,0,23,25,3,14,7,0,24,20,1,0,0,0,24,21,1,0,
        0,0,24,22,1,0,0,0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,
        1,0,0,0,27,29,1,0,0,0,28,26,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,
        32,5,1,0,0,32,33,5,8,0,0,33,34,5,2,0,0,34,35,3,4,2,0,35,36,5,3,0,
        0,36,3,1,0,0,0,37,39,3,18,9,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,
        1,0,0,0,40,41,1,0,0,0,41,5,1,0,0,0,42,40,1,0,0,0,43,44,5,4,0,0,44,
        45,5,8,0,0,45,46,5,8,0,0,46,47,5,2,0,0,47,48,3,8,4,0,48,49,5,3,0,
        0,49,7,1,0,0,0,50,52,3,18,9,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,
        1,0,0,0,53,54,1,0,0,0,54,9,1,0,0,0,55,53,1,0,0,0,56,57,5,5,0,0,57,
        58,5,8,0,0,58,59,5,2,0,0,59,60,3,12,6,0,60,61,5,3,0,0,61,11,1,0,
        0,0,62,64,3,18,9,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,
        66,1,0,0,0,66,13,1,0,0,0,67,65,1,0,0,0,68,69,5,6,0,0,69,70,5,8,0,
        0,70,71,5,2,0,0,71,72,3,16,8,0,72,73,5,3,0,0,73,15,1,0,0,0,74,76,
        3,18,9,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,
        78,17,1,0,0,0,79,77,1,0,0,0,80,81,5,8,0,0,81,82,5,7,0,0,82,83,5,
        9,0,0,83,19,1,0,0,0,6,24,26,40,53,65,77
    ]

class TerraformSubsetParser ( Parser ):

    grammarFileName = "TerraformSubset.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'provider'", "'{'", "'}'", "'resource'", 
                     "'variable'", "'output'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "STRING", "WS" ]

    RULE_terraform = 0
    RULE_provider = 1
    RULE_providerBody = 2
    RULE_resource = 3
    RULE_resourceBody = 4
    RULE_variable = 5
    RULE_variableBody = 6
    RULE_output = 7
    RULE_outputBody = 8
    RULE_keyValuePair = 9

    ruleNames =  [ "terraform", "provider", "providerBody", "resource", 
                   "resourceBody", "variable", "variableBody", "output", 
                   "outputBody", "keyValuePair" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    IDENTIFIER=8
    STRING=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TerraformContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TerraformSubsetParser.EOF, 0)

        def provider(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.ProviderContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.ProviderContext,i)


        def resource(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.ResourceContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.ResourceContext,i)


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.VariableContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.VariableContext,i)


        def output(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.OutputContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.OutputContext,i)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_terraform

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerraform" ):
                listener.enterTerraform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerraform" ):
                listener.exitTerraform(self)




    def terraform(self):

        localctx = TerraformSubsetParser.TerraformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_terraform)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 114) != 0):
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 20
                    self.provider()
                    pass
                elif token in [4]:
                    self.state = 21
                    self.resource()
                    pass
                elif token in [5]:
                    self.state = 22
                    self.variable()
                    pass
                elif token in [6]:
                    self.state = 23
                    self.output()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(TerraformSubsetParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProviderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TerraformSubsetParser.IDENTIFIER, 0)

        def providerBody(self):
            return self.getTypedRuleContext(TerraformSubsetParser.ProviderBodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_provider

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProvider" ):
                listener.enterProvider(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProvider" ):
                listener.exitProvider(self)




    def provider(self):

        localctx = TerraformSubsetParser.ProviderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_provider)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(TerraformSubsetParser.T__0)
            self.state = 32
            self.match(TerraformSubsetParser.IDENTIFIER)
            self.state = 33
            self.match(TerraformSubsetParser.T__1)
            self.state = 34
            self.providerBody()
            self.state = 35
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProviderBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.KeyValuePairContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.KeyValuePairContext,i)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_providerBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProviderBody" ):
                listener.enterProviderBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProviderBody" ):
                listener.exitProviderBody(self)




    def providerBody(self):

        localctx = TerraformSubsetParser.ProviderBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_providerBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 37
                self.keyValuePair()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(TerraformSubsetParser.IDENTIFIER)
            else:
                return self.getToken(TerraformSubsetParser.IDENTIFIER, i)

        def resourceBody(self):
            return self.getTypedRuleContext(TerraformSubsetParser.ResourceBodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_resource

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResource" ):
                listener.enterResource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResource" ):
                listener.exitResource(self)




    def resource(self):

        localctx = TerraformSubsetParser.ResourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_resource)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(TerraformSubsetParser.T__3)
            self.state = 44
            self.match(TerraformSubsetParser.IDENTIFIER)
            self.state = 45
            self.match(TerraformSubsetParser.IDENTIFIER)
            self.state = 46
            self.match(TerraformSubsetParser.T__1)
            self.state = 47
            self.resourceBody()
            self.state = 48
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResourceBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.KeyValuePairContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.KeyValuePairContext,i)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_resourceBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResourceBody" ):
                listener.enterResourceBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResourceBody" ):
                listener.exitResourceBody(self)




    def resourceBody(self):

        localctx = TerraformSubsetParser.ResourceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_resourceBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 50
                self.keyValuePair()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TerraformSubsetParser.IDENTIFIER, 0)

        def variableBody(self):
            return self.getTypedRuleContext(TerraformSubsetParser.VariableBodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = TerraformSubsetParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(TerraformSubsetParser.T__4)
            self.state = 57
            self.match(TerraformSubsetParser.IDENTIFIER)
            self.state = 58
            self.match(TerraformSubsetParser.T__1)
            self.state = 59
            self.variableBody()
            self.state = 60
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.KeyValuePairContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.KeyValuePairContext,i)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_variableBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableBody" ):
                listener.enterVariableBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableBody" ):
                listener.exitVariableBody(self)




    def variableBody(self):

        localctx = TerraformSubsetParser.VariableBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 62
                self.keyValuePair()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TerraformSubsetParser.IDENTIFIER, 0)

        def outputBody(self):
            return self.getTypedRuleContext(TerraformSubsetParser.OutputBodyContext,0)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)




    def output(self):

        localctx = TerraformSubsetParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(TerraformSubsetParser.T__5)
            self.state = 69
            self.match(TerraformSubsetParser.IDENTIFIER)
            self.state = 70
            self.match(TerraformSubsetParser.T__1)
            self.state = 71
            self.outputBody()
            self.state = 72
            self.match(TerraformSubsetParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValuePair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TerraformSubsetParser.KeyValuePairContext)
            else:
                return self.getTypedRuleContext(TerraformSubsetParser.KeyValuePairContext,i)


        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_outputBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputBody" ):
                listener.enterOutputBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputBody" ):
                listener.exitOutputBody(self)




    def outputBody(self):

        localctx = TerraformSubsetParser.OutputBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_outputBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 74
                self.keyValuePair()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValuePairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TerraformSubsetParser.IDENTIFIER, 0)

        def STRING(self):
            return self.getToken(TerraformSubsetParser.STRING, 0)

        def getRuleIndex(self):
            return TerraformSubsetParser.RULE_keyValuePair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyValuePair" ):
                listener.enterKeyValuePair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyValuePair" ):
                listener.exitKeyValuePair(self)




    def keyValuePair(self):

        localctx = TerraformSubsetParser.KeyValuePairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_keyValuePair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(TerraformSubsetParser.IDENTIFIER)
            self.state = 81
            self.match(TerraformSubsetParser.T__6)
            self.state = 82
            self.match(TerraformSubsetParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





