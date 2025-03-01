def resume_evaluation(job_description, resume):
        print("length of job description and resume", len(job_description), len(resume))
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
            1. Skill Match (SM) - How well the skills in the resume match the job description
            2. Industry Relevance (IR) - Commonality of the industry, domain, or similarity in business accumen the candidate worked with.
            3. Educational Qualifications (EQ) - If the candidate posses the required educational qualifications as per the job description, else drop accordingly
            4. Relevant Experience (RE) - Relavance of the experience the candidate has with the job description
            5. Technical Knowledge (TK) - How well the technical knowledge of the candidate matches the job description

            And respond back ONLY in the below JSON format with the scores for each component. All other way of interpretation will be considered invalid.
            EXAMPLE JSON OUTPUT:
            {{
                "SM": x,
                "IR": x,
                "EQ": x,
                "RE": x
                "TK": x
            }}

            The score should be between 0 and 10
            The keys should be the same as mentioned above as well as the order.
            if not found relevant information, score 0 for that component.            

            Only JSON is a valid response. No summary / explanations are needed.
            
            """
    
def jobdescription_insights(job_description):
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

        And most importantly - the total character count should not exceed more than 1500 characters and not less than 1200.
        Anything that goes beyond this limit will be an invalid response because the token limit is just within 350 tokens.
        And dont add say anything like this is the best version or anything like that. Just the extracted information.
        """

def resume_work_experience(resume):
    return f"""
        Here is the candidate's resume and you are the expert in extracting the information from the resume.
        {resume}
        ----------------------------------------------------------------------------------------

        Given the resume - Summarize the work experience this candidate has obtained. 
        Extract all the industrial work experience the person posesses and not skip any (should not include the academic details).
        Also elaborate on what they have done and how it impacted the company. 
        For example: dont just say "Used photoshop for image optimization" - also say how they used it and what was the impact.
        The summary should be atleast 1500 characters and not more than 2000 characters.
        """

def resume_insights(resume):
    return f"""
        Here is the resume:
        {resume}
        ----------------------------------------------------------------------------------------

        Given the resume - summarize and return the JSON with the below keys:
        Please follow the below criterias mentioned in each key like how to extract the information and what to return.
        1. Education - degrees (only bachelors and masters)
        2. Hard Skills - Pragramming languages, frameworks, tools, etc
        3. Certifications - any certifications and licenses they have.
        4. Projects - any personal or open source projects they have worked on.
        5. Publications - any publications they have done.
        6. Volunteer - any volunteer work they have done.
        
        Respond with only the JSON. Do not include any introductory text, explanations, or additional comments
        Fill all the above collected information in the below JSON format and return it. 
        {{
            "Education": [
                {{
                    "Degree": x,
                    "Field": x,
                    "University": x,
                }},
            ],
            "Hard Skills": [
                x,y,z
            ],
            "Certifications": [
                {{
                    "Name": x,
                    "IssuedBy": x
                }},
            ],
            "Projects": [
                {{
                    "Name": x,
                    "Description": x
                }},
            ],
            "Publications": [
                {{
                    "Title": x,
                    "Publication": x
                }},
            ],
            "Volunteer": [
                {{
                    "Organization": x,
                    "Role": x
                }}
            ]
        }}
        """

    
   