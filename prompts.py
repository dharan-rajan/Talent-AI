def resume_evaluation(job_description, resume):
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
            {
                {"SM": "x","YOE": "y","IR": "z","EF": "u","RE": "v"}
            }

            Only JSON is a valid response. No explanations are needed. Just the scores for the resume in proper JSON format
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