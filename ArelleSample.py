import gettext, time, datetime
import xml.dom.minidom, xml.parsers.expat, os
from arelle import (Cntlr, FileSource, ModelManager, ModelXbrl, ModelDocument, XmlUtil, Version, ModelInstanceObject, ViewFileFactTable)
from arelle import (XbrlConst, XmlUtil, UrlUtil, ModelObject, ValidateFilingText, XmlValidate)
from arelle.ModelValue import (qname)

class ArelleCntlrSample(Cntlr.Cntlr):
    def __init__(self):
        super().__init__()

    def run(self):
        self.messages = []
        modelManager = ModelManager.initialize(self)
        # filesource = FileSource.FileSource("./aapl-20180929.xml")
        filesource = FileSource.FileSource("https://www.sec.gov/Archives/edgar/data/320187/000032018719000051/nke-20190531.xml")
        modelXbrl = modelManager.load("https://www.sec.gov/Archives/edgar/data/320187/000032018719000051/nke-20190531.xml", _("views loading")) 
        for fact in modelXbrl.facts:
            print(fact)
  
    def addToLog(self, message):
        if self.messages !=  None:
            self.messages.append(message + '\n')
        else:
            print(message) 
    
    def showStatus(self, message, clearAfter=None):
        pass

def main():
    # ArelleCntlrSample().run()
    # xbrl = Cntlr.Cntlr().modelManager.load('https://www.sec.gov/Archives/edgar/data/101984/000010198416000062/ueic-20151231.xml') 
    xbrl = Cntlr.Cntlr().modelManager.load('./nke-20190531.xml') 
    # ViewFileFactTable.viewFacts(xbrl, './ueic-20151231.csv')
    # modelDoc = ModelDocument.load(xbrl,'./ueic-20151231.xml')
    # mf = ModelInstanceObject.ModelFact()
    for fact in xbrl.undefinedFacts: 
        print(fact) 
    # modelManager = ModelManager.initialize(Cntlr.Cntlr())
    # filesource = FileSource.FileSource('./nke-20190531.xml')
    # xbrl=ModelXbrl.load(modelManager,'./nke-20190531.xml')
    # ViewFileFactTable.viewFacts(xbrl, './nke-20190531.csv')

if __name__ == "__main__":
    main()