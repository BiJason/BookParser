import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from StringIO import StringIO
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
import string 
import re
import pyphen


# This program utilizes the Flesch reading-ease score(FRES), a metric to quantify and compute the difficulty of a text.
# This metric was devised by J. Peter Kincaid under US navy research in 1975. The formula is as follows:
# 206.835 - 1.015 (total words/total sentences) - 84.6(total syllables/total words)
# 
#


wordCounts = {}


class MyParser(object):
    def __init__(self, pdf):
        ## Snipped adapted from Yusuke Shinyamas 
        #PDFMiner documentation
        # Create the document model from the file
        parser = PDFParser(open(pdf, 'rb'))
        document = PDFDocument(parser)
        # Try to parse the document
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        # Create a PDF resource manager object 
        # that stores shared resources.
        rsrcmgr = PDFResourceManager()
        # Create a buffer for the parsed text
        self.retstr = StringIO()
        # Spacing parameters for parsing
        laparams = LAParams()
        codec = 'utf-8'
 
        # Create a PDF device object
        device = TextConverter(rsrcmgr, self.retstr, 
                               codec = codec, 
                               laparams = laparams)
        # Create a PDF interpreter object
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
         
        self.records            = []
         
        lines = self.retstr.getvalue().splitlines()
        for line in lines:
            self.handle_line(line)
     
    def handle_line(self, line):
        # Customize your line-by-line parser here
        self.records.append(line)
        

def countSyl(word):
    dic = pyphen.Pyphen(lang='en')
    return len((dic.inserted(word)).split('-'))


def analyzeFile(fileName):
    p = MyParser(fileName)
    sentences = len(re.split(r'(?<!\d)\.(?!\d)', p.retstr.getvalue()))
    words = 0
    syllables = 0
    for s in p.records:
        s = "".join([c for c in s if c.isalpha() or c in string.whitespace])
        s = s.lower()
        l = s.split()
        for w in l:
            words = words + 1
            syllables = syllables + countSyl(w)
    score = 206.835 - (1.015 * (float(words)/sentences)) - (84.6 * (float(syllables)/words))
    gradeLevel = (0.39 * (float(words)/sentences)) + (11.8 * (float(syllables)/words)) - 15.59
    minutes = words / 250
    analyzed = [sentences, words, syllables, score, round(gradeLevel), round(minutes)]
    return analyzed
    
    
        


    


    

