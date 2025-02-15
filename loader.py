import os

from services import DBService, PDFService
from tests import DBTest

class Loader:
    def __init__(self):
        self.path = './resumes/'

    def load(self):
        dbService = DBService('resumes')
        for folder in os.scandir(self.path):
            if folder.is_dir():
                folder_path = os.path.join(self.path, folder.name)
                documents, ids, metadatas = [], [], []

                for file in os.scandir(folder_path):
                    pdf_path = os.path.join(folder_path, file.name)

                    id = str(file.name.split('.')[0])
                    ids.append(id)
                    
                    content = self.parse_pdf(pdf_path)
                    documents.append(content)

                    category = folder.name
                    metadatas.append({'category': category})
            
                dbService.addDocuments(documents, metadatas, ids)
                print(f"All the files in the {folder.name} have been loaded - {len(ids)} files")
        
    def parse_pdf(self, path):
        return PDFService().parse_pdf(path)

Loader().load()