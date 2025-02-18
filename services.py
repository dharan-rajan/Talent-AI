import chromadb
import PyPDF2
import ollama

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
    def _evaluation_prompt(cls, job_description, resume):
        return f"""
            Given Job description and resumes
            
            ### Job Description:
            ----------------------------------------------------------------------------------------
            {job_description}
            ----------------------------------------------------------------------------------------

            ### Resume:
            ----------------------------------------------------------------------------------------
            {resume}
            ----------------------------------------------------------------------------------------

            Now Imagine Yourself that you are an expert resume evaluator. 
            Your job is to evaluate and score the resume based on how well they fit the given job description.

            Below are the key compontents that you need to evaluate - the score on each should be between 0 and 10:
            1. Skill Match (SM)
            2. Years of Experience (YOE)
            3. Industry Relevance (IR)
            4. Education Fit (EF)
            5. Recent Experience (RE)

            And return the JSON in the below format: the value should be score alone.
            Only JSON is accepted, no other explanations are needed anywhere in the response.
            {
                {"SM": "x","YOE": "y","IR": "z","EF": "u","RE": "v"}
            }
            """
    
    def jobdescription_insights(cls, job_description):
        return f"""
            Here is the job description:
            {job_description}
            ----------------------------------------------------------------------------------------

            Given the job description, cut down the unnecessary information and shrink the job description as per the below headings:
            1. Educational qualifications required - like the degree,schooling, diplomas (purely academic qualifications)
            2. Years of experience required - minimum how many experience is required and how far they are tolerable
            3. Hard Skills Required - Technologies, tools, languages, framework, etc
            4. Soft Skills Required - communication, leadership, collaboration, etc
            5. Key responsibilities - what the candidate is expected to do on their day to day job, how well are they expected to perform
            6. Nice to have skills - the skills that are not mandatory but good to have

            In all the above headings, the values should be extracted from the given job description, and it should be the same keywords and no modifications allowed.
            It should be descriptive and not subjective. 

            Things to note:
            This data will be used to evaluate the resumes and score them based on how well they match the job description.
            So make sure you extract the right information and make it as clear as possible.
            Need 100% accuracy and no mistakes are allowed. The information you are going to give must reflect the job description accurately and entirely.

            And most importantly - the total character count should not exceed 1500 characters and should not be less than 1200.
            """
    
    def insights_query(cls, job_description):
        return ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "assistant", "content": cls.jobdescription_insights(job_description), "stream": False}])
    
    def Scoring_LLMQuery(cls, job_description, resume):
        prompt = cls._evaluation_prompt(job_description, resume)
        print(prompt)
        return ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "assistant", "content": prompt, "stream": False , "options":{"max_tokens": 50}}])
        # return ollama.generate(model="deepseek-r1:1.5b", prompt=cls._evaluation_prompt(job_description, resume))
            # No more explanations are needed. Just the scores for each resume. More like a JSON array of objects.
            # Total score should be between 0-50 ( which you have to just sum up the above 5 scores)