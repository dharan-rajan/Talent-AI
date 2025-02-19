from fastapi import FastAPI
import ollama

from services import DBService, LLMService

app = FastAPI()

import os
os.environ["OLLAMA_CUDA"] = "1"

import json


@app.get("/")
def read_root():
        jd ="""About the job
            As a Software Developer at Bucketlist Rewards, you will help create the next generation of our rewards and recognition program. You will work collaboratively with a cross-functional agile team and gain experience with a wide variety of tasks. We value clean pragmatic solutions, sustainable growth, and provide opportunities based on your interests. If you're passionate about software development and would like to join a diverse and experienced team, we're looking for someone like you!



            About Us: Bucketlist Rewards provides a leading B2B SaaS solution that allows organizations of all sizes to introduce effective rewards and recognition programs to its workforce. Our goal is to provide companies with an easy-to-use web platform that enables employers to reward team members in a meaningful way that matters to them, while achieving great business results and building better organizational cultures. When it comes to great company culture, the Bucketlist team walks the talk and we are proud to be Great Place to Work certified!



            Key Responsibilities:

            Programming in Python and Django, Angular, and React.
            Working frequently with Linux, PostgreSQL, Kubernetes, Docker, and cloud services (AWS).
            Learning best practices in regards to design, testing and automation.
            Participating in agile ceremonies and other collaborative team activities.
            Involvement with DevOps, QA, Support as well as product development.


            Required Skills for Success:

            At least 3 years of full stack development experience.
            At least 3 years of Object-oriented programming.
            BSc in Computer Science, Software Engineering or equivalent.
            Positive attitude and a desire to learn.
            Excellent problem solving skills.
            Comfort working independently and with a remote team.
            Passion for software design using recognized best practices.
            Basic Linux command-line literacy.
            Excellent English communication skills.
            Familiarity with git and project tracking software such as Jira.


            Nice to have:

            Experience programming with Python and Django.
            Experience programming with front-end frameworks such as React.
            Familiarity with design patterns and testing techniques.
            Familiarity with containers and cloud computing.
            Familiarity with CI/CD principles.


            Why Join Us?

            At Bucketlist, we believe in meaningful work and meaningful rewards. You’ll join a supportive, collaborative team that values your growth and provides opportunities to explore your interests. Together, we’re building a platform that helps organizations create better workplaces, one recognition at a time.



            The Perks:

            Growth Opportunities: Join a growing company where you’ll be part of a high-performing team with lots of potential.
            Remote Work: We are a distributed workplace (100% remote). This position is open to anyone located in a timezone that aligns with continental North America.
            Wellness Days: In addition to paid vacation days, we offer flexible paid time off to fit individual needs.
            Comprehensive Benefits Package: Includes health, dental, vision care, EFAP, and more.
            Annual Bucketlist Benefit: An additional paid day off and $$ to spend to help check items off your own bucket list!
            Rewards and Recognition: We drink our own champagne! We’ll help you achieve not just your career goals but your personal goals as well!


            Anticipated Salary Range: The base salary for this role is $80-110k CAD annually for candidates located in Canada. The final offer will consider factors such as your expertise and previous experience. For candidates located outside of Canada, the annual salary will be adjusted based on the local market expectations.



            At Bucketlist Rewards, we are committed to fostering a diverse, equitable, and inclusive workplace. We believe that varied perspectives drive innovation and creativity, and we welcome applicants from all backgrounds and experiences. We encourage individuals from underrepresented groups to apply, as we strive to build a team that reflects the diverse communities we serve. We are dedicated to creating an environment where everyone feels valued, respected, and empowered to contribute their best work."""
    
        # JD insights
        llm = LLMService()
        insights = llm.insights_query(jd)

        insights = insights['message']['content']
        
        # # Remove deep seek thinking
        # insights = insights.split("/think")[1]

        # # Chroma semantic search        
        data = DBService('resumes').queryDocuments([jd], 20)
        docs = data["documents"][0]
        ids = data["ids"][0]

        # # Scoring
        # res = llm.scoring_query(insights, docs[0]) # 3 resumes
        # res = res['message']['content']
        
        # # Fetch JSON
        # print(res)
        

        #Llama 
        res = llm.scoring_query(insights, docs[0])
        res = res['message']['content']
        # res = llm.json_fetcher(res)
        res = json.loads(res)

        res["id"]=ids[0]
        return res