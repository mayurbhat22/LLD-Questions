#Before SOLID
from abc import ABC
class DocumentProcessor(ABC):
    def convert(self, file, conversion_type):
        if conversion_type == "PDFtoDOCX": 
            pass
        if conversion_type == "PDFtoJPEG":
            pass
    
    def upload_file(self, file):
        pass


#After S - Single Responsility Principle
"""
A class should have only one reason to change
"""

class FileConvertor(ABC):
    def convert(self, file, conversion_type):
        if conversion_type == "PDFtoDOCX": 
            pass
        if conversion_type == "PDFtoJPEG":
            pass

class UploadFiles(ABC):
    def upload_file(self, file):
        pass

#After O - Open/Closed Principle
"""
A class should open for extension, and closed for modification
"""
class FileConvertor(ABC):
    def convert(self, file):
        pass

class PDFtoDOCXConvertor(FileConvertor):
    def convert(self, file):
        print("PDF to DOCX")

class PDFtoJPEGConvertor(FileConvertor):
    def convert(self, file):
        print("PDF to JPEG")    

class UploadFiles(ABC):
    def upload_file(self, file):
        pass

class DocumentService:
    def __init__(self):
        self.converter = PDFtoDOCXConvertor()
        self.uploader = UploadFiles()

    def process(self, file):
        self.converter.convert(file)
        self.uploader.upload_file(file)
"""
Now, if any other type has to be added, just EXTEND the class to add another PDFtoTXT class.
"""

#After 'D' - Dependency Inversion Principle
"""
High level modules should not be dependent on the lower level modules
"""
class FileConvertor(ABC):
    def convert(self, file):
        pass

class PDFtoDOCXConvertor(FileConvertor):
    def convert(self, file):
        print("PDF to DOCX")

class PDFtoJPEGConvertor(FileConvertor):
    def convert(self, file):
        print("PDF to JPEG")    

class UploadFiles(ABC):
    def upload_file(self, file):
        pass

class DocumentService:
    def __init__(self, converter, uploader):
        self.converter = converter
        self.uploader = uploader

    def process(self, file):
        self.converter.convert(file)
        self.uploader.upload_file(file)

class Client:
    pdf_to_doc = PDFtoDOCXConvertor()
    uploader = UploadFiles()

    service = DocumentService(pdf_to_doc, uploader)
    service.process("Resume.pdf")
