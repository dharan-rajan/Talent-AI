import json
import re
import chromadb
import PyPDF2
import ollama

from prompts import jobdescription_insights, resume_evaluation, resume_insights, resume_work_experience

chroma_client = chromadb.PersistentClient("data/")

class DBService:
    def __init__(self, collectionName):
        self.collection = chroma_client.get_or_create_collection(collectionName)
    
    def addDocuments(self, documents, metadatas, ids):
        # For now the document and the embeddings are taken care by chroma
        self.collection.add(documents=documents, metadatas=metadatas, ids=ids)

    def getDocuments(self, ids):
        newids = []
        for id in ids:
            newids.append(str(id))
        print("-----------", newids)
        return self.collection.get(ids=newids, include=['documents', 'metadatas'])

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
    def __init__(self):
        self.model="llama3.2:1b"
        self.role="user"

    def jd_insights(self, job_description):
        prompt = jobdescription_insights(job_description)
        return ollama.chat(model=self.model, messages=[{"role": self.role, "content": prompt, "stream": False}])
    
    def resume_work_experience(self, resume):
        prompt = resume_work_experience(resume)
        print(prompt)
        return ollama.chat(model=self.model, messages=[{"role": self.role, "content": prompt, "stream": False, "options":{"max_tokens": 2000, "temperature": 0.7}}])
    
    def resume_insights(self, resume):
        prompt = resume_insights(resume)
        print(prompt)
        return ollama.chat(model=self.model, messages=[{"role": self.role, "content": prompt, "stream": False, "options":{"max_tokens": 2000, "temperature": 0.7}}])
    
    def scoring_query(self, job_description, resume):
        prompt = resume_evaluation(job_description, resume)
        return ollama.chat(model=self.model, messages=[{"role": self.role, "content": prompt, "stream": False , "options":{"max_tokens": 50, "temperature": 0.2}}])

    def json_fetcher(self, res):
        try:
            print(res)
            match = re.search(r'```json\n(.*?)\n```', res, re.DOTALL)
            json_str = match.group(1)
            return json.loads(json_str)
        except Exception as e:
            print(f"Failed to fetch JSON: {e}")
            return {}