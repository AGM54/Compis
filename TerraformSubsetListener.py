# Generated from TerraformSubset.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TerraformSubsetParser import TerraformSubsetParser
else:
    from TerraformSubsetParser import TerraformSubsetParser

# This class defines a complete listener for a parse tree produced by TerraformSubsetParser.
class TerraformSubsetListener(ParseTreeListener):

    # Enter a parse tree produced by TerraformSubsetParser#terraform.
    def enterTerraform(self, ctx:TerraformSubsetParser.TerraformContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#terraform.
    def exitTerraform(self, ctx:TerraformSubsetParser.TerraformContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#provider.
    def enterProvider(self, ctx:TerraformSubsetParser.ProviderContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#provider.
    def exitProvider(self, ctx:TerraformSubsetParser.ProviderContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#providerBody.
    def enterProviderBody(self, ctx:TerraformSubsetParser.ProviderBodyContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#providerBody.
    def exitProviderBody(self, ctx:TerraformSubsetParser.ProviderBodyContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#resource.
    def enterResource(self, ctx:TerraformSubsetParser.ResourceContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#resource.
    def exitResource(self, ctx:TerraformSubsetParser.ResourceContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#resourceBody.
    def enterResourceBody(self, ctx:TerraformSubsetParser.ResourceBodyContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#resourceBody.
    def exitResourceBody(self, ctx:TerraformSubsetParser.ResourceBodyContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#variable.
    def enterVariable(self, ctx:TerraformSubsetParser.VariableContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#variable.
    def exitVariable(self, ctx:TerraformSubsetParser.VariableContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#variableBody.
    def enterVariableBody(self, ctx:TerraformSubsetParser.VariableBodyContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#variableBody.
    def exitVariableBody(self, ctx:TerraformSubsetParser.VariableBodyContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#output.
    def enterOutput(self, ctx:TerraformSubsetParser.OutputContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#output.
    def exitOutput(self, ctx:TerraformSubsetParser.OutputContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#outputBody.
    def enterOutputBody(self, ctx:TerraformSubsetParser.OutputBodyContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#outputBody.
    def exitOutputBody(self, ctx:TerraformSubsetParser.OutputBodyContext):
        pass


    # Enter a parse tree produced by TerraformSubsetParser#keyValuePair.
    def enterKeyValuePair(self, ctx:TerraformSubsetParser.KeyValuePairContext):
        pass

    # Exit a parse tree produced by TerraformSubsetParser#keyValuePair.
    def exitKeyValuePair(self, ctx:TerraformSubsetParser.KeyValuePairContext):
        pass



del TerraformSubsetParser