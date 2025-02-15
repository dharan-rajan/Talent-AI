import chromadb
import PyPDF2

chroma_client = chromadb.PersistentClient("data/")

class DBService:
    def __init__(self, collectionName):
        self.collection = chroma_client.get_or_create_collection(collectionName)
    
    def addDocuments(self, documents, metadatas, ids):
        # For now the document and the embeddings are taken care by chroma
        self.collection.add(documents=documents, metadatas=metadatas, ids=ids)

    def queryDocuments(self, query_texts, topk):
        return self.collection.query(query_texts=query_texts, n_results=topk)
    
    def getCount(self):
        return self.collection.count()
    
    def reset(self):
       chroma_client.delete_collection(self.collection.name)


class PDFService:
    def parse_pdf(cls, path):
        try:
            with open(path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() + '\n'
            return text
        except Exception as e:
            print(f"Failed to parse {path}: {e}")
            return None
        
class LLMService:
    pass