from abc import ABC,abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass 


class WordDocument(Document):
    def open(self):
        print('Opening a Word document.......')

class PdfDocument(Document):
    def open(self):
        print('Opening PDF file.....')

class HTMLDocument(Document):
    def open(self):
        print('opening HTML file......')


class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

class WordDocumentFactory(DocumentFactory):
    def create_document(self):
        return WordDocument()


class PdfDocumentFactory(DocumentFactory):
    def create_document(self):
        return PdfDocument()


def process_document(factory:DocumentFactory):
    document = factory.create_document()
    document.open()


word_factory = WordDocumentFactory()
process_document(word_factory)

pdf_facotry = PdfDocumentFactory()
process_document(pdf_facotry)